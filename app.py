from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route("/input")
def hello():
    data = request.args.get("x")
    return "Hello {}".format(data)

if __name__=="__main__":
    app.run(host="0.0.0.0")
