# https://stackabuse.com/time-series-prediction-using-lstm-with-pytorch-in-python/
import torch
import torch.nn as nn

import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# load in the flights dataset from seaborn
flight_data = sns.load_dataset("flights")
flight_data.head()

# increases the default plot size
fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 15
fig_size[1] = 5
plt.rcParams["figure.figsize"] = fig_size
# plots the monthly frequency of the number of passengers
plt.title('Month vs Passenger')
plt.ylabel('Total Passengers')
plt.xlabel('Months')
plt.grid(True)
plt.autoscale(axis='x',tight=True)
plt.plot(flight_data['passengers'])
# show the plot
# plt.show()

# Data Preprocessing
# first preprocessing step is to change the type of the passengers column to float
all_data = flight_data['passengers'].values.astype(float)
#print(all_data)
# divide our data set into training and test sets
test_data_size = 12

train_data = all_data[:-test_data_size]
test_data = all_data[-test_data_size:]
# normalizes our data using the min/max scaler with minimum and maximum values of -1 and 1, respectively
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler(feature_range=(-1, 1))
train_data_normalized = scaler.fit_transform(train_data .reshape(-1, 1))
# important to mention here that data normalization is only applied on the training data and not on the test data
#print(train_data_normalized[:5])
#print(train_data_normalized[-5:])

# convert our dataset into tensors since PyTorch models are trained using tensors
train_data_normalized = torch.FloatTensor(train_data_normalized).view(-1)
# convert our training data into sequences and corresponding labels
train_window = 12
# accept the raw input data and will return a list of tuples
def create_inout_sequences(input_data, tw):
    inout_seq = []
    L = len(input_data)
    for i in range(L-tw):
        train_seq = input_data[i:i+tw]
        train_label = input_data[i+tw:i+tw+1]
        inout_seq.append((train_seq ,train_label))
    return inout_seq
# create sequences and corresponding labels for training
train_inout_seq = create_inout_sequences(train_data_normalized, train_window)

# Creating LSTM Model
class LSTM(nn.Module):
    def __init__(self, input_size=1, hidden_layer_size=100, output_size=1):
        super().__init__()
        self.hidden_layer_size = hidden_layer_size

        self.lstm = nn.LSTM(input_size, hidden_layer_size)

        self.linear = nn.Linear(hidden_layer_size, output_size)

        self.hidden_cell = (torch.zeros(1,1,self.hidden_layer_size),
                            torch.zeros(1,1,self.hidden_layer_size))

    def forward(self, input_seq):
        lstm_out, self.hidden_cell = self.lstm(input_seq.view(len(input_seq) ,1, -1), self.hidden_cell)
        predictions = self.linear(lstm_out.view(len(input_seq), -1))
        return predictions[-1]
# create an object of the LSTM() class, define a loss function and the optimizer
model = LSTM()
loss_function = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
#print(model)

# Training the Model
epochs = 150

for i in range(epochs):
    for seq, labels in train_inout_seq:
        optimizer.zero_grad()
        model.hidden_cell = (torch.zeros(1, 1, model.hidden_layer_size),
                        torch.zeros(1, 1, model.hidden_layer_size))

        y_pred = model(seq)

        single_loss = loss_function(y_pred, labels)
        single_loss.backward()
        optimizer.step()

    if i%25 == 1:
        print(f'epoch: {i:3} loss: {single_loss.item():10.8f}')

print(f'epoch: {i:3} loss: {single_loss.item():10.10f}')

# Making Predictions
fut_pred = 12

test_inputs = train_data_normalized[-train_window:].tolist()

model.eval()

for i in range(fut_pred):
    seq = torch.FloatTensor(test_inputs[-train_window:])
    with torch.no_grad():
        model.hidden = (torch.zeros(1, 1, model.hidden_layer_size),
                        torch.zeros(1, 1, model.hidden_layer_size))
        test_inputs.append(model(seq).item())

# Since we normalized the dataset for training, the predicted values are also normalized.
# We need to convert the normalized predicted values into actual predicted values
actual_predictions = scaler.inverse_transform(np.array(test_inputs[train_window:] ).reshape(-1, 1))
#print(actual_predictions)
#  plot the predicted values against the actual values
x = np.arange(132, 144, 1)

plt.title('Month vs Passenger')
plt.ylabel('Total Passengers')
plt.grid(True)
plt.autoscale(axis='x', tight=True)
plt.plot(flight_data['passengers'])
plt.plot(x,actual_predictions)
plt.show()