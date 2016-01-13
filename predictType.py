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
	midrate = abs((middle - begin) * 1.0 / begin)
	if rate <= 0.05 and midrate < 0.05:
		global stable
		stable += 1
		
		if stable > 0:
			return 0
		
		return 2
	if rate >= 0.2:
		if end > begin:
			return 1
		else:
			return 3
	return 0

csvfile = file('SIRdecayImpulse/group_data_lyf/idset.csv', 'rb')
reader = csv.reader(csvfile)
idlist = list()
riselist = list()
falllist = list()
badlist = list()
for line in reader:
	idlist.append(line)
csvfile.close()
target = list()
count = 0
usefulID = list()
days = list()
distribution = [0, 0, 0]
for line in idlist:
	name = line[0].strip()
	csvfile = file('SIRdecayImpulse/group_data_lyf/' + name + '.csv', 'rb')
	reader = csv.reader(csvfile)
	unitdata = list()
	for unit in reader:
		unitdata.append(unit)
	csvfile.close()
	days.append(len(unitdata[0]))
	result = getType(unitdata, count)
	if result != 0:
		usefulID.append(count)
		if result == 1:
			riselist.append(count)
		else:
			falllist.append(count)
		target.append(result)
		distribution[result-1] += 1
	count += 1
	if count >= 2022:
		break
csvfile.close()
csvfile = file('SIRdecayImpulse/multi_res/simpleParams.csv', 'rb')
reader = csv.reader(csvfile)
params = list()

#Multi
count = 0
for line in reader:
	tplist = list()
	#if len(line) < 7 or line[-1] < 
	if len(line) > 5 and float(line[-1]) >= days[count] - 10:
		badlist.append(count)
	for i in range(len(line)):
		#if i != 3 and i != 4:
		if i < 5:
			tplist.append(float(line[i]))
	#tplist = list(line)
	#while len(tplist) < 19:
	#	tplist.append(0)
	count += 1
	params.append(tplist)
'''
#Single
for line in reader:
	tplist = list()
	for i in range(len(line)):
		#if i == 3 and i == 5:
		#	tplist.append(line[i] * 1.0 / line[4])
		#if i != 3 and i != 4:
		#if i < 5:
			tplist.append(float(line[i]))
	params.append(tplist)
'''
feature = list()
for line in usefulID:
	feature.append(params[line])
feature = numpy.array(feature)
target = numpy.array(target)
f_train, f_test, t_train, t_test = cross_validation.train_test_split(feature, target, test_size=0.2, random_state=0)
clf = svm.LinearSVC().fit(f_train, t_train)
print clf.coef_
#clf = svm.SVC().fit(f_train, t_train)
#print f_test
#result = clf.predict(f_test)
result = clf.predict(f_test)
print result
print clf.score(f_test, t_test)
idfile = list()
for i in usefulID:
	perline = list()
	perline.append(i)
	idfile.append(perline)
csvwrite = file('usefulID.csv', 'wb')
writer = csv.writer(csvwrite)
writer.writerows(idfile)
csvwrite.close()
badfile = list()

for i in badlist:
	perline = list()
	perline.append(i)
	badfile.append(perline)
csvwrite = file('badID.csv', 'wb')
writer = csv.writer(csvwrite)
writer.writerows(badfile)
csvwrite.close()
'''
errorlist = list()
clf = svm.SVC().fit(feature, target)
print clf.score(feature, target)
result = clf.predict(feature)

for i in range(len(result)):
	if result[i] != target[i]:
		errorlist.append(usefulID[i])
print errorlist
'''




