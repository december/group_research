import loadGroupData
import optGroupData
import disGroupData
import SIRd
import csv
import numpy

def getRes(p, real, kind):
	unitmae = list()
	unitrmse = list()
	beta = p['beta'].value
	G = p['G'].value
	n = p['n'].value
	index = len(real[0]) - 1
	#print index
	if real[1][index] - real[3][index] <= 0:
		return unitmae, unitrmse
	if kind == 0:
		res = SIRd.SI(beta, G, n, index+1)
	if kind == 1:
		gamma = p['gamma'].value
		res = SIRd.SIRd(gamma, 0, beta, G, n, index+1)
	if kind == 2:
		gamma = p['gamma'].value
		alpha = p['alpha'].value
		res = SIRd.SIRd(gamma, alpha, beta, G, n, index+1)
	if kind == 3:
		gamma = p['gamma'].value
		alpha = p['alpha'].value
		lambdaval=p['lambdaval'].value
		deltaval=p['delta'].value
		res = SIRd.SIRdecayImpulse(gamma, alpha, beta, G, n, index+1, lambdaval, deltaval)
	if kind == 4:
		gamma = p['gamma'].value
		alpha = p['alpha'].value
		lambdaval = list()
		deltaval = list()
		count = 0
		while 2 * (count + 1) + 5 <= len(p):
			lambdaval.append(p['lambdaval'+str(count)].value)
			deltaval.append(p['delta'+str(count)].value)
			count += 1
		res = SIRd.SIRdecayMultiImpulse(gamma, alpha, beta, G, n, index+1, lambdaval, deltaval)

	#print index
	#print len(res[0])
	temp = abs(res[0][index] - real[1][index])
	unitmae.append(temp)
	temp = temp * 1.0 / real[1][index]
	unitrmse.append(temp)

	temp = abs(res[1][index] - (real[1][index] - real[3][index]))
	unitmae.append(temp)
	temp = temp * 1.0 / (real[1][index] - real[3][index])
	unitrmse.append(temp)

	temp = abs(res[2][index] - real[3][index])
	unitmae.append(temp)
	if real[3][index] != 0:
		temp = temp * 1.0 / real[3][index]
	unitrmse.append(temp)

	return unitmae, unitrmse

mrfile = list()
csvfile = file('../si_res/simpleParams.csv', 'rb')
reader = csv.reader(csvfile)
params = list()
for line in reader:
	params.append(line)
csvfile.close()
csvfile = file('../../badID.csv', 'rb')
reader = csv.reader(csvfile)
badID = list()
for line in reader:
	badID.append(int(line[0]))
csvfile.close()
mae = list()
rmse = list()
for i in range(3):
	mae.append(list())
	rmse.append(list())
fw = open('SIFront.csv', 'w')
error = 0
for i in range(2022):
	if i in badID:
		print '!' + str(i)
		continue
	print i
	rawdata = loadGroupData.load_data(i)
	front = list()
	for j in range(4):
		front.append(rawdata[j][:-10])
	result = optGroupData.optimize(front)
	m, r = getRes(result.params, rawdata, 0)
	if len(m) == 0:
		error += 1
		continue
	temp = list()
	temp.append(m)
	temp.append(r)
	mrfile.append(temp)
	fw.write(str(result.params))
	fw.write('\n')
	for j in range(3):
		mae[j].append(m[j])
		rmse[j].append(r[j])
fw.close()
print error
csvwrite = file('SIPredictPeople.csv', 'wb')
writer = csv.writer(csvwrite)
writer.writerows(mrfile)
csvwrite.close()
for i in range(3):
	print sum(mae[i]) / len(mae[i])
	print sum(rmse[i]) / len(rmse[i])

print 'Finished'
