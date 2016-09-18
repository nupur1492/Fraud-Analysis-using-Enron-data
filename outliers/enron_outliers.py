#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot as plt
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
print(data_dict)
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)


### your code below
print(type(data))
data.sort(axis = 0)
for point in data:
    salary = point[0]
    bonus = point[1]
    #print(bonus, salary)
    plt.scatter(salary, bonus)


print(data)
plt.xlabel("Salary")
plt.ylabel("Bonus")
plt.show()


