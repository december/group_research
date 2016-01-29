import csv
csv.field_size_limit(1000000000)

def mycmp(x, y):
	if x[0] < y[0]:
		return -1
	if x[0] > y[0]:
		return 1
	if x[0] == y[0]:
		if x[1] < y[1]:
			return -1
		if x[1] > y[1]:
			return 1
	return 0

def newcmp(x, y):
	if x[0] < y[0]:
		return -1
	if x[0] > y[0]:
		return 1
	if x[0] == y[0]:
		if x[1] < y[1]:
			return -1
		if x[1] > y[1]:
			return 1
		if x[1] == y[1]:
			if int(x[3]) < int(y[3]):
				return -1;
			if int(x[3]) > int(y[3]):
				return 1;
	return 0

def isEqual(x, y):
	if x[0] == y[0] and x[1] == y[1] and abs(int(x[3]) - int(y[3])) < 5:
		return True
	return False

public = [0, 0, 0]
sep = []

#get all target group ids
idlist = list()
filename = ['20151020_gid_20151120_20000', '20151020_gid_20151120_40000', '20151020_gid_20151120_60000', '20151020_gid_20151120_60000-100000', '20151020_gid_20151120_100000-135667']
for fn in filename:
	f = open('../origindata/' + fn)
	line = f.readline()
	tplist = line.strip().split(',') 
	idlist.extend(tplist)
f.close()
print len(idlist)
print 'Getting target group ID finished...'

#people added into the group by others
come = list()
csvfile = file('../origindata/10299_20151125_20151202_20000.csv', 'rb')
reader = csv.reader(csvfile)
data = list()
for line in reader:
	line[2] = 0
	data.append(line)
csvfile.close()
data = data[1:]
for line in data:
	if int(line[3]) >= 1448640000:
		come.append(line)
filename = ['10299_20151120_20151122', '10299_20151123_20151127', '10299_20151203_20151212_20000', '10299_20151213_20151222_20000', '10299_20151223_20151231_20000', '10299_20151128_20151231_40000', '10299_20151128_20151231_60000', '10299_20151128_20151231_60000-100000', '10299_20151128_20151231_100000-135667']
for fn in filename:	
	csvfile = file('../origindata/' + fn + '.csv', 'rb')
	reader = csv.reader(csvfile)
	data = list()
	for line in reader:
		line[2] = 0
		data.append(line)
	csvfile.close()
	come.extend(data[1:])
sep.append(len(come))
print 'Added-part Finished.'

#people scan the 2D barcode
filename = ['10312_20151120_20151122_r', '10312_20151123_20151127', '10312_20151128_20151213_20000', '10312_20151214_20151231_20000', '10312_20151128_20151231_40000', '10312_20151128_20151231_60000', '10312_20151128_20151231_60000-100000', '10312_20151128_20151231_100000-135667']
for fn in filename:
	csvfile = file('../origindata/' + fn + '.csv', 'rb')
	reader = csv.reader(csvfile)
	data = list()
	for line in reader:
		line[2] = 1
		data.append(line)
	csvfile.close()
	data = data[1:]
	for line in data:
		if int(line[4]) == 1:
			come.append(line)
sep.append(len(come) - sep[0])
print 'Scan-part Finished.'

#people invited to the group
filename = ['11088_20151120_20151122', '11088_20151123_20151127', '11088_20151128_20151231_20000', '11088_20151128_20151231_40000', '11088_20151128_20151231_60000', '11088_20151128_20151231_60000-100000', '11088_20151128_20151231_100000-135667']
for fn in filename:
	csvfile = file('../origindata/' + fn + '.csv', 'rb')
	reader = csv.reader(csvfile)
	data = list()
	for line in reader:
		line[2] = 2
		data.append(line)
	csvfile.close()
	data = data[1:]
	for line in data:
		if int(line[4]) == 1:
			come.append(line)
sep.append(len(come) - sep[0] - sep[1])
print 'Invited-part Finished.'

#examine 10061
csvfile = file('../origindata/10061_20151120_40.csv', 'rb')
reader = csv.reader(csvfile)
data = list()
for line in reader:
	data.append(line)
