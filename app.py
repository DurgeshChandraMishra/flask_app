from flask import Flask
from flask import request,render_template,jsonify,url_for,redirect
import math
app = Flask(__name__)

@app.route("/",methods = ['GET'])
def index():
    return render_template('index.html',url = app.url_for("calculate"))

@app.route("/math",methods = ['POST'])
def calculate():
    try :
        if request.method == 'POST':

            num1 = int(request.form['num1'])
            num2 = int(request.form["num2"])
            operation = request.form["operation"]
            result = "{} of {} and {} is {}"
            if operation == 'add' :
                r = num1 + num2
            elif operation == 'subtract' :
                r = num1 - num2
            elif operation == 'multiply' :
                r = num1 * num2
            elif operation == 'divide' :
                r = num1 /num2
            else :
                r = math.log(num1)
            result.format(operation,str(num1),str(num2),str(r))
            return render_template("results.html",result = result.format(operation,str(num1),str(num2),str(r)))
    except Exception as e:
        return e

@app.route("/calculate",methods = ['POST'])
def calculateAPI():
    try :
        if request.method == 'POST':

            num1 = int(request.json['num1'])
            num2 = int(request.json["num2"])
            operation = request.json["operation"]
            result = "{} of {} and {} is {}"
            if operation == 'add' :
                r = num1 + num2
            elif operation == 'subtract' :
                r = num1 - num2
            elif operation == 'multiply' :
                r = num1 * num2
            elif operation == 'divide' :
                r = num1 /num2
            else :
                r = math.log(num1)
            result.format(operation,str(num1),str(num2),str(r))
            return {
                "result" : result.format(operation,str(num1),str(num2),str(r))
            }
    except Exception as e:
        return {
                "result" : e
            }

if __name__=="__main__":
    app.run(host="0.0.0.0")
