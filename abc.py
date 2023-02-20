from flask import Flask

app = Flask(__name__)

@app.route("/")
def info():
    return '''<b>Company Name:</b> ABC Corporation<br>
<b>Location</b>: India<br>
<b>Contact Detail</b>: 999-999-9999'''

@app.route("/welcome")
def welcome():
    return '''<h2>Welcome to ABC Corporation</h2>'''

if __name__=="__main__":
    app.run(host="0.0.0.0")