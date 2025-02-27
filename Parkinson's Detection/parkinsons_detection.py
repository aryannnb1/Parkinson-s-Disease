# -*- coding: utf-8 -*-
"""parkinsons_detection.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13abKU7UqVyuGD2um11XWtRbJSE9x-Vp5

Importing dependencies
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import svm
from sklearn.metrics import accuracy_score
import pickle

# Converting csv file to Pandas DataFrame
parkinsons_data = pd.read_csv(r'/content/parkinsons.csv')

# Printing the first five rows of the DataFrame
parkinsons_data.head()

#number of rows and columns in the dataset
parkinsons_data.shape

"""Getting more information about the data set"""

parkinsons_data.info()

# checking missing values in each column
parkinsons_data.isnull().sum()

# getting some statistical measures about the data
parkinsons_data.describe()

# distribution of target variable
parkinsons_data['status'].value_counts()

"""1 ---> Parkinson's positive

0 ---> Healthy
"""

# grouping the data based on the target column
numeric_df = parkinsons_data.select_dtypes(include=[np.number])
numeric_df['status'] = parkinsons_data['status']
numeric_df.groupby('status').mean()

"""Data pre-processing"""

# separating the features and target
X = parkinsons_data.drop(columns = ['name', 'status'], axis = 1)
Y = parkinsons_data['status']

print(X)

print(Y)

"""Splitting the data to training data and test data"""

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 2)

print(X.shape, X_train.shape, X_test.shape)

scaler = StandardScaler()

scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

print(X_train)

model = svm.SVC(kernel = 'linear')

model.fit(X_train, Y_train)

X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(Y_train, X_train_prediction)

print('Accuracy score of training data: ', training_data_accuracy)

X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(Y_test, X_test_prediction)

print('Accuracy score of testing data: ', test_data_accuracy)

input_data = (197.07600,206.89600,192.05500,0.00289,0.00001,0.00166,0.00168,0.00498,0.01098,0.09700,0.00563,0.00680,0.00802,0.01689,0.00339,26.77500,0.422229,0.741367,-7.348300,0.177551,1.743867,0.085569)
input_array = np.asarray(input_data)
input_reshaped = input_array.reshape(1, -1)
std_data = scaler.transform(input_reshaped)
prediction = model.predict(std_data)
print(prediction)

if prediction[0] == 0:
  print('The person does not have Parkinson\'s Disease')
else:
  print('The person has Parkinson\'s Disease')

with open('trained_model.pkl', 'wb') as file:
    pickle.dump(model, file)

"""Saving trained model"""

print("Model saved as 'trained_model.pkl'")
