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
 
from os.path import exists

dir = './Data_Sura_test.csv'

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

def get_temp(date, hour = None):
    # date, hour = date.split(' ')
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
    aHours = []
    temp = []
    windSpeed = []
    # Lägger till temperatur och vindhastighet för alla timmar för det angivna datumet i två listor
    for item in weatherData["timeSeries"]:
        if (item["validTime"][0:10] == date):
            aHours.append(item["validTime"][11:13])
            for row in item["parameters"]:
                # print(row)
                if row["name"] == 't':
                    temp.append(row["values"][0])
                elif row["name"] == 'ws':
                    windSpeed.append(row["values"][0])
            availableHours += 1
    if (hour == None):
        return temp, aHours
    if (len(temp) <= 0):
        return False
    if (availableHours == 24):
        t = temp[int(hour)-1]
        w = windSpeed[int(hour)-1]
        return t, w
    else:
        t = sum(temp) / len(temp)
        w = sum(windSpeed) / len(windSpeed)
        return t, w

def run_prediction(pred_val, rf):
    print("Predicting...")
    res = test_model(rf, pred_val)
    return res

def run_program(date = None, hour = None, temp = None):
    if exists("weights.pickle"):
        print("Load model...")
        rf = load_model()
    else:
        train_and_save_model()
        rf = load_model()
    # Om temp anges använd den annars hämta den.
    if temp != None:
        t = float(temp)
        w = 0
    else:
        if (hour != None): 
            t, w = get_temp(date, hour)
        else:
            t, h = get_temp(date)
            w = [0]*len(t)
    year, month, day = date.split('-')
    if isinstance(t, list):
        pred_values = []
        for i, t_v in enumerate(t):
            pred_values.append(run_prediction([[year, month, day, h[i], t_v, w[i]]], rf)[0])
        return pred_values, t, h
    else:
        pred_values = [[year, month, day, hour, t, w]]
        p = run_prediction(pred_values, rf)
    return p

def train_and_save_model():
    print("Loading data...")
    dataset = open_file(dir)
    print("Formatting data...")
    dataset, data_list, labels = format_data(dataset)
    print("Labeling data...")
    train_features, test_features, train_labels, test_labels = train_test_split(dataset, labels, test_size = 0.25, random_state = 42)
    print(test_labels)
    print("Training model...")
    rf = train_model(test_features, test_labels)
    print("Saving Model...")
    save_model(rf)

# print(run_program("2022-05-04"))


