import loadGroupData
import optGroupData
import disGroupData
from lmfit import report_fit
import csv

def getItem(order, mode):
	rawdata = loadGroupData.load_data(i)
	result = optGroupData.optimize(rawdata, mode)
	return str(result.params)

mode = 4
name = ['multi', 'single', 'sird', 'sir', 'si']
f = open('../../rawresult/'+name[mode]+'.csv', 'r')
data = f.readlines()
f.close()
fw = open('../../rawresult/'+name[mode]+'Params.csv', 'w')
count = 0
for i in range(len(data)):
	if i == 27980:
		for j in range(27980, 27993):
			s = getItem(j, mode)
			#print s
			fw.write(s)
			fw.write('\n')
			count += 1
		continue
	if i == 104169:
		for j in range(104181, 104188):
			s = getItem(j, mode)
			fw.write(s)
			fw.write('\n')
			count += 1
		continue
	if i == 131805:
		for j in range(131823, 131837):
			s = getItem(j, mode)
			fw.write(s)
			fw.write('\n')
			count += 1
		continue
	#print data[i]
	fw.write(data[i])
	count += 1
fw.close()
print count
print 'Finished'
