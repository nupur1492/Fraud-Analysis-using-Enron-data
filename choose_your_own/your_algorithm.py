#!/usr/bin/python

#import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
#from class_vis import prettyPicture
from sklearn import neighbors
from sklearn.metrics import accuracy_score
from sklearn.ensemble import AdaBoostClassifier
from sklearn.svm import SVC
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
# plt.xlim(0.0, 1.0)
# plt.ylim(0.0, 1.0)
# plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
# plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
# plt.legend()
# plt.xlabel("bumpiness")
# plt.ylabel("grade")
# plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary

# K-nearest neighbors

n_neighbors = 20
#fit
clf_knn = neighbors.KNeighborsClassifier(n_neighbors=n_neighbors)
clf_knn.fit(features_train, labels_train)

#predict
pred_knn = clf_knn.predict(features_test)

#accuracy:
print("KNN Accuracy: ",accuracy_score(labels_test,pred_knn))

#accuracy - 10: 93.2
# 15: 92.8
#20: 93.6

# Adaboost
#clf_ada = AdaBoostClassifier(base_estimator=SVC(kernel="linear", C=1000), algorithm="SAMME", n_estimators=500)
clf_ada = AdaBoostClassifier(base_estimator=tree.DecisionTreeClassifier(min_samples_split=40))

clf_ada.fit(features_train,labels_train)

pred_ada = clf_ada.predict(features_test)

print("Adaboost Accuracy: ", accuracy_score(labels_test,pred_ada))

# initial- Decision trees: 92.4
# SVM rbf: 66.4
# SVM linear, c = 1000: 91.2

# Random Forests
clf_rf = RandomForestClassifier(n_estimators=50, max_depth=5)

clf_rf.fit(features_train,labels_train)

pred_rf = clf_rf.predict(features_test)

print("Randon Forests Accuracy: ", accuracy_score(labels_test,pred_rf))

# accuracy: 92, estimators: 500
# accuracy: 91.2, estimators: 50
# accuracy: 92.8, estimators: 50, depth = 5


# try:
#     prettyPicture(clf, features_test, labels_test)
# except NameError:
#     pass
