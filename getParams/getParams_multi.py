import csv

csvfile = file('multi_30_0_135621_res_params.csv', 'rb')
reader = csv.reader(csvfile)
data = list()
for line in reader:
	data.append(line)
params = list()
unit = list()
temp = list()
'''
maxparam = list()
minparam = list()
for i in range(7):
	maxparam.append(-1)
	minparam.append(100)
'''
peaks = {}
count = 0
for line in data:
	ps = len(line) / 4
	pk = (ps - 5) / 2
	if pk > 4:
		print count
	count += 1
	if peaks.has_key(pk):
		peaks[pk] += 1
	else:
		peaks[pk] = 1
	for i in range(ps):
		temp = line[i*4+2].split(' ')
		p = float(temp[1][6:])
		'''
		if p > maxparam[i]:
			maxparam[i] = p
		if p < minparam[i]:
			minparam[i] = p
		'''
		unit.append(p)
	params.append(unit)
	unit = list()
csvwrite = file('simpleMulti_30.csv', 'wb')
writer = csv.writer(csvwrite)
writer.writerows(params)
csvwrite.close()
'''
print maxparam
print minparam
'''
print peaks
print 'Finished'
