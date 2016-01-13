import loadGroupData
import optGroupData
import disGroupData
from lmfit import report_fit
import csv

csvfile = file('../../usefulID.csv', 'rb')
reader = csv.reader(csvfile)
data = list()
for line in reader:
	data.append(line)
csvfile.close()
csvfile = file('../../badID.csv', 'rb')
reader = csv.reader(csvfile)
baddata = list()
for line in reader:
	baddata.append(line)
csvfile.close()
fw = open('../multi_predict/params.csv','w')
for line in data:
	flag = False
	for per in baddata:
		if line[0] == per[0]:
			flag = True
			break
	if flag:
		continue
	index = int(line[0])
	rawdata = loadGroupData.load_data(index)
	front = list()
	for i in range(4):
		front.append(rawdata[i][:-10])
	result=optGroupData.optimize(front)
	report_fit(result.params)
	fw.write(str(result.params))
	fw.write('\n')
	path='../multi_predict/'
	p = disGroupData.display(rawdata,result,path+line[0]+'.png')
fw.close()
print 'Finished.'
