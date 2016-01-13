import loadGroupData
import optGroupData
import disGroupData
import SIRd
import csv
import numpy
from scipy import stats

def getCurve(p, flag):
	p = [float(k) for k in p]
	t = SIRd.SIRdecayImpulse(p[2], p[0], p[1], p[3], p[4], 40, p[5], p[6])
	#s = [k/p[3] for k in t[flag]]
	return t[flag]

csvfile = file('../lyf_res/simpleParams.csv', 'rb')
reader = csv.reader(csvfile)
params = list()
for line in reader:
	params.append(line)
test = list()
for i in range(2022):
	#print i
	rawdata = loadGroupData.load_data(i)
	come = numpy.array(rawdata[1])
	go = numpy.array(rawdata[3])
	result = list()
	#res = getCurve(params[i], 0)
	temp = stats.ks_2samp(come, getCurve(params[i], 0))
	result.append(temp)
	if i < 20:
		print temp
		print come
	temp = stats.ks_2samp(go, getCurve(params[i], 2))
	result.append(temp)
	test.append(result)
csvwrite = file('../lyf_res/kstest.csv', 'wb')
writer = csv.writer(csvwrite)
writer.writerows(test)
csvwrite.close()
print 'Finished.'
