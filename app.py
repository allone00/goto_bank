from flask import Flask
from flask import render_template
import os
import logging
app = Flask(__name__, static_folder='static')


@app.route('/')
@app.route('/<path:path>')
def hello_world(path='/'):
    return render_template('auth.html')


if __name__ == "__main__":
    logging.info(os.environ.get('PROD', 8080))
    app.run(host='0.0.0.0', port=os.environ.get('PROD', 8080), debug=True)
