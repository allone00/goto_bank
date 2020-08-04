from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, Float
from sqlalchemy.orm import sessionmaker
import pika
import json


db_string = "postgres://banki:banki@db:5432/banki"

db = create_engine(db_string)  
base = declarative_base()

Session = sessionmaker(db)  
session = Session()

class User(base):
    __tablename__ = 'Users'
    id=Column(Integer, primary_key=True)
    reputation=Column('reputation', String(32))
    mac_address=Column('mac_address', String(32))
    hash_=Column('hash_', String(32))
    
    def __init__(self, reputation=None, mac_address=None,hash_=None):
        self.reputation = reputation
        self.mac_address = mac_address
        self.hash_ = hash_

class Credit(base):
    __tablename__ = "Credits"
    id=Column(Integer, primary_key=True)
    user_hash=Column('user_hash',Integer)
    sum=Column('sum',Integer)
    interest=Column('interest',Float)
    penny_rate=Column('penny_rate',Float)
    approved=Column('approved',Boolean)
    
    def __init__(self,user_hash=None,sum_=None,interest=None,penny_rate=None,approved=None):
        self.user_hash = user_hash
        self.sum = sum_
        self.interest = interest
        self.penny_rate = penny_rate
        self.approved = approved

base.metadata.create_all(db)

def addUser(user, session):
    session.add(user)

def addCredit(credit,session):
    session.add(credit)

def userExists(user_hash,session):
    exists = session.query(session.query(User).filter_by(user_hash=user_hash).exists()).scalar()  
    return exists


def callback(ch, method, properties, body):
    global session
    body = json.loads(body)
    #test if pika is working
    if(body['function']=="test_api"):
        print("Got the test function from api, returning stuff")
        channel.basic_publish(exchange='', routing_key='api', body=json.dumps({'function':'test_db','result':True}))  


    if(body['function']=="ncredit"):
        # check if user exists
        # if user does not exist create a new user
        if(userExists(body['user_hash'], session)==False):
            addUser(User(hash_=body['user_hash']))
        else:
            #user already exists, we just need to generate the credit 
            try:
                addCredit(Credit(user_hash=body['user_hash'],sum=body['sum'],interest=25,penny_rate=10,approved=False), session)
                result = True
            except:
                result = False
        #отправить api что все норм/фигово
        channel.basic_publish(exchange='', routing_key='api', body=json.dumps({'function':'ncredit_','result':result}))  
        return result

    
credentials = pika.PlainCredentials("rabbitmq", "rabbitmq")
parameters = pika.ConnectionParameters("rmq", 5672, "/", credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='db')
channel.basic_consume(on_message_callback=callback, queue='db', auto_ack=False)