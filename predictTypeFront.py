#distribution:[183, 709, 211]
import csv
import numpy
from sklearn import cross_validation
from sklearn import svm

stable = 0

def getType(data, c):
	n = len(data[0])
	end = int(data[1][-1]) - int(data[3][-1])
	middle = int(data[1][-6]) - int(data[3][-6])
	begin = int(data[1][-11]) - int(data[3][-11])
	delta = abs(end - begin)
	if begin < 0 or end < 0:
		print 'Errordata ' + str(c)
		return 0
	if begin == 0:
		if end == 0:
			return 0
		else:
			print 'Amazing!'
			return 1
	rate = delta * 1.0 / begin
	'''
	midrate = abs((middle - begin) * 1.0 / begin)
	if rate <= 0.05 and midrate < 0.05:
		global stable
		stable += 1
		
		if stable > 0:
			return 0
		
		return 2
	'''
	if rate >= 0.2:
		if end > begin:
			return 1
		else:
			return 3
	return 0

csvfile = file('usefulID.csv', 'rb')
reader = csv.reader(csvfile)
idlist = list()
for line in reader:
	idlist.append(line)
csvfile.close()
print len(idlist)
csvfile = file('badID.csv', 'rb')
reader = csv.reader(csvfile)
badlist = list()
for line in reader:
	badlist.append(line)
csvfile.close()
csvfile = file('SIRdecayImpulse/group_data_lyf/idset.csv', 'rb')
reader = csv.reader(csvfile)
idset = list()
for line in reader:
	idset.append(line)
csvfile.close()
target = list()
count = 0
for line in idlist:
	flag = False
	for per in badlist:
		if per[0] == line[0]:
			flag = True
			break
	if flag:
		continue
	name = idset[int(line[0].strip())][0].strip()
	csvfile = file('SIRdecayImpulse/group_data_lyf/' + name + '.csv', 'rb')
	reader = csv.reader(csvfile)
	unitdata = list()
	for unit in reader:
		unitdata.append(unit)
	csvfile.close()
	result = getType(unitdata, count)
	if result != 0:
		target.append(result)
	count += 1
	if count >= 2022:
		break
print count
csvfile.close()
csvfile = file('SIRdecayImpulse/single_predict/simpleParams.csv', 'rb')
reader = csv.reader(csvfile)
params = list()
'''
#Multi
for line in reader:
	tplist = list()
	#if len(line) < 7 or line[-1] < 
	for i in range(len(line)):
		#if i != 3 and i != 4:
		if i < 3:
			tplist.append(float(line[i]))
	#tplist = list(line)
	#while len(tplist) < 15:
	#	tplist.append(0)
	params.append(tplist)
'''
#Single
for line in reader:
	tplist = list()
	for i in range(len(line)):
		#if i == 3 and i == 5:
		#	tplist.append(line[i] * 1.0 / line[4])
		#if i != 3 and i != 4:
		#if i < 3:
			tplist.append(float(line[i]))
	params.append(tplist)

feature = numpy.array(params)
target = numpy.array(target)
print feature.shape
print target.shape
f_train, f_test, t_train, t_test = cross_validation.train_test_split(feature, target, test_size=0.2, random_state=0)
print f_train.shape
print f_test.shape
clf = svm.LinearSVC().fit(f_train, t_train)
print clf.coef_
#clf = svm.SVC().fit(f_train, t_train)
#print f_test
#result = clf.predict(f_test)
print clf.score(f_test, t_test)
'''
idfile = list()
for i in usefulID:
	perline = list()
	perline.append(i)
	idfile.append(perline)
csvwrite = file('usefulID.csv', 'wb')
writer = csv.writer(csvwrite)
writer.writerows(idfile)
csvwrite.close()
errorlist = list()
clf = svm.SVC().fit(feature, target)
print clf.score(feature, target)
result = clf.predict(feature)

for i in range(len(result)):
	if result[i] != target[i]:
		errorlist.append(usefulID[i])
print errorlist
'''



