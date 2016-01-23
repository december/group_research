import loadGroupData
import optGroupData
import disGroupData
from lmfit import report_fit


fw=open('../lyf_res/params.csv','w')
peaks = {}
for i in range(2023):
    rawdata=loadGroupData.load_data(i)
    testdata=loadGroupData.load_test_data(i)
    result=optGroupData.optimize(rawdata)
    #result_test=optGroupData.optimize(testdata)
    report_fit(result.params)
    fw.write(str(result.params))
    fw.write('\n')
    path='../lyf_res/'
    #disGroupData.display_bi(rawdata,result,result_test,path+str(i)+'.png')
    p = disGroupData.display(rawdata,result,path+str(i)+'.png')
    if peaks.has_key(p):
        peaks[p] += 1
    else:
        peaks[p] = 1
fw.close()
print peaks