from flask import Flask
from flask import render_template, request, redirect
import requests
import os
import logging
import json
import pika
import time
import _thread
from flask import jsonify
app = Flask(__name__, static_folder='static')

token = ''
message_from_ui = {}
body = {}
testing = True
credentials = pika.PlainCredentials("rabbitmq", "rabbitmq")
parameters = pika.ConnectionParameters("rmq", 5672, "/", credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.queue_declare(queue='api')

"""
def callback(ch, method, properties, body):
    global credits
    body = json.loads(body)

    if(body["function"]=="listCredits_"):
        app.logger.info("Got credits!")
        credits = body["credits"]
        app.logger.info(credits)

channel.basic_consume(on_message_callback=callback, queue='db', auto_ack=False)
channel.start_consuming()"""


@app.route('/')
@app.route('/<path:path>')
def hello_world(path='/'):
    return render_template('auth.html')
"""
@app.route('/api/asdf')
def returnCredits():
    credits = None
    channel.basic_publish(exchange='', routing_key="cbs", body=json.dumps({"function":"listCredits"}))
    
    #wait for credits, then return the info
    while(credits is None):
        app.logger.info("a")
        time.sleep(0.01)

    app.logger.info(credits)
    return jsonify(credits)"""

@app.route('/api/qwerty', methods=['GET','POST'])
def get_message():
    global testing
    message_from_ui =  eval(list(request.form.to_dict().keys())[0])
    value = message_from_ui['code']
    url = 'https://stonks.goto.msk.ru/o/token/'
    myobj = {'client_id': 'rvAyzLvmASDEw1DCDMShbdjNpsPR6I89IRiGgpoL', #if testing else 'M2mY5d4b6NcVKxr2XqKXSxZgpk78WK6ZaU3IxYDd',
            'client_secret': 'nIUUEC0sQSvehn03I4UTIHcEZmT7yCjn5uUzwD02PqbikQNid5jFRWlulGXBt1gQsmlEWAgirCpsUwsOmMQFx3bfgq0nxuvDZEl31lM1sSDvRLrpevcTsh9NNxe5xXIs',# if testing else '81ASvQUU6xYJzGei9r1HwkIcR3xZgFHrkMBlHtl5FifykxbbodQNPRixEQ5RwN4K5MSJIdqn4xXLWxqKDzfQ5kxPzZoWde6OsZ1rmaz8TKMNA8aOMHQ4Raxj8okxo2bs',
            'grant_type': 'authorization_code',
            'code': value}
    x = requests.post(url, data=myobj)
    token = json.loads(x.text)["access_token"]
    #get user info by token
    info = json.loads(requests.get("http://stonks.goto.msk.ru/api/bank/", headers={'Authorization':f'Bearer {token}'}).text)
    app.logger.info("debug 3")
    transferring_to_db = {"function": "ncredit", "user_hash": token, "sum": message_from_ui["sum"], "mac_address": message_from_ui["mac"], "user_email":info["email"], "full_name":(info["first_name"]+" "+info["last_name"])}
    channel.basic_publish(exchange='',
                    routing_key='db',
                    body=json.dumps(transferring_to_db))
    return token

@app.route('/auth', methods=['GET', 'POST'])
def request_auth():
    return redirect(f'/form?code={request.args.get("code")}')
def callback(ch, method, properties, body):
    body = json.loads(body)

channel.basic_consume(on_message_callback=callback, queue='api', auto_ack=False)

@app.route('/api/bid', methods=['POST'])
def send_message():
    global body
    url = 'http://localhost:8081/api/bid'
    x = requests.post(url, data=body)
    message_to_ui = json.dumps(x)
    return message_to_ui

if __name__ == "__main__":
    # print " [x] Sent 'Hello World!'
    logging.info(os.environ.get('PROD', 8080))
    app.run(host='0.0.0.0', port=os.environ.get('PROD', 8080), debug=True)

channel.start_consuming()
