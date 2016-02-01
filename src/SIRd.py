def SI(beta=0.05, G=200, n=40, nsteps=100):
    totSteps = nsteps
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
    myRes=list()
    At[0]=Pt[0]-Nt[0]
    for t in range(1,totSteps):
        S=G-Pt[t-1]
        pseq[t]=S*beta*At[t-1]/G
        Pt[t]=Pt[t-1]+pseq[t]
        aseq[t]=pseq[t]
        At[t]=At[t-1]+pseq[t]
    myRes.append(Pt)
    myRes.append(At)
    myRes.append(Nt)
    return(myRes)



def SIRd(gamma=0.05, alpha=1.0, beta=0.05, G=200, n=40, nsteps=100):
    totSteps=nsteps
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
    myRes=list()
    #qt[0]=gamma
    for i in range(0,totSteps):
        qt[i]=gamma*((i+2)**(1-alpha)-(i+1)**(1-alpha))/(1-alpha)
    #print qt
    Nt[0]=n*qt[0]
    At[0]=Pt[0]-Nt[0]
    aseq[0]=At[0]
    for t in range(1,totSteps):
        S=G-Pt[t-1]
        pseq[t]=S*beta*At[t-1]/G
        Pt[t]=Pt[t-1]+pseq[t]
        aseq[t]=pseq[t]
        for j in range(0,t):
            tmp=aseq[j]*qt[t-j]
            aseq[j]=aseq[j]-tmp
            nseq[t]=nseq[t]+tmp
        Nt[t]=Nt[t-1]+nseq[t]
        At[t]=At[t-1]+pseq[t]-nseq[t]

    myRes.append(Pt)
    myRes.append(At)
    myRes.append(Nt)
    #print Pt
    #print At
    #print Nt
    return(myRes)


    #print yvals

def SIRdecayImpulse(gamma=0.05, alpha=1.0, beta=0.05, G=200, n=40, nsteps=100, lambdaval=0, deltaval=1):
    totSteps=nsteps
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
    myRes=list()
    #qt[0]=gamma
    for i in range(0,totSteps):
        qt[i]=gamma*((i+2)**(1-alpha)-(i+1)**(1-alpha))/(1-alpha)
    #print qt
    Nt[0]=n*qt[0]
    At[0]=Pt[0]-Nt[0]
    aseq[0]=At[0]
    for t in range(1,totSteps):
        S=G-Pt[t-1]
        pseq[t]=S*beta*At[t-1]/G+lambdaval*(t==deltaval)
        Pt[t]=Pt[t-1]+pseq[t]
        aseq[t]=pseq[t]
        for j in range(0,t):
            tmp=aseq[j]*qt[t-j]
            aseq[j]=aseq[j]-tmp
            nseq[t]=nseq[t]+tmp
        Nt[t]=Nt[t-1]+nseq[t]
        At[t]=At[t-1]+pseq[t]-nseq[t]

    myRes.append(Pt)
    myRes.append(At)
    myRes.append(Nt)
    return(myRes)

def SIRdecayMultiImpulse(gamma=0.05, alpha=1.0, beta=0.05, G=200, n=40, nsteps=100, lambdaval=list(), deltaval=list()):
    totSteps=nsteps
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
    myRes=list()
    #qt[0]=gamma
    for i in range(0,totSteps):
        qt[i]=gamma*((i+2)**(1-alpha)-(i+1)**(1-alpha))/(1-alpha)
    #print qt
    Nt[0]=n*qt[0]
    At[0]=Pt[0]-Nt[0]
    aseq[0]=At[0]
    for t in range(1,totSteps):
        S=G-Pt[t-1]
        pseq[t]=S*beta*At[t-1]/G
        for order in range(len(deltaval)):
            if t == deltaval[order]:
                pseq[t] += lambdaval[order]
        Pt[t]=Pt[t-1]+pseq[t]
        aseq[t]=pseq[t]
        for j in range(0,t):
            tmp=aseq[j]*qt[t-j]
            aseq[j]=aseq[j]-tmp
            nseq[t]=nseq[t]+tmp
        Nt[t]=Nt[t-1]+nseq[t]
        At[t]=At[t-1]+pseq[t]-nseq[t]

    myRes.append(Pt)
    myRes.append(At)
    myRes.append(Nt)
    return(myRes)


    #print yvals

