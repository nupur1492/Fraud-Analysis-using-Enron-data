#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

#features_train = features_train[:len(features_train)/100]
#labels_train = labels_train[:len(labels_train)/100]

clf = SVC(kernel="rbf", C=10000.0)

t0 = time()
clf.fit(features_train,labels_train)
print("training time: ", time()-t0,3)

t1 = time()
pred = clf.predict(features_test)
print("Prediction time: ", time()-t1,3)

print("Accuracy: ",accuracy_score(labels_test,pred))
#print(pred[10])
#print(pred[26])
#print(pred[50])

count = 0
i=0
for i in range(0,len(pred),1):
    if pred[i]==1:
        count += 1

print(count)
#########################################################