csvfile.close()
data = data[1:]
count = 0
newitem = 0
for line in data:
	count += 1
	if count % 10000 == 0:
		print count
	if int(line[4]) == 2 or int(line[2]) >= 1451577600 or line[0] not in idlist:
		continue
	tplist = line[:2]
	tplist.append(3)
	tplist.append(line[2])
	come.append(tplist)
	newitem += 1
print 'Examinine data ready.'
come.sort(lambda x,y:newcmp(x, y))
mycome = list()
error = 0
errorlist = list()
for i in range(len(come)):
	if int(come[i][3]) >= 1451577600:
		continue
	if come[i][2] != 3:
		mycome.append(come[i])
	else:
		flag = True
		if i > 0 and isEqual(come[i], come[i-1]):
			flag = False
			newitem -= 1
			if come[i-1][2] == 3:
				if come[i-1][3] != come[i][3]:
					tplist = list()
					errorlist.append(come[i-1])
					errorlist.append(come[i])
					error += 1
			else:
				public[come[i-1][2]] += 1
		if flag and i < len(come) and isEqual(come[i], come[i+1]):
			if come[i+1][2] != 3:
				public[come[i+1][2]] += 1
				newitem -= 1
				flag = False
		if flag:
			mycome.append(come[i])
print 'Examining Finished.'
print error
print newitem
print public
print sep
csvwrite = file('../groupdata/errorlist.csv', 'wb')
writer = csv.writer(csvwrite)
writer.writerows(errorlist)
csvwrite.close()

#exit and order
csvfile = file('../origindata/12078_20151120_20160117.csv', 'rb')
reader = csv.reader(csvfile)
data = list()
for line in reader:
	if line[2][0] != 't' and int(line[2]) < 1451577600:
		data.append(line)
csvfile.close()
splist = list()
for line in data:
	tplist = list()
	tplist.append(line[0])
	tplist.append(int(line[2]))
	tplist.append(1)
	splist.append(tplist)
for line in mycome:
	tplist = list()
	tplist.append(line[0])
	tplist.append(int(line[3]))
	tplist.append(0)
	splist.append(tplist)
splist.sort(lambda x,y:mycmp(x, y))
print 'Order Finished...'

#calculate and output
splist.append([-1, 0, 2])
idset = list()
day = 86400
lastid = -1
unitdata = list()
begintime = 0
d = 0
c = 0
g = 0
daylist = list()
comelist = list()
golist = list()
for line in splist:
	if line[0] != lastid:
		if lastid != -1:
			daylist.append(d)
			comelist.append(c)
			golist.append(g)
			while d < 42:
				d += 1
				daylist.append(d)
				comelist.append(c)
				golist.append(g)
			unitdata.append(daylist)
			unitdata.append(comelist)
			unitdata.append(daylist)
			unitdata.append(golist)
			csvwrite = file('../groupdata/' + lastid + '.csv', 'wb')
			writer = csv.writer(csvwrite)
			writer.writerows(unitdata)
			csvwrite.close()
			unitdata = list()
		d = 0
		c = 0
		g = 0
		daylist = list()
		comelist = list()
		golist = list()
		lastid = line[0]
		tplist = list()
		tplist.append(line[0])
		idset.append(tplist)
		begintime = int(line[1])
	while (int(line[1]) - begintime > (d + 1) * day):
		daylist.append(d)
		comelist.append(c)
		golist.append(g)
		d += 1
	if int(line[2]) == 1:
		g += 1
	else:
		c += 1
daylist.append(d)
comelist.append(c)
golist.append(g)
while d < 42:
	d += 1
	daylist.append(d)
	comelist.append(c)
	golist.append(g)
unitdata.append(daylist)
unitdata.append(comelist)
unitdata.append(daylist)
unitdata.append(golist)
csvwrite = file('../groupdata/' + lastid + '.csv', 'wb')
writer = csv.writer(csvwrite)
writer.writerows(unitdata)
csvwrite.close()

csvwrite = file('../groupdata/idset.csv', 'wb')
writer = csv.writer(csvwrite)
writer.writerows(idset)
csvwrite.close()

print 'Finished'

