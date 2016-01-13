import csv

csvfile = file('selected_group_behavior.csv', 'rb')
reader = csv.reader(csvfile)
data = list()
for line in reader:
	data.append(line)
lastid = -1
day = 86400
prefix = 'SIRdecayImpulse/group_data_lyf/'
suffix = '.csv'
unitdata = list()
for line in data:
	if line[0] != lastid:
		if lastid != -1:
			daylist.append(date)
			comelist.append(come)
			golist.append(go)
			while (date < 30):
				date += 1
				daylist.append(date)
				comelist.append(come)
				golist.append(go)
			unitdata.append(daylist)
			unitdata.append(comelist)
			unitdata.append(daylist)
			unitdata.append(golist)
			csvwrite = file(prefix + lastid + suffix, 'wb')
			writer = csv.writer(csvwrite)
			writer.writerows(unitdata)
			csvwrite.close()
			'''
			for i in unitdata:
				fw.write(i)
				fw.write('\n')
			fw.close()
			'''	
			unitdata = list()
		date = 0
		come = 0
		go = 0
		daylist = list()
		comelist = list()
		golist = list()
		lastid = line[0]
	while (int(line[3]) > (date + 1) * day):
		daylist.append(date)
		comelist.append(come)
		golist.append(go)
		date += 1
	if int(line[4]) == 4:
		go += 1
	else:
		come += 1
print 'Finished'
