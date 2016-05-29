import numpy as np
import csv
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
import pandas as pd
import pdb

clf = MultinomialNB()

train_data = pd.read_csv('xaa')
test_data = pd.read_csv('xab')

X = train_data.ix[:,1:]
y = train_data.ix[:,0]

clf.fit(X,y)

test_X = test_data.ix[:,1:]
test_y = test_data.ix[:,0]

pred = clf.predict(test_X)

print "accuracy", accuracy_score(test_y,pred)

print "classification_report", classification_report(test_y, pred)


