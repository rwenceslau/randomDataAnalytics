import numpy as np # linear algebra
import pandas as pd
# Random Forests are good here because very small amount of data
from sklearn.ensemble import RandomForestClassifier 
from sklearn.cross_validation import train_test_split # split data
from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_auc_score
import operator

#--- SETUP ---#
pd.set_option('display.max_columns', None)
#-------------#

# Reading Kaggle's NFL Play-by-Play Season 2015 dataset.
dataset = pd.read_csv("data/nflplaybyplay2015.csv", low_memory=False)
dataset = dataset.fillna(method='ffill')
#print dataset.columns.values
validPlays = ['Pass', 'Run', 'Sack', 'Field Goal', 'Punt']
potentialPlays = dataset[dataset.PlayType.isin(validPlays)]
#print potentialPlays.corr()

predFeatures = potentialPlays[['qtr', 'down', 'TimeUnder','ydstogo', 'PassAttempt', 'RushAttempt',
							 'Reception', 'Sack', 'PosTeamScore', 'DefTeamScore', 'ScoreDiff', 'AbsScoreDiff', 'Fumble']]


# Splitting 
X, test = train_test_split(predFeatures, test_size = 0.5)

y = X.pop('Fumble')
test_y = test.pop('Fumble')


#print np.isnan(predFeatures).any()
#predFeatures[np.isnan(predFeatures.down)] = np.median(predFeatures[~np.isnan(predFeatures)])

clf = RandomForestClassifier(n_estimators=800)
clf.fit(X,y)
fumble_prediction = clf.predict(test)
print f1_score(test_y, fumble_prediction)

#print clf.decision_path(X)
print clf.score(test,test_y)
print roc_auc_score(test_y, fumble_prediction)
print confusion_matrix(test_y, fumble_prediction)

#print y
#print test_y


list_of_features = {}
for feature, importance in enumerate(zip(clf.feature_importances_, X.columns)):
	#print feature, importance
	list_of_features[feature] = importance

sorted_by_importance = sorted(list_of_features.items(), key=operator.itemgetter(1), reverse = True)

for feature in sorted_by_importance:
	print feature 
#print len(ne_brady_completed)

# print ne_passPlays.corr()
# print len(ne_passPlays)
# model = ne_validPlays[['down', 'ydstogo', 'TimeSecs', 'PosTeamScore', 'DefTeamScore', 'yrdline100']]
# target = ne_validPlays['yrdline100']

# X, test = train_test_split(model, test_size = 0.2)
# Y = X.pop('yrdline100')
# test_y = test.pop('yrdline100')

# clf = RandomForestClassifier(n_estimators=1000)
# clf.fit(X,Y)

# print clf.score(test,test_y)
# x = clf.feature_importances_
# y = X.columns

# print x
# print y 
