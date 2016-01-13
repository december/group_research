#alpha: 0.0 88.8947476352
#beta: 1.46653800215e-10 20.8215590434
#gamma: 0.0 1.0
#G: 20.0000000009 3459.0
#n: 0.0 1941.0
#n:G: 0.0 1.0

import csv
import numpy
import pylab

csvfile = file('SIRdecayImpulse/multi_res/simpleParams.csv', 'rb')
reader = csv.reader(csvfile)
data = list()
for line in reader:
	data.append(line)
prefix = 'SIRdecayImpulse/params_distribution_multi/'
suffix = '.png'
name = ['alpha', 'beta', 'gamma', 'G', 'n', 'n:G']
basic = list()
peak = list()
for i in range(6):
	basic.append(list())
for i in range(4):
	n = max(i, 1)
	bigtemp = list()
	for j in range(n): 
		temp = list()
		temp.append(list())
		temp.append(list())
		bigtemp.append(temp)
	peak.append(bigtemp)
for line in data:
	for i in range(5):
		basic[i].append(float(line[i]))
	basic[5].append(basic[4][-1] / basic[3][-1])
	pnum = (len(line) - 5) / 2
	if pnum == 0:
		continue
	if pnum < 4:
		j = 0
		while j < pnum:
			#print j
			#print pnum
			peak[pnum][j][0].append(float(line[j*2+5]))
			peak[pnum][j][1].append(float(line[j*2+6]))
			j += 1
	j = 5
	while j < len(line):
		peak[0][0][0].append(float(line[j]))
		peak[0][0][1].append(float(line[j+1]))
		j += 2
for i in range(6):
	print name[i] + ': ' + str(min(basic[i])) + ' ' + str(max(basic[i])) 



'''
bins = list()
bins.append([0.0, 20, 4])
bins.append([0.0, 10, 1.0])
bins.append([0.0, 10, 1.0])
bins.append([20.0, 20, 3500.0])
bins.append([0.0, 20, 200.0])
bins.append([0.0, 20, 150.0])
bins.append([0.0, 10, 42.0])
distribution = list()
for i in range(7):
	temp = list()
	distribution.append(temp)
for line in data:
	for i in range(7):
		distribution[i].append(float(line[i]))
for 
for i in range(7):
	x = list()
	y = list()
	number = bins[i][1]
	d = (bins[i][2] - bins[i][0]) * 1.0 / bins[i][1]
	begin = bins[i][0] + d / 2
	for j in range(number):
		x.append(begin + j * d)
		y.append(0)
	for k in distribution[i]:
		index = int((k - bins[i][0]) / d)
		if i == 5 and k == 0:
			continue
		if index == bins[i][1]:
			index -= 1
		if index > bins[i][1] or index < 0:
			print index
			print k
			print bins[i][0]
			print bins[i][2]
		else:
			y[index] += 1
	print x
	print y
	pylab.plot(x, y)
	pylab.xlabel(name[i])
	pylab.savefig(prefix+name[i]+suffix)
	pylab.clf()
	pylab.cla()
	pylab.semilogx(x, y)
	pylab.xlabel('log('+name[i]+')')
	pylab.savefig(prefix+name[i]+'_log'+suffix)
	pylab.clf()
	pylab.cla()
ng = list()
for i in range(2022):
	ng.append(distribution[4][i] * 1.0 / distribution[3][i])
bins.append([0.0, 10, 1.0])
d = 0.1
x = list()
y = list()
begin = 0.05
for j in range(10):
	x.append(begin + j * d)
	y.append(0)
for k in ng:
	index = int((k - bins[7][0]) / d)
	y[index] += 1
pylab.plot(x, y)
pylab.xlabel(name[7])
pylab.savefig(prefix+name[7]+suffix)
pylab.clf()
pylab.cla()
pylab.semilogx(x, y)
pylab.xlabel('log('+name[7]+')')
pylab.savefig(prefix+name[7]+'_log'+suffix)
pylab.clf()
pylab.cla()
'''
print 'Finished'
