from lmfit import minimize, Parameters, Parameter, report_fit
import numpy as np
import pylab
import optGroupData
import matplotlib.pyplot

def display(rawdata,result,path):
    x=np.array([rawdata[0],rawdata[2]])
    data=np.array([rawdata[1],rawdata[3]])
    Tdis=40
    xdis=range(Tdis)
    
    #Single Impulse
    res=optGroupData.params2fcnval(result.params,Tdis)
    peaks = 1
    '''
    #Multi Impulse begin
    [lambdaval, deltaval, peaks] = optGroupData.multiImpulse(rawdata[1], 10)
    res=optGroupData.params2fcnvalMulti(result.params, Tdis, peaks)
    #Multi Impulse end
    '''
    final=res[0]
    nlist=res[2]
    fig=matplotlib.pyplot.figure()
    pylab.plot(x[0], data[0], 'k+')
    pylab.plot(x[1], data[1], 'b+')
    pylab.plot(xdis, final, 'r')
    pylab.plot(xdis, nlist, 'b')
    pylab.savefig(path)
    #Multi Impulse begin
    return peaks
    #Multi Impulse end

def display_bi(rawdata,result1,result2,path):
    x=np.array([rawdata[0],rawdata[2]])
    data=np.array([rawdata[1],rawdata[3]])
    #xx=np.array([testdata[0],testdata[2]])
    #testdata=np.array([testdata[1],testdata[3]])
    Tdis=40
    xdis=range(Tdis)
    res=optGroupData.params2fcnval(result1.params,Tdis)
    res2=optGroupData.params2fcnval(result2.params,Tdis)
    final=res[0]
    nlist=res[2]
    f2=res2[0]
    n2=res2[2]
    fig=matplotlib.pyplot.figure()
    pylab.plot(x[0], data[0], 'k+')
    pylab.plot(x[1], data[1], 'b+')
    pylab.plot(xdis, final, 'r')
    pylab.plot(xdis, nlist, 'b')
    pylab.plot(xdis, f2, 'k')
    pylab.plot(xdis, n2, 'k')
    pylab.savefig(path)


