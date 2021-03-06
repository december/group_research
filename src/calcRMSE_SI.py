import loadGroupData
import optGroupData
import disGroupData
import SIRd
import csv
import numpy
from scipy import stats

flatlist = list()
length = 42
haveFlat = False

def rmse(prediciton, target):
	prediciton = numpy.array(prediciton)
	target = numpy.array(target)
	return numpy.sqrt(((prediciton - target) ** 2).mean())

def getCurve(p, flag, steps):
	p = [float(k) for k in p]
	t = SIRd.SI(p[0], p[1], p[2], steps)
	s = [k/p[1] for k in t[flag]]
	return t[flag], s

def isFlat(fl, order):
	if len(fl) == 1:
		if fl[0] == order:
			return True
		else:
			return False
	index = len(fl) / 2
	if fl[index] == order:
		return True
	if fl[index] > order:
		return isFlat(fl[:index], order)
	if fl[index] < order:
		if index + 1 >= len(fl):
			return False
		return isFlat(fl[index+1:], order)

#kick out flat groups
if not haveFlat:
	csvfile = file('../../flatID.csv', 'rb')
	reader = csv.reader(csvfile)
	for line in reader:
		flatlist.append(int(line[0].strip()))
	print len(flatlist)

s = 0
t = 0
csvfile = file('../../model_params_20dyas_and_30days/simpleSI_30.csv', 'rb')
reader = csv.reader(csvfile)
params = list()
for line in reader:
	params.append(line)
test = list()

total = 135621
for i in range(total):
	#print i
	if i % 1000 == 0:
		print i
	rawdata = loadGroupData.load_data(i)
	come = numpy.array(rawdata[1][:length])
	go = numpy.array(rawdata[3][:length])
	for j in range(len(come)):
		come[j] -= go[j]
	result = list()
	#res = getCurve(params[i], 0)
	t1, t2 = getCurve(params[i], 0, len(come))
	temp = rmse(t1, come)
	t += temp
	result.append(temp)
	come = [k/float(params[i][1]) for k in come]
	temp = rmse(t2, come)
	s += temp
	result.append(temp)
	'''
	t1, t2 = getCurve(params[i], 2, len(go))
	temp = rmse(t1, go)
	result.append(temp)
	go = [k/float(params[i][3]) for k in go]
	temp = rmse(t2, go)
	result.append(temp)
	'''
	test.append(result)
csvwrite = file('../../rawdata/rmseSI'+str(length)+'.csv', 'wb')
writer = csv.writer(csvwrite)
writer.writerows(test)
csvwrite.close()
print s / total
print t / total
print 'Finished.'