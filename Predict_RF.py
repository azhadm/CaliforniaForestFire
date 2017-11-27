import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
import pickle

from sklearn.externals import joblib
import os
# import cPickle as pickle
import csv

sensor_data = pd.read_csv('CA_Forest_Dataset_Final.csv')
X = sensor_data.values[:, 0:6]
Y = sensor_data.values[:,6]

print(X)
print(Y)

X_train, X_test, y_train, y_test = train_test_split( X, Y, test_size = 0.3, random_state = 100)

clf = RandomForestClassifier()
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
y_pred

print("Accuracy for Random Forest Classifier is ", accuracy_score(y_test,y_pred)*100)

result1 = clf.predict([[39.1,-121.6,18.9,4.92,0,63],[37.6,-121.0,22.3,6.93,0,72]])
print('The predicted result using RF for sensor data record [39.5,-121.6,57.9,6.71,69 --> N]  is: ')
print(result1)

result2 = clf.predict([[41.3,-122.3,1077.5,0.67,0,60],[41.3,-122.3,1077.5,2.24,0,64]])
print('The predicted result using RF for sensor data record [39.5,-121.6,57.9,2.46,73 ----> Y] is: ')
print(result2)

filename = 'model_RF.sav'
pickle.dump(clf, open(filename, 'wb'))