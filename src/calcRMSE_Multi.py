import loadGroupData
import optGroupData
import disGroupData
import SIRd
import csv
import numpy
from scipy import stats

c = 0
flatlist = list()
length = 42
haveFlat = False

def rmse(prediciton, target, p):
	prediciton = numpy.array(prediciton)
	target = numpy.array(target)
	mr = numpy.sqrt(((prediciton - target) ** 2).mean())
	if mr > 1000000000:
		print prediciton
		print target
		print p
		global c
		c += 1
		return 0
	else:
		return mr

def getCurve(p, flag, steps):
	p = [float(k) for k in p]
	cnt = 5
	l = list()
	d = list()
	while cnt < len(p):
		l.append(p[cnt])
		d.append(p[cnt+1])
		cnt += 2
	t = SIRd.SIRdecayMultiImpulse(p[2], p[0], p[1], p[3], p[4], steps, l, d)
	s = [k/p[3] for k in t[flag]]
	return t[flag], s

def calcAt(Pt, Nt, g):
	n = len(Pt)
	At = list()
	for i in range(n):
		At.append(Pt[i] - Nt[i])
	newAt = [k/g for k in At]
	return At, newAt

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

csvfile = file('../../rawresult/simpleMulti.csv', 'rb')
reader = csv.reader(csvfile)
params = list()
comermse = list()
atrmse = list()
gormse = list()
s1 = 0
s2 = 0
s3 = 0

total = 135621
for line in reader:
	params.append(line)
test = list()
for i in range(total):
	if i % 1000 == 0:
		print i
	if isFlat(flatlist, i):
		continue
	rawdata = loadGroupData.load_data(i)
	at = list()
	for j in range(length):
		at.append(float(rawdata[1][j]) - float(rawdata[3][j]))
	come = numpy.array(rawdata[1][:length])
	go = numpy.array(rawdata[3][:length])
	result = list()
	#res = getCurve(params[i], 0)
	t1, t2 = getCurve(params[i], 0, len(come))
	p = params[i]
	temp = rmse(t1, come, p)
	result.append(temp)
	s1 += temp
	come = [k/float(params[i][3]) for k in come]
	temp = rmse(t2, come, p)
	result.append(temp)
	comermse.append(temp)

	t3, t4 = getCurve(params[i], 2, len(go))
	temp = rmse(t3, go, p)
	result.append(temp)
	s2 += temp
	go = [k/float(params[i][3]) for k in go]
	temp = rmse(t4, go, p)
	result.append(temp)
	gormse.append(temp)

	t5, t6 = calcAt(t1, t3, float(params[i][3]))
	temp = rmse(t5, at, p)
	result.append(temp)
	s3 += temp
	at = [k/float(params[i][3]) for k in at]
	temp = rmse(t6, at, p)
	result.append(temp)
	atrmse.append(temp)

	test.append(result)
csvwrite = file('../../rawdata/rmseMulti'+str(length)+'.csv', 'wb')
writer = csv.writer(csvwrite)
writer.writerows(test)
csvwrite.close()
total -= c
print c
print s1 / total
print s2 / total
print s3 / total
print sum(comermse) / len(comermse)
print sum(gormse) / len(gormse)
print sum(atrmse) / len(atrmse)
print 'Finished.'