import loadGroupData
import optGroupData
import disGroupData
from lmfit import report_fit


fw=open('../../sird_res/params.csv','a')
peaks = {}
for i in range(75684, 135672):
    rawdata=loadGroupData.load_data(i)
    testdata=loadGroupData.load_test_data(i)
    result=optGroupData.optimize(rawdata)
    #result_test=optGroupData.optimize(testdata)
    report_fit(result.params)
    fw.write(str(result.params))
    fw.write('\n')
    path='../../sird_res/'
    #disGroupData.display_bi(rawdata,result,result_test,path+str(i)+'.png')
    p = disGroupData.display(rawdata,result,path+str(i)+'.png')
    if peaks.has_key(p):
        peaks[p] += 1
    else:
        peaks[p] = 1
    print 'No.' + str(i) + ' items finished.(SIRd)'
fw.close()
print peaks
