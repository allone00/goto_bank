from flask import Flask
from flask import render_template, request, redirect
import requests
import os
import logging
import json
import pika
app = Flask(__name__, static_folder='static')

message_from_ui = {}
credentials = pika.PlainCredentials("rabbitmq", "rabbitmq")
parameters = pika.ConnectionParameters("rmq", 5672, "/", credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.queue_declare(queue='api')

@app.route('/')
@app.route('/<path:path>')
def hello_world(path='/'):
    return render_template('auth.html')

@app.route('/api/qwerty', methods=['GET'])
def get_message():
    global message_from_ui
    message_from_ui = request.json()
    print(message_from_ui)

# @app.route('/api/get_token', methods=['POST'])
# # def get_t():


@app.route('/auth', methods=['GET', 'POST'])
def request_auth():
    value = request.args.get('code')
    url = 'https://stonks.goto.msk.ru/o/token/'
    myobj = {'client_id': 'M2mY5d4b6NcVKxr2XqKXSxZgpk78WK6ZaU3IxYDd',
            'client_secret': '81ASvQUU6xYJzGei9r1HwkIcR3xZgFHrkMBlHtl5FifykxbbodQNPRixEQ5RwN4K5MSJIdqn4xXLWxqKDzfQ5kxPzZoWde6OsZ1rmaz8TKMNA8aOMHQ4Raxj8okxo2bs',
            'grant_type': 'authorization_code',
            'code': value}
    x = requests.post(url, data=myobj)
    token = json.loads(x.text)
    return redirect(f'/form=?token={token}')


    global message_from_ui

    #get user info by token
    
    info = json.loads( requests.post("http://stonks.goto.msk.ru/api/bank/",headers={'Authorization':f'Bearer {token}'}) )
    
    transferring_to_db = {"function": "ncredit", "user_hash": token, "sum": message_from_ui["sum"], "mac_address": message_from_ui["mac"], "user_email":info["email"], "full_name":(info["first_name"]+info["last_name"])}
    channel.basic_publish(exchange='',
                    routing_key='db',
                    body=json.dumps(transferring_to_db))
    return token



# @app.route('/login')
# def rel_login():
#     t = 'boo'
#     return t.text


if __name__ == "__main__":
    # print " [x] Sent 'Hello World!'
    logging.info(os.environ.get('PROD', 8080))
    app.run(host='0.0.0.0', port=os.environ.get('PROD', 8080), debug=True)

