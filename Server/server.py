import imp
from flask import Flask, render_template, request, redirect, jsonify
from jinja2 import Undefined
from power_consumption_prediction import run_program

UPLOAD_FOLDER = 'static/uploads/'

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

# @app.route('/')
# def index():
#   return render_template('index.html')

@app.route('/power_pred/', methods = ['POST'])
def pow_pred():
    #date = "2022-04-30 12"
    #return str(run_program(request.form['date'])[0])
    return render_template('index.html', pred=str(run_program(request.form['date'])[0]))

@app.route('/')
def home_page():
    example_embed='This string is from python'
    return render_template('index.html', embed=example_embed)

# Get effect from date and hour, gets wind and temp
@app.route('/predict/<date>/<hour>', methods=['GET'])
def testfn(date, hour):
    # GET request
    if request.method == 'GET':
        message = {
            'status': 200,
            'date': date,
            'hour': hour,
            'prediction_value':str(run_program(date=date, hour=hour)[0])
            }
        return jsonify(message)

# Get effect from date, hour and temp. wind should be 0?
@app.route('/predict/<date>/<hour>/<temp>', methods=['GET'])
def testfn2(date, hour, temp):
    # GET request
    if request.method == 'GET':
        message = {
            'status': 200,
            'date': date,
            'hour': hour,
            'temp': temp,
            'prediction_value':str(run_program(date=date, hour=hour, temp=temp)[0])
            }
        return jsonify(message)

# If nothing is entered return a graph for the upcoming 24 hours
@app.route('/predict', methods=['GET'])
def testfn3():
    # GET request
    if request.method == 'GET':
        message = {
            'status': 200,
            'prediction_value':str(run_program()[0])
            }
        return jsonify(message)

# If only date: Get all avalible hours and plot on graph
@app.route('/predict/<date>', methods=['GET'])
def testfn4(date):
    # GET request
    if request.method == 'GET':
        prediction_value, temperatures, hours = run_program(date=date)
        message = {
            'status': 200,
            'date': date,
            'prediction_value':prediction_value,
            'temperatures': temperatures,
            'hours': hours
            }
        return jsonify(message)


if __name__ == '__main__':
  app.run(debug=True)