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
##########################################################################################
dataset = pd.read_csv('./Python/Data/Sura/Data_Sura_test.csv', delimiter=";", decimal='.')
dataset.columns = ["år", 
                   "månad", 
                   "dag", 
                   "timme", 
                   "temp",
                   "effekt",
                   "vindhastighet"]
dataset.head()
##########################################################################################
print('The shape of our features is:', dataset.shape)
#The shape of our features is: (9704, 8)
dataset.describe()
##########################################################################################
# Labels are the values we want to predict
labels = np.array(dataset['effekt'])
# Remove the labels from the features
# axis 1 refers to the columns
dataset= dataset.drop('effekt', axis = 1)
# Saving feature names for later use
dataset_list = list(dataset.columns)
# Convert to numpy array
dataset = np.array(dataset)
##########################################################################################
# Split the data into training and testing sets
train_features, test_features, train_labels, test_labels = train_test_split(dataset, labels, test_size = 0.25, random_state = 42)
##########################################################################################
print('Training Features Shape:', train_features.shape)
print('Training Labels Shape:', train_labels.shape)
print('Testing Features Shape:', test_features.shape)
print('Testing Labels Shape:', test_labels.shape)
##########################################################################################
# The baseline predictions are the historical averages
baseline_preds = test_features[:, dataset_list.index('temp')]
# Baseline errors, and display average baseline error
baseline_errors = abs(baseline_preds - test_labels)
print('Average baseline error: ', round(np.mean(baseline_errors), 2))
##########################################################################################
# Instantiate model with 1000 decision trees
rf = RandomForestRegressor(n_estimators = 2000, random_state = 42)
# Train the model on training data
rf.fit(train_features, train_labels)
##########################################################################################
# Use the forest's predict method on the test data
predictions = rf.predict(test_features)
# Calculate the absolute errors
errors = abs(predictions - test_labels)
# Print out the mean absolute error (mae)
print('Mean Absolute Error:', round(np.mean(errors), 2))
predictions
##########################################################################################
# Use datetime for creating date objects for plotting
import datetime
# Dates of training values
months = dataset[:, dataset_list.index('månad')]
days = dataset[:, dataset_list.index('dag')]
years = dataset[:, dataset_list.index('år')]
hours = dataset[:, dataset_list.index('timme')]
# List and then convert to datetime object
dates = [str(int(year)) + '-' + str(int(month)) + '-' + str(int(day)) + ' ' + str(int(hour)) for year, month, day, hour in zip(years, months, days, hours)]
dates = [datetime.datetime.strptime(date, '%Y-%m-%d %H') for date in dates]
# Dataframe with true values and dates
true_data = pd.DataFrame(data = {'date': dates, 'actual': labels})
# Dates of predictions
months = test_features[:, dataset_list.index('månad')]
days = test_features[:, dataset_list.index('dag')]
years = test_features[:, dataset_list.index('år')]
hours = dataset[:, dataset_list.index('timme')]
# Column of dates
test_dates = [str(int(year)) + '-' + str(int(month)) + '-' + str(int(day))+ ' ' + str(int(hour)) for year, month, day, hour in zip(years, months, days, hours)]
# Convert to datetime objects
test_dates = [datetime.datetime.strptime(date, '%Y-%m-%d %H') for date in test_dates]
# Dataframe with predictions and dates
predictions_data = pd.DataFrame(data = {'date': test_dates, 'prediction': predictions})
# Plot the actual values
plt.plot(true_data['date'], true_data['actual'], 'b-', label = 'actual')
# Plot the predicted values
plt.plot(predictions_data['date'], predictions_data['prediction'], 'ro', label = 'prediction')
plt.xticks(rotation = '60'); 
plt.legend()
# Graph labels
plt.xlabel('Date'); plt.ylabel('effekt'); plt.title('Actual and Predicted Values');
##########################################################################################
#print(predictions_data)
#print(true_data)
preds = []

predictions_data.sort_values(by='date', inplace=True)
for i, true in true_data.iterrows():
  if (i%100==0):
    print("{0:.0%}".format(i / len(true_data)))
  for j, pred in predictions_data.iterrows():
    if (true['date'] == pred['date']):
      preds.append([true['actual'], pred['prediction']])
      continue
print(preds)
##########################################################################################
ef = []
pr_ef = []
for p in preds:
  ef.append(p[0])
  pr_ef.append(p[1])
##########################################################################################
df = pd.DataFrame()
df['Effekt'] = ef
df['Förutspådd effekt'] = pr_ef
error_margin = 3
df['Correct'] = [1 if corr-pred <= error_margin and corr-pred >= -error_margin else 0 for corr, pred in zip(df['Effekt'], df['Förutspådd effekt'])]
##########################################################################################
df['Correct'].sum() / len(df)
print("{0:.0%} med marginal på +-{err} mega watt.".format(df['Correct'].sum() / len(df), err = error_margin))