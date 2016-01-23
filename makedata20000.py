import csv

sep = []
public = [0, 0, 0]

#get 20000 target group ids
f = open('../data20000/20151020_gid_20151120_20000')
line = f.readline()
idlist = line.strip().split(',') 
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
print len(come)
csvfile = file('../data20000/10299_20151123_20151127.csv', 'rb')
reader = csv.reader(csvfile)
data = list()
for line in reader:
	data.append(line)
csvfile.close()
for line in data:
	if line[0] in idlist and int(line[3]) < 1448380800:
		come.append(line)
print len(come)
filename = ['10299_20151125_20151202_20000', '10299_20151203_20151212_20000', '10299_20151213_20151222_20000', '10299_20151223_20151231_20000']
for fn in filename:	
	csvfile = file('../data20000/' + fn + '.csv', 'rb')
	reader = csv.reader(csvfile)
	data = list()
	for line in reader:
		data.append(line)
	csvfile.close()
	come.extend(data[1:])
	print len(come)
sep.append(len(come))

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
	print len(come)
sep.append(len(come))

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
	print len(come)
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
	for i in len(come):
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
