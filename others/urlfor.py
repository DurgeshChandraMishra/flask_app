from flask import url_for
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'index page'

@app.route('/login')
def login():
    return 'login page'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='Durgesh'))
    print(url_for('profile', username='abc'))
