#0.alpha max:376.3188752251327 min:9.703349235223868e-14
#1.beta max:0.9999999999999991 min:1.4083010535514973e-08
#2.gamma max:1 min:0
#3.G max:3459 min:20.000000172440952
#4.n max:1941 min:0
#5.lambdaval max:1452.137019312928 min:0
#6.delta max:42 min:1
import csv
import numpy
import pylab

csvfile = file('SIRdecayImpulse/lyf_res/simpleParams.csv', 'rb')
reader = csv.reader(csvfile)
data = list()
for line in reader:
	data.append(line)
prefix = 'SIRdecayImpulse/params_distribution/'
suffix = '.png'
name = ['alpha', 'beta', 'gamma', 'G', 'n', 'lambdaval', 'delta', 'n:G']
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
	'''
	temp = numpy.array(distribution[i])
	bin = numpy.arange(bins[i][0], bins[i][1], bins[i][2])
	print temp
	pylab.hist(temp, bin)
	'''
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

print 'Finished'
