# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EQN6WCj-bhyfu1KXUPnMv8zzf-_LCkv4

Import required libraries
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,classification_report

"""reading data"""

url="https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
file=pd.read_csv(url)
file.head()

"""CLEANING THE DATA"""

file.fillna(0,inplace=True) #replacing NaN with 0
file=pd.get_dummies(file,columns=['Sex','Embarked'],drop_first=True) #treating categorical values

"""declaring feature matrix and target variable"""

X=file.drop(['Survived','Name','Ticket','Cabin'],axis=1) #feature matrix ,
Y=file['Survived'] #target variable

"""splitting the data for training and testing"""

X_test,X_train,Y_test,Y_train=train_test_split(X,Y,test_size=0.25,random_state=100)

"""Creating model with RandomForestClassifier"""

model=RandomForestClassifier(n_estimators=200,max_depth=19,min_samples_split=5,random_state=100)
model.fit(X_train,Y_train) #training model

"""predictions using built model"""

predictions = model.predict(X_test)

"""checking accuracy of model"""

score = accuracy_score(Y_test, predictions)
print(f"Accuracy: {score}")