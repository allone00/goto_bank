from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, Float
from sqlalchemy.orm import sessionmaker, relationship
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
    
    def __init__(self, reputation=None, mac_address=None,hash_=None,full_name=None,email=None):
        self.reputation = reputation
        self.mac_address = mac_address
        self.hash_ = hash_
        self.full_name = full_name
        self.email = email

class Credit(base):
    __tablename__ = "Credits"
    id=Column(Integer, primary_key=True)
    user_email=Column('user_email',String(32))
    sum=Column('sum',Integer)
    interest=Column('interest',Float)
    penny_rate=Column('penny_rate',Float)
    approved=Column('approved',Boolean)
    full_name=Column('full_name',String(32))
    
    def __init__(self,sum_=None,interest=None,penny_rate=None,approved=None,full_name=None,user_email=None):
        self.sum = sum_
        self.interest = interest
        self.penny_rate = penny_rate
        self.approved = approved
        self.full_name = full_name
        self.user_email = user_email


# CBS
class Transactions(base):
    __tablename__ = "Transactions"
    id = Column(Integer, primary_key=True)
    money = Column("money", Integer)
    day = Column("day", Integer)
    hours_late = Column("hours_late", Integer)
    credit_id = Column('credit_id', Integer)


base.metadata.create_all(db)

def addUser(user, session):
    session.add(user)

def addCredit(credit,session):
    session.add(credit)

def userExists(user_name,session):
    exists = session.query(session.query(User).filter_by(full_name=user_name).exists()).scalar()  
    return exists

def creditExists(user_name,session):
    exists = session.query(session.query(Credit).filter_by(full_name=user_name).exists()).scalar()  
    return exists

def callback(ch, method, properties, body):
    global session
    body = json.loads(body)
    #test if pika is working
    print("Got a message")
    if(body['function']=="test_api"):
        print("Recieved test")
        channel.basic_publish(exchange='', routing_key='api', body=json.dumps({'function':'test_db','result':True}))  


    if(body['function']=="ncredit"):
        print(body)
        # check if user exists
        # if user does not exist create a new user
        if(userExists(body['full_name'], session)==False):
            addUser(User(email=body['user_email'],hash_=body["user_hash"],full_name=body["full_name"],mac_address=body["mac_address"]),session)
        
        addCredit(Credit(user_email=body['user_email'],sum_=body['sum'],interest=25,penny_rate=10,approved=False,full_name=body["full_name"]), session)
        session.commit()
        result = True
        return result

    if(body["function"]=="listCredits"):
        credits = []
        for cr in session.query(Credit).all():
            credits.append({"id":cr.id, "full_name":cr.full_name, "interest":cr.interest, "sum":cr.sum})
        
        channel.basic_publish(exchange='', routing_key='api', body=json.dumps({'function':'listCredits_','credits':credits}))  
        return True

    # CBS
    if(body["function"] == "table"):
        # credit =
        # ans = {"credit": {
        #     "sum": credit.sum,
        #     "interest": credit.interest,
        #     "penny_rate": credit.penny_rate
        # }, "transactions" [{
        #     "money": transaction.money
        #     "day": transaction.day
        #     "hours_late": transaction.hours_late
        # } for transaction in transactions]
        # }
        ans = {"type": "table", "sber": "bonk"}  # Test

        body = json.dumps(ans)
        connection = pika.BlockingConnection(pika.ConnectionParameters(
            "rmq", 5672, "/", pika.PlainCredentials("rabbitmq", "rabbitmq")))
        channel = connection.channel()
        channel.queue_declare(queue="cbs")
        channel.basic_publish(exchange='', routing_key="cbs", body=body)
        connection.close()


credentials = pika.PlainCredentials("rabbitmq", "rabbitmq")
parameters = pika.ConnectionParameters("rmq", 5672, "/", credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='db')
channel.basic_consume(on_message_callback=callback, queue='db', auto_ack=False)
channel.start_consuming()