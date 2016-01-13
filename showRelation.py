#0.alpha bound:0-4
#1.beta bound:0-1
#2.gamma bound:0-1
#3.G bound:20-3459
#4.n bound:0-2000
#5.lambdaval bound:0-150
#6.delta bound:0-42
import csv
import numpy
import pylab

upper = [4, 1, 1, 3460, 2000, 150,42]
outlier = 0

def checkBound(item):
	for i in range(7):
		if float(item[i]) > upper[i]:
			return False
	return True

csvfile = file('SIRdecayImpulse/lyf_res/simpleParams.csv', 'rb')
reader = csv.reader(csvfile)
data = list()
for line in reader:
	data.append(line)
prefix = 'SIRdecayImpulse/params_relation/'
suffix = '.png'
name = ['alpha', 'beta', 'gamma', 'G', 'n', 'lambdaval', 'delta', 'n:G']
distribution = list()
for i in range(8):
	temp = list()
	distribution.append(temp)
for line in data:
	if checkBound(line):
		for i in range(7):
			distribution[i].append(float(line[i]))
		distribution[7].append(float(line[4]) / float(line[3]))
	else:
		outlier += 1
for i in range(8):
	for j in range(i+1, 8):
		pylab.scatter(distribution[i], distribution[j], s=10, c='r')
		pylab.xlabel(name[i])
		pylab.ylabel(name[j])
		pylab.savefig(prefix+name[i]+'-'+name[j]+suffix)
		pylab.clf()
		pylab.cla()

print outlier
print 'Finished'
