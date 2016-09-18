#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
from sklearn import cross_validation
from sklearn import tree
from sklearn.metrics import accuracy_score, precision_score, recall_score

sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)


features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(features,labels,
                                                                                             test_size=0.3,
                                                                                             random_state= 42)
print(len(labels_test))
### it's all yours from here forward!

clf = tree.DecisionTreeClassifier()

clf.fit(features_train, labels_train)

pred = clf.predict(features_test)

print("accuracy: ", accuracy_score(pred, labels_test))

print(pred)
print(labels_test)

print("Precision:   ", precision_score(labels_test,pred))
print("Recall:   ", recall_score(labels_test,pred))


### your code goes here 


