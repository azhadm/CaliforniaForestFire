import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score
import pickle

sensor_data = pd.read_csv('CA_Forest_Dataset_Final.csv')
X = sensor_data.values[:, 0:6]
Y = sensor_data.values[:,6]

X_train, X_test, y_train, y_test = train_test_split( X, Y, test_size = 0.3, random_state = 100)

clf_svm = svm.SVC()
clf_svm.fit(X_train, y_train)

y_pred = clf_svm.predict(X_test)

print("Accuracy for SVM is ", accuracy_score(y_test, y_pred)*100)

result1 = clf_svm.predict([[39.1,-121.6,18.9,4.92,0,63],[37.6,-121.0,22.3,6.93,0,72]])
print('The predicted result using SVM for sensor data record [39.1,-121.6,18.9,4.92,0,63 --> N]  is: ')
print(result1)

result2 = clf_svm.predict([[41.3,-122.3,1077.5,0.67,0,60],[41.3,-122.3,1077.5,2.24,0,64]])
print('The predicted result using SVM for sensor data record [41.3,-122.3,1077.5,0.67,0,60 ----> Y] is: ')
print(result2)

filename = 'model_SVM.sav'
pickle.dump(clf_svm, open(filename, 'wb'))