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

sep = []
public = [0, 0, 0]

#get 20000 target group ids
f = open('../data20000/20151020_gid_20151120_20000')
line = f.readline()
idlist = line.strip().split(',') 
f.close()
print len(idlist)
print 'Getting target group ID finished...'

#people added into the group by others
csvfile = file('../data20000/10299_20151120_20151122_20000_r.csv', 'rb')
reader = csv.reader(csvfile)
data = list()
for line in reader:
	data.append(line)
csvfile.close()
come = data[1:]
csvfile = file('../data20000/10299_20151123_20151127.csv', 'rb')
reader = csv.reader(csvfile)
data = list()
for line in reader:
	data.append(line)
csvfile.close()
for line in data:
	if line[0] in idlist and int(line[3]) < 1448380800:
		come.append(line)
filename = ['10299_20151125_20151202_20000', '10299_20151203_20151212_20000', '10299_20151213_20151222_20000', '10299_20151223_20151231_20000']
for fn in filename:	
	csvfile = file('../data20000/' + fn + '.csv', 'rb')
	reader = csv.reader(csvfile)
	data = list()
	for line in reader:
		data.append(line)
	csvfile.close()
	come.extend(data[1:])
sep.append(len(come))
print 'Added-part Finished.'

#people scan the 2D barcode
filename = ['10312_20151120_20151122_r', '10312_20151123_20151127', '10312_20151128_20151213_20000', '10312_20151214_20151231_20000']
for fn in filename:
	csvfile = file('../data20000/' + fn + '.csv', 'rb')
	reader = csv.reader(csvfile)
	data = list()
	for line in reader:
		data.append(line)
	csvfile.close()
	for line in data:
		if line[0] in idlist and int(line[4]) == 1:
			come.append(line)
sep.append(len(come))
print 'Scan-part Finished.'

#people invited to the group
filename = ['11088_20151120_20151122', '11088_20151123_20151127', '11088_20151128_20151231_20000']
for fn in filename:
	csvfile = file('../data20000/' + fn + '.csv', 'rb')
	reader = csv.reader(csvfile)
	data = list()
	for line in reader:
		data.append(line)
	csvfile.close()
	for line in data:
		if line[0] in idlist and int(line[4]) == 1:
			come.append(line)
print 'Invited-part Finished.'
sep.append(len(come))

#examine 10061
csvfile = file('../data20000/10061_20151120_40.csv', 'rb')
reader = csv.reader(csvfile)
data = list()
for line in reader:
	data.append(line)
csvfile.close()
print 'Begin examining...'
count = 0
newitem = 0
for line in data:
	count += 1
	if count % 10000 == 0:
		print count
	if line[0] not in idlist or int(line[4]) == 2:
		continue
	flag = True
	for i in range(len(come)):
		if line[0] == come[i][0] and line[1] == come[i][1] and abs(int(line[2]) - int(come[i][3])) < 5:
			flag = False
			for j in range(3):
				if i < sep[j]:
					public[j] += 1
			break
	if flag:
		tplist = line[:2]
		tplist.append(0)
		tplist.append(line[2])
		come.append(tplist)
		newitem += 1
print newitem
print public
print sep
print 'Examining Finished.'
'''
#exit and order
csvfile = file('../data20000/12078_20151120_20160117.csv', 'rb')
reader = csv.reader(csvfile)
data = list()
for line in reader:
	data.append(line)
csvfile.close()
splist = list()
for line in data:
	tplist = list()
	tplist.append(line[0])
	tplist.append(int(line[2]))
	tplist.append(1)
	splist.append(tplist)
for line in come:
	tplist = list()
	tplist.append(line[0])
	tplist.append(int(line[3]))
	tplist.append(0)
	splist.append(tplist)
splist.sort(lambda x,y:mycmp(x, y))
print 'Order Finished...'

#calculate and output
idset = list()
day = 86400
lastid = -1
unitdata = list()
begintime = 0
for line in splist:
	if line[0] != lastid:
		if lastid != -1:
			daylist.append(d)
			comelist.append(c)
			golist.append(g)
			while date < 30:
				date += 1
				daylist.append(d)
				comelist.append(c)
				golist.append(g)
			unitdata.append(daylist)
			unitdata.append(comelist)
			unitdata.append(daylist)
			unitdata.append(golist)
			csvwrite = file('../groupdata_20000/' + lastid + '.csv', 'wb')
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
		go += 1
	else:
		come += 1
csvwrite = file('../groupdata_20000/idset.csv', 'wb')
writer = csv.writer(csvwrite)
writer.writerows(idset)
csvwrite.close()
'''
print 'Finished'

