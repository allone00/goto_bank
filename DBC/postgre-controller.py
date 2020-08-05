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
    full_name=Column('full_name', String(32))
    email=Column('email', String(32))
    
    def __init__(self, reputation=None, mac_address=None,hash_=None):
        self.reputation = reputation
        self.mac_address = mac_address
        self.hash_ = hash_

class Credit(base):
    __tablename__ = "Credits"
    id=Column(Integer, primary_key=True)
    user_email=Column('user_email',String(32))
    sum=Column('sum',Integer)
    interest=Column('interest',Float)
    penny_rate=Column('penny_rate',Float)
    approved=Column('approved',Boolean)
    full_name=Column('full_name',String(32))
    
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
    exists = session.query(session.query(User).filter_by(email=email).exists()).scalar()  
    return exists

def creditExists(user_hash,session):
    exists = session.query(session.query(Credit).filter_by(user_email=user_email).exists()).scalar()  
    return exists

# def approveCredit(user_hash,appr,session):
#     credit = session.query(session.query(Credit).filter_by(user_hash=user_hash).first()
#     credit.approved = appr
#     session.commit()
#     return True


def callback(ch, method, properties, body):
    global session
    body = json.loads(body)
    #test if pika is working
    print("Got a message")
    if(body['function']=="test_api"):
        print("Recieved test")
        channel.basic_publish(exchange='', routing_key='api', body=json.dumps({'function':'test_db','result':True}))  


    if(body['function']=="ncredit"):
        # check if user exists
        # if user does not exist create a new user
        if(userExists(body['user_email'], session)==False):
            addUser(User(email=body['user_email']),session)
        
        addCredit(Credit(user_email=body['user_email'],sum_=body['sum'],interest=25,penny_rate=10,approved=False,full_name=body["full_name"]), session)
        session.commit()
        result = True

        #отправить api что все норм/фигово
        #channel.basic_publish(exchange='', routing_key='api', body=json.dumps({'function':'ncredit_','result':result}))  
        return result

    # if(body["function"]=="acredit"):
    #     #check if credit exists
    #     if(creditExists(body['user_hash'], session)):
    #         approveCredit(body["user_hash"],body["apprpved"], session)
    #         return True
    #     else:
    #         return False


    
credentials = pika.PlainCredentials("rabbitmq", "rabbitmq")
parameters = pika.ConnectionParameters("rmq", 5672, "/", credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='db')
channel.basic_consume(on_message_callback=callback, queue='db', auto_ack=False)
channel.start_consuming()