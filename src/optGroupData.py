from lmfit import minimize, Parameters, Parameter, report_fit
import numpy as np
import SIRd
import random

def singleImpulse(seq,threshold=10):
    lambdaval=0
    deltaval=-1
    for i in range(1,len(seq)):
        d=seq[i]-seq[i-1]
        if(d>threshold and d>0.2*seq[i-1] and d>lambdaval):
            lambdaval=d
            deltaval=i
    return [lambdaval,deltaval]

def multiImpulse(seq, threshold=10):
    lambdaval = list()
    deltaval = list()
    for i in range(1, len(seq)):
        d = seq[i] - seq[i-1]
        if d > threshold and d > 0.2 * seq[i-1]:
            lambdaval.append(d)
            deltaval.append(i)
    return [lambdaval, deltaval,len(lambdaval)]

def params2fcnval(params,nsteps,mode):
    beta=params['beta'].value
    G=params['G'].value
    n=params['n'].value
    if mode == 5:
        eps = params['eps'].value
        res = SIRd.SpikeM(beta, G, n nsteps, eps)
        return res
    if mode == 4:
        res = SIRd.SI(beta, G, n, nsteps)
        return res
    gamma=params['gamma'].value
    if mode == 3:
        res = SIRd.SIRd(gamma, 0, beta, G, n, nsteps)
        return res
    alpha=params['alpha'].value
    if mode == 2:
        res = SIRd.SIRd(gamma, alpha, beta, G, n, nsteps)
        return res    
    lambdaval=params['lambdaval'].value
    deltaval=params['delta'].value
    res=SIRd.SIRdecayImpulse(gamma,alpha,beta,G,n,nsteps,lambdaval,deltaval)
    return res

def fcn2minSingleImpulse(params,x,data,mode):
    x1=x[0]
    x2=x[1]
    #Predict People
    nsteps=max(max(x1),max(x2))+1
    #nsteps=max(max(x1),max(x2))+11

    res=params2fcnval(params,nsteps,mode)
    plist=list()
    nlist=list()
    if mode < 4:
        for i in x1:
            plist.append(res[0][int(i)])
        for i in x2:
            nlist.append(res[2][int(i)])
        model=np.array(plist+nlist)
        d1=list(data[0])
        d2=list(data[1])
        data_f=np.array(d1+d2)
    else:
        for i in x1:
            plist.append(res[0][int(i)])
        model = np.array(plist)
        d1 = np.array(data[0])
        d2 = np.array(data[1])
        data_f = d1 - d2
    try:
        return model-data_f
    except:
        print model
        print data_f
        print res
        return

def params2fcnvalMulti(params,nsteps,peaks):
    beta=params['beta'].value
    alpha=params['alpha'].value
    gamma=params['gamma'].value
    G=params['G'].value
    n=params['n'].value
    lambdaval=list()
    deltaval=list()
    for i in range(peaks):
        if len(params) - 5 < 2 * (i + 1):
            break
        lambdaval.append(params['lambdaval'+str(i)].value)
        deltaval.append(params['delta'+str(i)].value)
    #nsteps=x.max()+1
    res=SIRd.SIRdecayMultiImpulse(gamma,alpha,beta,G,n,nsteps,lambdaval,deltaval)
    return res

def fcn2minMultiImpulse(params,x,data,peaks):
    x1=x[0]
    x2=x[1]
    #Predict People
    nsteps=max(max(x1),max(x2))+1
    #nsteps=max(max(x1),max(x2))+11
    #print nsteps

    res=params2fcnvalMulti(params,nsteps,peaks)
    plist=list()
    nlist=list()
    for i in x1:
        plist.append(res[0][int(i)])
    for i in x2:
        nlist.append(res[2][int(i)])
    model=np.array(plist+nlist)
    d1=list(data[0])
    d2=list(data[1])
    data_f=np.array(d1+d2)
    try:
        return model-data_f
    except:
        print model
        print data_f
        print res
        return

def optimize(rawdata, mode):

    x=np.array([rawdata[0],rawdata[2]])
    data=np.array([rawdata[1],rawdata[3]])
    seq=rawdata[1]
    
    #Single Impulse
    if mode == 1:
        [lambdaval,deltaval]=singleImpulse(rawdata[1],10)
        if deltaval > -1:
            deltaval=rawdata[0][deltaval]
    #Multi Impulse Begin
    if mode == 0:
        [lambdaval, deltaval, peaks] = multiImpulse(rawdata[1], 10)
        for i in deltaval:
            if i > -1:
                i = rawdata[0][i]
    #Multi Impulse End
    Gmin=int(max(data[0]))
    ninit=data[0][0]
    params=Parameters()
    if mode < 3:
        params.add('alpha',value=0.3,min=0.0)
    params.add('beta',value=0.05,min=0.0)
    if mode < 4:
        params.add('gamma',value=0.05,min=0.0,max=1.0)
    params.add('G',value=2*Gmin,min=Gmin,max=100000)
    params.add('n',value=ninit,vary=False)
    
    #SpikeM
    if mode == 5:
        params.add('eps', value=0.0, min=0.0)

    #Single Impulse
    if mode == 1:
        params.add('lambdaval',value=lambdaval,min=0,max=lambdaval+1)
        params.add('delta',value=deltaval,vary=False)
    
    #Multi Impulse Begin
    if mode == 0:
        if peaks > 5:
            print 'Too many peaks.(' + str(peaks) + ')'
        for i in range(peaks):
            params.add('lambdaval'+str(i), value=lambdaval[i], min=0, max=lambdaval[i]+1)
            params.add('delta'+str(i), value=deltaval[i], vary=False)
    #Multi Impulse End
    #print x
    #print data
    
    #Single Impulse
    if mode > 0:
        result=minimize(fcn2minSingleImpulse,params,args=(x,data,mode))
    else:
    #Multi Impulse
        result=minimize(fcn2minMultiImpulse,params,args=(x,data,peaks))
    return result
