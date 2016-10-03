# randomDataAnalytics
Just a compilation of algorithms creating random analysis around some interesting topics

# > bradyCompletions.py < #

Where in the field did T.Brady completed most of his passes during NFL's 2015 season?

OUTPUT:

OWN 1 - OWN 25: 70 -- (0.174129353234)
OWN 26 - 50: 106 -- (0.26368159204)
OPP 49 - OPP 25: -- 148 (0.36815920398)
OPP 24 - OPP 1: 78 -- (0.194029850746)
OPP ENDZONE 36 -- (0.089552238806)

Analysis: Brady completed most of his passes when the Patriots just crossed opponent's part of the field (and just before that,
still in Patriots' territory).

# > fumbles.py < #

What are the main causes for fumbling the ball in NFL's 2015 season?

OUTPUT

(2, (0.28149031326362722, 'TimeUnder'))
(3, (0.19283615938645762, 'ydstogo'))
(7, (0.15778346595471715, 'ScoreDiff'))
(8, (0.13079694923023943, 'AbsScoreDiff'))
(0, (0.10096494748556811, 'qtr'))
(1, (0.078077467350041008, 'down'))
(6, (0.042192508962130199, 'Sack'))
(4, (0.010155960934120158, 'PassAttempt'))
(5, (0.0057022274330989749, 'RushAttempt'))


f1: 0.0294117647059
acc: 0.981697171381
auc-roc: 0.507379275654

Analysis: This model got low f1 score, but it suggests that the time left in the quarter, yards to go and the difference between scores are the most important factors that can lead to fumble the ball last season.
