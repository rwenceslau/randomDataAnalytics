import numpy as np # linear algebra
import pandas as pd
# Random Forests are good here because very small amount of data
from sklearn.ensemble import RandomForestClassifier 
from sklearn.cross_validation import train_test_split # split data
import seaborn as sns; # plotting

#--- SETUP ---#
pd.set_option('display.max_columns', None)
#-------------#

# Reading Kaggle's NFL Play-by-Play Season 2015 dataset.
dataset = pd.read_csv("data/nflplaybyplay2015.csv", low_memory=False)

# Filtering by team
ne_plays = dataset[dataset.posteam == 'NE']
#print ne_plays.corr()

# Filtering by play type.
ne_pass_plays = ne_plays[ne_plays.PlayType == 'Pass']

# Filtering by completed passes.
ne_completed_passes = ne_pass_plays[ne_pass_plays.PassOutcome == 'Complete']

# Only Brady's completions.
ne_brady_completed = ne_completed_passes[ne_completed_passes.Passer == 'T.Brady']
total_completed = len(ne_brady_completed)

# Where those completions happened.
completed_area = ne_brady_completed['yrdline100']
#print completed_area

# Splits the field into 4 different zones (5 including the opponent Endzone)
danger_zone = []
neutral_zone_back = []
neutral_zone_front = []
red_zone = []

# I could just count it, but it's interesting to know exactly where that completion occurred.
for entry in completed_area:
	if entry < 25.0:
		danger_zone.append(entry)
	if entry >= 25.0 and entry <= 50.0:
		neutral_zone_back.append(entry)
	if entry > 50.0 and entry <= 75.0:
		neutral_zone_front.append(entry)
	if entry > 75.0 and entry < 100.0:
		red_zone.append(entry)

# Print the results.
print 'OWN 1 - OWN 25: {} -- ({})'.format(len(danger_zone), len(danger_zone) / float(total_completed))
print 'OWN 26 - 50: {} -- ({})'.format(len(neutral_zone_back), len(neutral_zone_back) / float(total_completed))
print 'OPP 49 - OPP 25: -- {} ({})'.format(len(neutral_zone_front), len(neutral_zone_front) / float(total_completed))
print 'OPP 24 - OPP 1: {} -- ({})'.format(len(red_zone), len(red_zone) / float(total_completed))
brady_tds = ne_completed_passes[ne_completed_passes.Touchdown == 1]

# Getting rid of TDs reversed by replay challenges
final_td_count = brady_tds[brady_tds.ChalReplayResult != 'Reversed']

print 'OPP ENDZONE {} -- ({})'.format(len(final_td_count), len(final_td_count) / float(total_completed))

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
