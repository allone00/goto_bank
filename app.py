from flask import Flask
from flask import render_template, jsonify, request
import requests
import os
import logging
import json
import pika
app = Flask(__name__, static_folder='static')

fake_variable = ''
credentials = pika.PlainCredentials("rabbitmq", "rabbitmq")
parameters = pika.ConnectionParameters("rmq", 5672, "/", credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='api')

@app.route('/')
@app.route('/<path:path>')
def hello_world(path='/'):
    return render_template('auth.html')


@app.route('/auth', methods=['GET', 'POST'])
def request_auth():
    global fake_variable
    value = request.args.get('code')
    url = 'https://stonks.goto.msk.ru/o/token/'
    myobj = {'client_id': 'M2mY5d4b6NcVKxr2XqKXSxZgpk78WK6ZaU3IxYDd',
             'client_secret': '81ASvQUU6xYJzGei9r1HwkIcR3xZgFHrkMBlHtl5FifykxbbodQNPRixEQ5RwN4K5MSJIdqn4xXLWxqKDzfQ5kxPzZoWde6OsZ1rmaz8TKMNA8aOMHQ4Raxj8okxo2bs',
             'grant_type': 'authorization_code',
             'code': value}
    x = requests.post(url, data=myobj)
    token = json.loads(x.text)
    fake_variable = token
    return token



@app.route('/login')
def rel_login():
    t = 'boo'
    return t.text



if __name__ == "__main__":
    
    transferring_to_db = {"function": "test_api", "user_hash": fake_variable, "sum": 20000}

    channel.basic_publish(exchange='',
                    routing_key='db',
                    body=json.dumps(transferring_to_db))

    # print " [x] Sent 'Hello World!'"
    connection.close()
    logging.info(os.environ.get('PROD', 8080))
    app.run(host='0.0.0.0', port=os.environ.get('PROD', 8080), debug=True)
