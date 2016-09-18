#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import pandas as pd
enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print(len(enron_data))
print(enron_data['SKILLING JEFFREY K'])

data = enron_data
df_enron = pd.DataFrame(data=data)

#res = [(x, my_dictionary[x]) for x in my_list]
person_name = enron_data.keys()

print(len(person_name))

if enron_data["SKILLING JEFFREY K"]["poi"] == True:
    print("khaklj")

count = 0
for name in person_name:
    if enron_data[name]["poi"] == True:
        count += 1
        ##if enron_data[name]["total_payments"] == "NaN":
           #and enron_data[name]["total_payments"] == "NaN":
            #count += 1

print("POI ",count)


count1 = 0
for name in person_name:
    if enron_data[name]["salary"] != "NaN":
        count1 += 1

print("salary: ",count1)

count2 = 0
for name in person_name:
    if enron_data[name]["email_address"] != "NaN":
        count2 += 1

print("emailids: ",count2)

count3 = 0
for name in person_name:
    if enron_data[name]["total_payments"] == "NaN":
        count3 += 1

print("tottal payments: ",count3)

print(enron_data["SKILLING JEFFREY K"]["poi"])

print(enron_data["PRENTICE JAMES"]["total_stock_value"])

print(enron_data["COLWELL WESLEY"]["from_this_person_to_poi"])

print(df_enron['SKILLING JEFFREY K']["total_payments"])
print(df_enron['LAY KENNETH L']["total_payments"])
print(df_enron['FASTOW ANDREW S']["total_payments"])