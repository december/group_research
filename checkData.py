import csv

csvfile = file('selected_group_behavior.csv', 'rb')
reader = csv.reader(csvfile)
count = 0;
data = list()
idlist = list()
for line in reader:
	data.append(line)
lastid = -1
lasttime = -1
for line in data:
	if line[0] == lastid:
		if int(line[3]) < int(lasttime):
			print "Time Error."
			print line
			print int(line[3])
			print int(lasttime)
		lasttime = line[3]
	else:
		if line[0] in idlist:
			print "Id Error."
		if int(line[3]) != 0:
			count += 1
			print "Initial Error."
			print line
		idlist.append(line[0])
		lastid = line[0]
		lasttime = line[3]
print "Finished."
fw = open('idset.csv', 'w')
for i in idlist:
	fw.write(i)
	fw.write('\n')
fw.close()
print count
print len(idlist)
