from flask import Flask, render_template,request  

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
    
# @app.route("/perform_operation", methods=['POST'])
@app.route("/", methods=['POST'])
def perform_operation():
    operation = request.form.get('operation')
    number1 = int(request.form.get('number1'))
    number2 = int(request.form.get('number2'))
    result = 0
    if operation == 'Add':
        result = number1+number2
    elif operation == 'Subtract':
        result = number1-number2
    elif operation == 'Multitply':
        result = number1*number2
    elif operation == 'Divide':
        if (number2==0):
            result = "Can not divide number by Zero"
        else:
            result = number1//number2    
    return render_template("index.html", result={'result':result})
    
if __name__ == "__main__":
    app.run(debug=True)