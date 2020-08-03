from flask import Flask
from flask import render_template, jsonify, request
import requests
import os
import logging
app = Flask(__name__, static_folder='static')

@app.route('/')
def hello_world():
    return render_template('auth.html')


@app.route('/auth', methods=['GET','POST'])
def request_auth():
    #value = request.args.get('code')
    value = 'eVxwq0GJy9NUdFkrdWWacZQdQgJBrG&state=random_state_string'
    url = 'https://stonks.goto.msk.ru/o/token/'
    myobj = {'client_id': 'M2mY5d4b6NcVKxr2XqKXSxZgpk78WK6ZaU3IxYDd',
             'client_secret': '81ASvQUU6xYJzGei9r1HwkIcR3xZgFHrkMBlHtl5FifykxbbodQNPRixEQ5RwN4K5MSJIdqn4xXLWxqKDzfQ5kxPzZoWde6OsZ1rmaz8TKMNA8aOMHQ4Raxj8okxo2bs',
             'grant_type': 'authorization_code',
             'code': value}


    x = requests.post(url, data=myobj)
    return x.text



if __name__ == "__main__":
    logging.info(os.environ.get('PROD', 8080))
    app.run(host='0.0.0.0', port=os.environ.get('PROD', 8080), debug=True)
