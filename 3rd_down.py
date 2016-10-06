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

# Summary of dataset's value.
#print dataset.describe()

# Getting all third down plays of the season. (9088 occurences)
third_down_plays = dataset[dataset.down == 3]

# Long third down situation. (3198 occurences = 35%)
long_situations = third_down_plays[third_down_plays.ydstogo >= 8]

# Situations where teams got the 1st Down on those complicated situations. (765 occurences = 23%) <- Not a good place for an offense to be!
long_first_downs = long_situations[long_situations.FirstDown == 1]

# Conversions through the running game. (54 occurences = 7%)
run_conversions = long_first_downs[long_first_downs.PlayType == 'Run']

# Conversions through the passing game. (591 occurences = 77%)
pass_conversions = long_first_downs[long_first_downs.PlayType == 'Pass']

# Conversions using screen passes (2 occurences = 0.2%) <- Terrible option!
screen_pass_one = long_first_downs[long_first_downs.desc.str.contains('Screen')]
screen_pass_two = long_first_downs[long_first_downs.desc.str.contains('screen')]
#screen_pass = screen_pass_one + screen_pass_two

print len(screen_pass_one) + len(screen_pass_two)
#print screen_pass_one
#print screen_pass.describe()


