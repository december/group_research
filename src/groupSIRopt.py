import loadGroupData
import optGroupData
import disGroupData
from lmfit import report_fit

traindays = 20
begin = 0
end = 135621
mode = 0 #[0, 1, 2, 3, 4, 5] for [multi, single, SIRd, SIR, SI, SpikeM]
name = ['multi', 'single', 'SIRd', 'SIR', 'SI']

fw=open('../../' + name[mode] + '_res/params.csv','w')
for i in range(begin, end):
    rawdata=loadGroupData.load_data(i)
    result=optGroupData.optimize(rawdata, mode)
    report_fit(result.params)
    fw.write(str(i)+',')
    fw.write(str(result.params))
    fw.write('\n')
    path='../../'+name[mode]+'/'
    #disGroupData.display_bi(rawdata,result,result_test,path+str(i)+'.png')
    p = disGroupData.display(rawdata,result,path+str(i)+'.png',mode)
    if peaks.has_key(p):
        peaks[p] += 1
    else:
        peaks[p] = 1
    print 'No.' + str(i) + ' items finished.('+name[i]+')'
fw.close()
print peaks
