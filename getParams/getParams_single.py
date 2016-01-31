import csv

csvfile = file('siParams.csv', 'rb')
reader = csv.reader(csvfile)
data = list()
for line in reader:
	data.append(line)
params = list()
unit = list()
temp = list()
maxparam = list()
minparam = list()
for i in range(3):
	maxparam.append(-1)
	minparam.append(100)
for line in data:
	for i in range(3):
		temp = line[i*4+2].split(' ')
		p = float(temp[1][6:])
		if p > maxparam[i]:
			maxparam[i] = p
		if p < minparam[i]:
			minparam[i] = p
		unit.append(p)
	params.append(unit)
	unit = list()
csvwrite = file('simpleSI.csv', 'wb')
writer = csv.writer(csvwrite)
writer.writerows(params)
csvwrite.close()
print maxparam
print minparam
print 'Finished'
