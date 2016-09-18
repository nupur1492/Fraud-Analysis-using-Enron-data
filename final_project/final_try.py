#!/usr/bin/python

import sys
import pickle
from sklearn import cross_validation
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, recall_score, precision_score

sys.path.append("../tools/")

from feature_format import featureFormat, targetFeatureSplit
from tester import dump_classifier_and_data

### Task 1: Select what features you'll use.
### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".
features_list = ['poi','salary','deferral_payments', 'total_payments', 'loan_advances', 'bonus',
                 'restricted_stock_deferred', 'deferred_income', 'total_stock_value', 'expenses',
                 'exercised_stock_options', 'other', 'long_term_incentive', 'restricted_stock', 'director_fees']


# You will need to use more features

### Load the dictionary containing the dataset
with open("final_project_dataset.pkl", "r") as data_file:
    data_dict = pickle.load(data_file)

data = featureFormat(data_dict, features_list)
print(type(data))

labels, features = targetFeatureSplit(data)

features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(features, labels,
                                                                                             test_size=0.3,
                                                                                              random_state= 42)

print(features_train[1])
plt.scatter(features_train[1],features_train[2])
#plt.show()
### Task 2: Remove outliers


### Task 3: Create new feature(s)
### Store to my_dataset for easy export below.


# ML
#gaussian NB
from sklearn.naive_bayes import GaussianNB
clf_gaussian = GaussianNB()

clf_gaussian.fit(features_train,labels_train)

pred_gaussian = clf_gaussian.predict(features_test)

print('Gaussian Niave Bayes')
print('Accuracy Score:  ', accuracy_score(labels_test, pred_gaussian))
print('Recall: ', recall_score(labels_test, pred_gaussian))
print('Precision: ', precision_score(labels_test, pred_gaussian))






