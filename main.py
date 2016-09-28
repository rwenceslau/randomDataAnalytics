import graphlab
import time

train = graphlab.SFrame.read_csv("data/adult.csv", ',', header=False, column_type_hints=[int, str, int, str, int, str, str, str, str, str, int, int, int, str, str])
test = graphlab.SFrame.read_csv("data/new_adult_test.csv", ',', header=False, column_type_hints=[int, str, int, str, int, str, str, str, str, str, int, int, int, str, str])

#graphlab.canvas.set_target('ipynb')
graphlab.canvas.set_target('headless', port=12345)
#print(train.head(10))
#train.show()

#time.sleep(900)
# Filtering only individuals with salaries > 50K/y
#salaries_filterHI = train[train['X15'] == '>50K']
#salaries_filterLO = train[train['X15'] == '<=50K']

#salaries_filterHI.show()
#salaries_filterLO.show()
#print salaries_filter.head(10)

features = ['X4', 'X5', 'X11', 'X12', 'X13', 'X1', 'X2', 'X9']
model_one = graphlab.random_forest_classifier.create(train, target='X15', features=features, verbose=False, max_iterations=25)
model_two = graphlab.logistic_classifier.create(train, target='X15')

#predictions = model.classify(test)
predictions_one = model_one.predict(test)
predictions_two = model_two.classify(test)
results_one = model_one.evaluate(test)
results_two = model_two.evaluate(test)
#results_sorted = results[results['class'] == 1].sort("probability")
#print predictions
print '\n RANDOM FOREST CLASSIFIER RESULTS'
print results_one

print '\n LOGISTIC REGRESSION CLASSIFIER RESULTS'
print results_two
#print results_sorted
#model.show(view='Tree', tree_id=1)
#