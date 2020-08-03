from flask import Flask
from flask import render_template

app = Flask(__name__, static_folder='static')


@app.route('/')
def hello_world():
    return render_template('auth.html')


if __name__ == "__main__":
    app.run(host='localhost', port=8080, debug=True)
