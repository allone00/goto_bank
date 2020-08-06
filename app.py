from flask import Flask
from flask import render_template, request, redirect
import requests
import os
import logging
import json
import pika
app = Flask(__name__, static_folder='static')

testing = True

# message_from_ui = {}
# credentials = pika.PlainCredentials("rabbitmq", "rabbitmq")
# parameters = pika.ConnectionParameters("rmq", 5672, "/", credentials)
#connection = pika.BlockingConnection(parameters)
#channel = connection.channel()
#channel.queue_declare(queue='api')

@app.route('/')
@app.route('/<path:path>')
def hello_world(path='/'):
    return render_template('auth.html')

@app.route('/api/qwerty', methods=['GET','POST'])
def get_message():
    global testing
    app.logger.info("debug 1")
    message_from_ui = request.get_json()
    value = request.args.get('code')

    url = 'https://stonks.goto.msk.ru/o/token/'
    myobj = {'client_id': 'rvAyzLvmASDEw1DCDMShbdjNpsPR6I89IRiGgpoL', #if testing else 'M2mY5d4b6NcVKxr2XqKXSxZgpk78WK6ZaU3IxYDd',
            'client_secret': 'nIUUEC0sQSvehn03I4UTIHcEZmT7yCjn5uUzwD02PqbikQNid5jFRWlulGXBt1gQsmlEWAgirCpsUwsOmMQFx3bfgq0nxuvDZEl31lM1sSDvRLrpevcTsh9NNxe5xXIs',# if testing else '81ASvQUU6xYJzGei9r1HwkIcR3xZgFHrkMBlHtl5FifykxbbodQNPRixEQ5RwN4K5MSJIdqn4xXLWxqKDzfQ5kxPzZoWde6OsZ1rmaz8TKMNA8aOMHQ4Raxj8okxo2bs',
            'grant_type': 'authorization_code',
            'code': value}
    x = requests.post(url, data=myobj)
    token = json.loads(x.text)
    app.logger.info("debug 2")
    #get user info by token
    app.logger.info(f'Sending request, value:{value}, token:{token}')
    info = json.loads( requests.post("http://stonks.goto.msk.ru/api/bank/",headers={'Authorization':f'Bearer {token}'}) )
    app.logger.info("debug 3")
    transferring_to_db = {"function": "ncredit", "user_hash": token, "sum": message_from_ui["sum"], "mac_address": message_from_ui["mac"], "user_email":info["email"], "full_name":(info["first_name"]+info["last_name"])}
    channel.basic_publish(exchange='',
                    routing_key='db',
                    body=json.dumps(transferring_to_db))
    app.logger.info("debug 4")


@app.route('/auth', methods=['GET', 'POST'])
def request_auth():    
    return redirect(f'/form?code={request.args.get("code")}')


if __name__ == "__main__":
    # print " [x] Sent 'Hello World!'
    logging.info(os.environ.get('PROD', 8080))
    app.run(host='0.0.0.0', port=os.environ.get('PROD', 8080), debug=True)

