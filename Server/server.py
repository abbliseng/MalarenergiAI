import imp
from flask import Flask, render_template, request, redirect, jsonify
from power_consumption_prediction import run_program
app = Flask(__name__)

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

@app.route('/test/<date>/<hour>', methods=['GET'])
def testfn(date, hour):
    # GET request
    print(date, hour)
    if request.method == 'GET':
        message = {'prediction_value':str(run_program(date+' '+hour)[0])}
        return jsonify(message)  # serialize and use JSON headers
    # POST request
    #if request.method == 'POST':
    #    print(request.get_json())  # parse as JSON
    #    return 'Sucesss', 200

if __name__ == '__main__':
  app.run(debug=True)