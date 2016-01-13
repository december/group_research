#!/usr/bin/python
#!/usr/local/bin/python
#!/usr/bin/python22
#
# $Log:$
#


##################
# Implements the Glass-Mackey equation
#      with Euler integration (= simple deltaT)
##############

try:
    import pylab as P
except:
    print "can not find pylab - get it from http://matplotlib.sourceforge.net/"
    raise
import math as M
import sys
from scipy.stats import binom

# the 'P' function of G-M
#     to be applied to the 'delayed' x-value
# see the Eq. 4.26, on page 183, of the book
#     Kaplan and Glass, 'Understanding nonlinear dynamics'

def PGM(y,beta,n):
    # y: number of red blood cells, 'tau' steps ago
    # beta: ~ birth rate
    # n: exponent that controls the steepness of the near-triangular drop
    val = beta* y / (1.0 + pow(y,n))
    return(val)


################################################################
# returns a vector of arange(0.0, float(duration), delta)
# filled in with the values of the Glass-Mackey equation, ready for plotting
# def gm(xinit=1.0, alpha=0.9, beta=0.5, tau=1.0, n=40, duration=10, delta=0.001):

    # xinit	initial value
    # alpha	decay rate
    # beta	~ birth rate
    # tau	delay, in time units
    # n		exponent in Glass-Mackey equation
    # duration	total number of time units
    # nsteps	steps within a time unit: 1/nsteps == delta t

def gm(xinit=1.0, gamma=0.05, alpha=1, beta=0.05, G=200, n=40, duration=1, nsteps=100):
    '''
    pref="	GM: "

    print pref, "xinit=", xinit
    print pref, "alpha=", alpha
    print pref, "beta=", beta
    print pref, "tau=", tau
    print pref, "n=", n
    print pref, "duration=", duration
    print pref, "nsteps per unit time=", nsteps
    '''
    delta = 1.0/nsteps
    #print pref, "delta=", delta
    # myt= P.arange(0.0, float(duration), delta)
    # myx= P.arange(0.0, float(duration), delta)
    totSteps = duration * nsteps
    # myx = P.array(totSteps)
    pseq = [0 for i in range(totSteps)]
    aseq = [0 for i in range(totSteps)]
    nseq = [0 for i in range(totSteps)]
    Pt =  [0 for i in range(totSteps)]
    At =  [0 for i in range(totSteps)]
    Nt =  [0 for i in range(totSteps)]
    qt =  [0 for i in range(totSteps)]
    n=int(n)
    pseq[0]=n
    Pt[0]=n
    At[0]=n

    myRes=list()
    for i in range(1,totSteps):
        qt[i]=gamma*(i)**(-alpha)

    for t in range(1,totSteps):
        S=G-Nt[t-1]-At[t-1]
        pseq[t]=binom.rvs(S,beta*At[t-1]/G);
        Pt[t]=Pt[t-1]+pseq[t]
        aseq[t]=pseq[t]
        for j in range(0,t-1):
            tmp=binom.rvs(aseq[j],qt[t-j])
            aseq[j]=aseq[j]-tmp
            nseq[t]=nseq[t]+tmp
        Nt[t]=Nt[t-1]+nseq[t]
        At[t]=At[t-1]+pseq[t]-nseq[t]

    print Pt
    myRes.append(Pt)
    myRes.append(At)
    myRes.append(Nt)
    return(myRes)
    #return([0 for i in range(totSteps)])

################################################################
'''
if __name__ == "__main__":      # when run as a script
    s=gm(alpha=00.5)
    print s
    print " "
    s=gm(G=2.0, alpha=0.6)
    print s
    print " "
    s=gm(tau=1, alpha=0.6, duration=2, nsteps=1)
    print s
    print " "
    s=gm(tau=20, alpha=0.1, duration=100, nsteps=10)
    print s
'''


def gmImpulse(xinit=1.0, gamma=0.05, alpha=1, beta=0.05, G=200, n=40, duration=1, nsteps=100, lambdaval=0, deltaval=1):
    '''
    pref="	GM: "

    print pref, "xinit=", xinit
    print pref, "alpha=", alpha
    print pref, "beta=", beta
    print pref, "tau=", tau
    print pref, "n=", n
    print pref, "duration=", duration
    print pref, "nsteps per unit time=", nsteps
    '''
    delta = 1.0/nsteps
    #print pref, "delta=", delta
    # myt= P.arange(0.0, float(duration), delta)
    # myx= P.arange(0.0, float(duration), delta)
    totSteps = duration * nsteps
    # myx = P.array(totSteps)
    pseq = [0 for i in range(totSteps)]
    aseq = [0 for i in range(totSteps)]
    nseq = [0 for i in range(totSteps)]
    Pt =  [0 for i in range(totSteps)]
    At =  [0 for i in range(totSteps)]
    Nt =  [0 for i in range(totSteps)]
    qt =  [0 for i in range(totSteps)]
    n=int(n)
    pseq[0]=n
    Pt[0]=n
    At[0]=n

    myRes=list()
    for i in range(1,totSteps):
        qt[i]=gamma*(i)**(-alpha)

    for t in range(1,totSteps):
        S=G-Nt[t-1]-At[t-1]
        pseq[t]=binom.rvs(S,beta*At[t-1]/G)+lambdaval*(t==deltaval);
        Pt[t]=Pt[t-1]+pseq[t]
        aseq[t]=pseq[t]
        for j in range(0,t-1):
            tmp=binom.rvs(aseq[j],qt[t-j])
            aseq[j]=aseq[j]-tmp
            nseq[t]=nseq[t]+tmp
        Nt[t]=Nt[t-1]+nseq[t]
        At[t]=At[t-1]+pseq[t]-nseq[t]

    print Pt
    myRes.append(Pt)
    myRes.append(At)
    myRes.append(Nt)
    return(myRes)
    #return([0 for i in range(totSteps)])

