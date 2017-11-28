import numpy as np
import pandas as pd
from sklearn import cross_validation,tree
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, f1_score
import pickle

sensor_data = pd.read_csv('CA_Forest_Dataset_Final.csv')
X = sensor_data.values[:, 0:6]
Y = sensor_data.values[:,6]

X_train, X_test, y_train, y_test = train_test_split( X, Y, test_size = 0.3, random_state = 100)

clf_gini = DecisionTreeClassifier(criterion = "gini")
clf_gini.fit(X_train, y_train)

clf_entropy = DecisionTreeClassifier(criterion = "entropy")
clf_entropy.fit(X_train, y_train)

y_pred = clf_gini.predict(X_test)

y_pred_en = clf_entropy.predict(X_test)

kf_total = cross_validation.KFold(len(X), n_folds=10, shuffle=True, random_state=4)
print("Cross validation accuracy is ", np.mean(cross_validation.cross_val_score(clf_gini, X, Y, cv=kf_total, n_jobs = 1)))

print("Accuracy for DT with gini index is ", accuracy_score(y_test,y_pred)*100)
print("F-score ", f1_score(y_test, y_pred, average='micro'))

print("Accuracy for DT with information gain is ", accuracy_score(y_test,y_pred_en)*100)
print("F-score ", f1_score(y_test, y_pred_en, average='micro'))

result1 = clf_gini.predict([[33.6,-116.2,-36,6.04,0.1,99], [33.3,-117.3,22.9,9.84,1.25,59],
                       [34.2,-118.5,234.7,10.51,6.51,52], [38.5,-121.5,4.6,2.24,0,61]])
print('N : The predicted result using DT for Case 1, Case 2, Case 3 and Case 4  is ', result1)

result2 = clf_gini.predict([[34.8,-114.6,271.3,6.04,0.1,115], [40.5,-122.3,151.5,9.84,0.94,58],
                       [40.5,-120.3,2545.7,1.12,1.6,72], [33.6,-116.2,-36,9.62,0,89]])
print('Y : The predicted result using DT for Case 5, Case 6, Case 7 and Case 8 is ', result2)

filename = 'model_DT.sav'
pickle.dump(clf_gini, open(filename, 'wb'))
