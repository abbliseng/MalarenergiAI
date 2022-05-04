import imp
from flask import Flask, render_template, request, redirect, jsonify
from jinja2 import Undefined
from power_consumption_prediction import run_program
from graph import drawGraph

import subprocess
import webbrowser
import os

UPLOAD_FOLDER = 'static/uploads/'

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

alt = False

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

# If only date: Get all avalible hours and plot on graph
@app.route('/predict/<date>', methods=['GET'])
def testfn4(date):
    # GET request
    if request.method == 'GET':
        prediction_value, temperatures, hours = run_program(date=date)
        img_path = drawGraph(date, prediction_value, hours)
        print(img_path)
        message = {
            'status': 200,
            'date': date,
            'prediction_value':prediction_value,
            'temperatures': temperatures,
            'hours': hours,
            'img_path': img_path
            }
        return jsonify(message)

def run():
    app.run(debug=True)

if __name__ == '__main__':
    # filename = 'file:///'+os.getcwd()+'/' + 'GFG.html'*
    # # url = os.path.abspath("./templates/index.html")
    # url = "http://localhost:5000"
    # # or a file on your computer
    # # url = "/Users/yourusername/Desktop/index.html
    # try: # should work on Windows
    #     os.startfile(url)
    # except AttributeError:
    #     try: # should work on MacOS and most linux versions
    #         subprocess.call(['open', url])
    #     except:
    #         print('Could not open URL')
    app.run(debug=True)