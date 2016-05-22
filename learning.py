import numpy as np
import csv
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
clf = MultinomialNB()

test = open('test_large.csv','rb')
f = open('train_large.csv', 'rb')

cnt = 0
y = np.array([])
X = np.array([])
rd = csv.reader(f, delimiter =',', quotechar='|')
for row in rd:
	y =np.append(y, int(row[0]))
	rt = map(int, row[1:5001])
	arr = np.array(rt)
	if cnt == 0:
		X = np.zeros(shape=(1,5000))
	else:	
		X = np.vstack((X,arr))
	cnt += 1
	if (cnt % 1000 ==0):
		print cnt
	if cnt > 5000:
		break
clf.fit(X,y)

cnt = 0
test_y = np.array([])
test_X = np.array([])
rd = csv.reader(test, delimiter =',', quotechar='|')
for row in rd:
	test_y =np.append(test_y, int(row[0]))
	rt2 = map(int, row[1:5001])
	arr = np.array(rt2)
	if cnt == 0:
		test_X = np.zeros(shape=(1,5000))
	else:	
		test_X = np.vstack((test_X,arr))
	cnt += 1
	if (cnt % 1000 ==0):
		print cnt
	if cnt > 5000:
		break


haha= 0 
pred = clf.predict(test_X)

print "accuracy", accuracy_score(test_y,pred)

print "classification_report", classification_report(test_y, pred)


