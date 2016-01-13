import loadGroupData
import optGroupData
import disGroupData
import SIRd
import csv
import numpy
from scipy import stats

def rmse(prediciton, target):
	prediciton = numpy.array(prediciton)
	target = numpy.array(target)
	return numpy.sqrt(((prediciton - target) ** 2).mean())

def getCurve(p, flag, steps):
	p = [float(k) for k in p]
	t = SIRd.SIRd(p[1], 0, p[0], p[2], p[3], steps)
	s = [k/p[2] for k in t[flag]]
	return t[flag], s

def calcAt(Pt, Nt, g):
	n = len(Pt)
	At = list()
	for i in range(n):
		At.append(Pt[i] - Nt[i])
	newAt = [k/g for k in At]
	return At, newAt

s1 = 0
s2 = 0
csvfile = file('../sir_res/simpleParams.csv', 'rb')
reader = csv.reader(csvfile)
params = list()
comermse = list()
atrmse = list()
gormse = list()
for line in reader:
	params.append(line)
test = list()
for i in range(2022):
	#print i
	rawdata = loadGroupData.load_data(i)
	at = list()
	for j in range(len(rawdata[1])):
		at.append(float(rawdata[1][j]) - float(rawdata[3][j]))

	come = numpy.array(rawdata[1])
	go = numpy.array(rawdata[3])
	result = list()
	#res = getCurve(params[i], 0)
	t1, t2 = getCurve(params[i], 0, len(come))
	temp = rmse(t1, come)
	result.append(temp)
	come = [k/float(params[i][2]) for k in come]
	temp = rmse(t2, come)
	s1 += temp
	result.append(temp)
	comermse.append(temp)

	t3, t4 = getCurve(params[i], 2, len(go))
	temp = rmse(t3, go)
	result.append(temp)
	go = [k/float(params[i][2]) for k in go]
	temp = rmse(t4, go)
	s2 += temp
	result.append(temp)
	gormse.append(temp)

	t5, t6 = calcAt(t1, t3, float(params[i][2]))
	temp = rmse(t5, at)
	result.append(temp)
	at = [k/float(params[i][2]) for k in at]
	temp = rmse(t6, at)
	result.append(temp)
	atrmse.append(temp)

	test.append(result)
csvwrite = file('../sir_res/rmse.csv', 'wb')
writer = csv.writer(csvwrite)
writer.writerows(test)
csvwrite.close()
print s1 / 2022
print s2 / 2022
print sum(comermse) / len(comermse)
print sum(gormse) / len(gormse)
print sum(atrmse) / len(atrmse)
print 'Finished.'