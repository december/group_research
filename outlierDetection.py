import csv
import numpy
import random
from sklearn import svm
from sklearn import cross_validation

rate = 0.2

#Multi
csvfile = file('SIRdecayImpulse/multi_res/simpleParams.csv', 'rb')
reader = csv.reader(csvfile)
params = list()
count = 0
for line in reader:
	tplist = list()
	for i in range(len(line)):
		if i < 3:
			tplist.append(float(line[i]))
	#while len(tplist) < 19:
	#	tplist.append(0)
	tplist.append(count)
	params.append(tplist)
	count += 1

testlist = list()
testid = list()
trainlist = list()
trainid = list()
for i in range(2022):
	r = random.random()
	if r < rate:
		testlist.append(params[i][:-1])
		testid.append(params[i][-1])
	else:
		trainlist.append(params[i][:-1])
		trainid.append(params[i][-1])
testlist = numpy.array(testlist)
trainlist = numpy.array(trainlist)
clf = svm.OneClassSVM()
clf.fit(trainlist)
result = clf.predict(testlist)
outlier = 0
for i in range(len(testid)):
	if result[i] == -1:
		print testid[i]
		outlier += 1
print 'All:' + str(len(testid))
print 'Outliers:' + str(outlier)
print 'Finished.'

