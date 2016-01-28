import loadGroupData
import optGroupData
import disGroupData
from lmfit import report_fit

traindays = 20  #how many days used to train
begin = 0    #start with which group
end = 135621    #end with which group
mode = 0 #[0, 1, 2, 3, 4] for [multi, single, SIRd, SIR, SI]
name = ['multi', 'single', 'SIRd', 'SIR', 'SI']

fw=open('../../' + name[mode] + '_res/params.csv','w')
for i in range(begin, end):
    rawdata=loadGroupData.load_data(i, traindays)
    result=optGroupData.optimize(rawdata, mode)
    report_fit(result.params)
    fw.write(str(result.params))
    fw.write('\n')
    path='../../'+name[mode]+'/'
    #disGroupData.display_bi(rawdata,result,result_test,path+str(i)+'.png')
    print 'No.' + str(i) + ' items finished.('+name[i]+')'
fw.close()
print peaks