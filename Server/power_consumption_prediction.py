print("Importing stuff...")
from tokenize import String
# import stuff
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import metrics
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.axis import Axis

import pickle

import requests
from datetime import datetime

dir = './Python/Data/Sura/Data_Sura_test.csv'

def open_file(path):
    if (type(path) != str): return False
    dataset = pd.read_csv(path, delimiter=";", decimal='.')
    dataset.columns = ["år", 
                    "månad", 
                    "dag", 
                    "timme", 
                    "temp",
                    "effekt",
                    "vindhastighet"]
    return dataset

def format_data(dataset):
    # Labels are the values we want to predict
    labels = np.array(dataset['effekt'])
    # Remove the labels from the features
    # axis 1 refers to the columns
    dataset= dataset.drop('effekt', axis = 1)
    # Saving feature names for later use
    dataset_list = list(dataset.columns)
    # Convert to numpy array
    dataset = np.array(dataset)
    return dataset, dataset_list, labels

def train_model(train_features, train_labels):
    # Instantiate model with 1000 decision trees
    rf = RandomForestRegressor(n_estimators = 2000, random_state = 42)
    # Train the model on training data
    rf.fit(train_features, train_labels)
    return rf

def save_model(rf):
    pickle_out = open('weights.pickle','wb')
    pickle.dump(rf, pickle_out)
    pickle_out.close()

def load_model():
    pickle_in = open('weights.pickle','rb')
    rf = pickle.load(pickle_in)
    return rf

def calc_probability():
    pass

def test_model(rf, test_features, test_labels = None):
    # Use the forest's predict method on the test data
    predictions = rf.predict(test_features)
    # Calculate the absolute errors
    #errors = abs(predictions - test_labels)
    # Print out the mean absolute error (mae)
    #print('Mean Absolute Error:', round(np.mean(errors), 2))
    return predictions

def get_temp(date):
    date, hour = date.split(' ')
    #print(date, time)
    # Ifall användaren inte matat in ett korrekt datum tas bara dagens datum
    if len(date) != 10:
        print("ERR: Incorrect input format. Using today's date.")
        date = datetime.today().strftime('%Y-%m-%d')

    r = requests.get(
        'https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/16.6001/lat/59.5972/data.json')

    
    # Rå data från SMHI:s API
    weatherData = r.json()
    # Antalet träffar på inmatade datumet
    availableHours = 0
    temp = []
    windSpeed = []
    # Lägger till temperatur och vindhastighet för alla timmar för det angivna datumet i två listor
    for item in weatherData["timeSeries"]:
        if (item["validTime"][0:10] == date):
            for row in item["parameters"]:
                if row["name"] == 't':
                    temp.append(row["values"][0])
                elif row["name"] == 'ws':
                    windSpeed.append(row["values"][0])
            availableHours += 1
    if (len(temp) <= 0):
        return False
    if (availableHours == 24):
        t = temp[int(hour)-1]
        w = windSpeed[int(hour)-1]
    else:
        t = sum(temp) / len(temp)
        w = sum(windSpeed) / len(windSpeed)

    return t, w

def run_prediction(pred_val):
    print("Load model...")
    rf = load_model()
    print("Testing model...")
    res = test_model(rf, pred_val)
    return res

def run_program(date):
    t, w = get_temp(date)
    date, hour = date.split(' ')
    year, month, day = date.split('-')
    pred_values = [[year, month, day, hour, t, w]]
    p = run_prediction(pred_values)
    return p
#test_value = [[2017.0, 12.0, 28.0, 4.0, 2.74, 2.3]] # 2.74, 2.3
#run_prediction(test_value)

#date = input('Name a date (YYYY-MM-DD TT). Note that a few dates ahead of time provide less amount of hours predicted.\n >>> ')
# get_temp(date)
#print(run_program(date))


#print("Loading data...")
#dataset = open_file(dir)
#print("Formatting data...")
#dataset, data_list, labels = format_data(dataset)
#print("Labeling data...")
#train_features, test_features, train_labels, test_labels = train_test_split(dataset, labels, test_size = 0.25, random_state = 42)
#print(test_labels)
#print("Training model...")
#rf = train_model(test_features, test_labels)
#print("Saving Model...")
#save_model(rf)