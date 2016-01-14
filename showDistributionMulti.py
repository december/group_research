#alpha: 0.0 88.8947476352
#beta: 1.46653800215e-10 20.8215590434
#gamma: 0.0 1.0
#G: 20.0000000009 3459.0
#n: 0.0 1941.0
#n:G: 0.0 1.0

import csv
import numpy
import pylab

csvfile = file('/Users/luyunfei/Desktop/laboratory/graduation project/SIRdecayImpulse/multi_res/simpleParams.csv', 'rb')
reader = csv.reader(csvfile)
data = list()
for line in reader:
	data.append(line)
prefix = '/Users/luyunfei/Desktop/laboratory/graduation project/SIRdecayImpulse/params_distribution_multi/'
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

basicbin = list()
basicbin.append([0.0, 50, 4.0])
basicbin.append([0.0, 50, 2.0])
basicbin.append([0.0, 50, 1.0])
basicbin.append([20.0, 50, 2500.0])
basicbin.append([0.0, 50, 500.0])
basicbin.append([0.0, 50, 1.0])
 
for i in range(6):
	x = list()
	y = list()
	number = basicbin[i][1]
	d = (basicbin[i][2] - basicbin[i][0]) * 1.0 / basicbin[i][1]
	begin = basicbin[i][0] + d / 2
	for j in range(number):
		x.append(begin + j * d)
		y.append(0)
	for k in basic[i]:
		index = int((k - basicbin[i][0]) / d)
		#if i == 5 and k == 0:
		#	continue
		if index == basicbin[i][1]:
			index -= 1
		if index > basicbin[i][1] or index < 0:
			#print index
			#print k
			#print basicbin[i][0]
			#print basicbin[i][2]
			continue
		else:
			y[index] += 1
	#print x
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

twopeak = [0.0, 50, 90.0]
threepeak = [0.0, 50, 95.0]
x = list()
y = list()
d = twopeak[2] / twopeak[1]
begin = twopeak[0] + d / 2
for i in range(3):
	y.append(list())
for i in range(twopeak[1]):
	x.append(begin + i * d)
	y[0].append(0)
	y[1].append(0)
	y[2].append(0)
for i in range(2):
	for k in peak[2][i][0]:
		index = int((k - twopeak[0]) / d)
		if index == twopeak[1]:
			index -= 1
		if index < 0 or index > twopeak[1]:
			continue
		y[i][index] += 1
for i in range(twopeak[1]):
	if i == 0:
		y[0][i] = (y[0][0] + y[0][1]) * 1.0 / 2
		y[1][i] = (y[1][0] + y[1][1]) * 1.0 / 2
		continue
	if i == twopeak[1] - 1:
		y[0][i] = (y[0][i] + y[0][i-1]) * 1.0 / 2
		y[1][i] = (y[1][i] + y[1][i-1]) * 1.0 / 2
		continue
	y[0][i] = (y[0][i] + y[0][i-1] + y[0][i+1]) * 1.0 / 3
	y[1][i] = (y[1][i] + y[1][i-1] + y[1][i+1]) * 1.0 / 3
pylab.plot(x, y[0], 'r')
pylab.plot(x, y[1], 'g')
pylab.xlabel('2 Peaks')
pylab.savefig(prefix+'Twopeak_smooth'+suffix)
pylab.clf()
pylab.cla()
pylab.semilogx(x, y[0], 'r')
pylab.semilogx(x, y[1], 'g')
pylab.xlabel('log(2 Peaks)')
pylab.savefig(prefix+'Twopeak_log_smooth'+suffix)
pylab.clf()
pylab.cla()
d = threepeak[2] / threepeak[1]
begin = threepeak[0] + d / 2
for i in range(threepeak[1]):
	x[i] = begin + i * d
	y[0][i] = 0
	y[1][i] = 0
	y[2][i] = 0
for i in range(3):
	for k in peak[3][i][0]:
		index = int((k - threepeak[0]) / d)
		if index == threepeak[1]:
			index -= 1
		if index < 0 or index > threepeak[1]:
			continue
		y[i][index] += 1
for i in range(threepeak[1]):
	if i == 0:
		y[0][i] = (y[0][0] + y[0][1]) * 1.0 / 2
		y[1][i] = (y[1][0] + y[1][1]) * 1.0 / 2
		y[2][i] = (y[2][0] + y[2][1]) * 1.0 / 2
		continue
	if i == twopeak[1] - 1:
		y[0][i] = (y[0][i] + y[0][i-1]) * 1.0 / 2
		y[1][i] = (y[1][i] + y[1][i-1]) * 1.0 / 2
		y[2][i] = (y[2][i] + y[2][i-1]) * 1.0 / 2
		continue
	y[0][i] = (y[0][i] + y[0][i-1] + y[0][i+1]) * 1.0 / 3
	y[1][i] = (y[1][i] + y[1][i-1] + y[1][i+1]) * 1.0 / 3
	y[2][i] = (y[2][i] + y[2][i-1] + y[2][i+1]) * 1.0 / 3
pylab.plot(x, y[0], 'r')
pylab.plot(x, y[1], 'g')
pylab.plot(x, y[2], 'b')
pylab.xlabel('3 Peaks')
pylab.savefig(prefix+'Threepeak_smooth'+suffix)
pylab.clf()
pylab.cla()
pylab.semilogx(x, y[0], 'r')
pylab.semilogx(x, y[1], 'g')
pylab.semilogx(x, y[2], 'b')
pylab.xlabel('log(3 Peaks)')
pylab.savefig(prefix+'Threepeak_log_smooth'+suffix)
pylab.clf()
pylab.cla()
print 'Finished'
