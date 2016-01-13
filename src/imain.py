#!/usr/bin/env python
#!/usr/bin/python

"""
   Interactive main routine, for the Glass-Mackey delay differential equation.
   Allows for tweaking of the input parms (alpha, beta etc)
"""

try:
    from pylab import *
    from matplotlib.widgets import Slider, Button
except:
    print "can not find pylab - get it from http://matplotlib.sourceforge.net/"
    raise
try:
    import GM
except:
    print "can not find GM.py - try svn update, or christos@cs.cmu.edu "
    raise

# import sys
import loadGroupData

xinit=40
# alpha=0.1
# beta=0.2
#G=200
duration=1
# nsteps=10
# n=10

def myfun(myg,mya,myb,myG,myn,mysteps,mylambda,mydelta):
    mys=GM.gmImpulse(gamma=myg,alpha=mya,beta=myb, \
                 xinit=xinit, G=myG, \
		 duration=duration,n=myn, \
		 nsteps=mysteps,lambdaval=mylambda,deltaval=mydelta)
    return(mys)

ax = subplot(111)
# subplots_adjust(left=0.25, bottom=0.25)
subplots_adjust(bottom=0.35)
gm0=0.05
a0 = 0.5   # alpha default
b0 = 0.05   # beta default
G0=300  # matches the Glass-Mackey for white blood cells
n0=10      # matches GM
nsteps0= 50
lambda0=0
delta0=1

s = myfun(gm0,a0,b0,G0,n0,nsteps0,lambda0,delta0)
# create the horizontal axis
t = range(len(s[0]))
print "duration = ", len(s)/nsteps0
#t = [ float(item)/nsteps0 for item in t]
# l, = plot(t,s, lw=2, color='red')
# l = plot(t,s, lw=2, color='red')
data_N=8
data=loadGroupData.load_data(data_N)
t_data=range(len(data[0]))

plot(t_data,data[0],'b+')
plot(t_data,data[1],'r+')

plot(t, s[0], lw=2, color='blue')
plot(t, s[1], lw=2, color='black')
plot(t, s[2], lw=2, color='red')
xlabel("time")
ylabel("value")
ptitle= "Wechat Group g=%2.2f a=%2.2f b=%2.2f init=%2.2f , nsteps=%3d" % \
    (gm0, a0, b0, n0/G0, nsteps0)
title(ptitle)
axis([0, nsteps0, 0, G0+50])

axcolor = 'lightgoldenrodyellow'
axgamma = axes([0.15, 0.15, 0.25, 0.03], axisbg=axcolor)
axalpha = axes([0.15, 0.10, 0.25, 0.03], axisbg=axcolor)
axbeta  = axes([0.15, 0.20, 0.25, 0.03], axisbg=axcolor)
aG =    axes([0.6, 0.20, 0.25, 0.03], axisbg=axcolor)
an =      axes([0.6, 0.15, 0.25, 0.03], axisbg=axcolor)
ansteps = axes([0.6, 0.10, 0.25, 0.03], axisbg=axcolor)
alambda = axes([0.15, 0.25, 0.25, 0.03], axisbg=axcolor)
adelta = axes([0.6, 0.25, 0.25, 0.03], axisbg=axcolor)

sgamma = Slider(axgamma, 'gamma-rRate',  0.01, 0.5, valinit=gm0)
salpha =  Slider(axalpha, 'alpha-decay',  0.0,  2.0, valinit=a0)
sbeta =   Slider(axbeta,  'beta-bRate',   0.01,  0.5, valinit=b0)
sG =    Slider(aG,    'G-total',      1,   500, valinit=G0)
sn =      Slider(an,      'p-init',   1,   500, valinit=n0)
snsteps = Slider(ansteps, 'T-steps',  10, 200, valinit=nsteps0)
slambda = Slider(alambda, 'lambda0',  10, 300, valinit=lambda0)
sdelta = Slider(adelta, 'delta0',  0, 40, valinit=delta0)

def update(val):
    gamma = sgamma.val
    alpha = salpha.val
    beta  = sbeta.val
    G   = sG.val
    n   = min(sn.val,G)
    nsteps= int(snsteps.val)
    lambdaval = int(slambda.val)
    deltaval = int(sdelta.val)
    # re-do the plot
    ax = subplot(111)
    data=loadGroupData.load_data(data_N)
    t_data=range(len(data[0]))
    # clear old plot
    cla()

    yvals=myfun(gamma,alpha,beta,G,n,nsteps,lambdaval,deltaval)
    #t = range(len(yvals))
    #t = [ float(item)/nsteps for item in t]
    t = range(len(yvals[0]))
    # assert len(yvals)==len(t), "unequal lengths for plotting"
    #print '----------------------------'
    #print yvals
    plot(t_data,data[3],'r+')
    plot(t_data,data[1],'b+')
    plot(t,yvals[0], lw=2, color='blue')
    plot(t,yvals[1], lw=2, color='black')
    plot(t,yvals[2], lw=2, color='red')
    ptitle= "Wechat Group g=%2.2f a=%2.2f b=%2.2f init=%2.2f , nsteps=%3d" % \
    (gm0, a0, b0, n0/G0, nsteps0)
    title(ptitle)
    xlabel("time")
    ylabel("value")
    axis([0, nsteps, 0, G+50])
    draw()

sgamma.on_changed(update)
salpha.on_changed(update)
sbeta.on_changed(update)
sG.on_changed(update)
sn.on_changed(update)
snsteps.on_changed(update)
#sphase.on_changed(update)
slambda.on_changed(update)
sdelta.on_changed(update)

resetax = axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor=0.5)
def reset(event):
    sgamma.reset()
    salpha.reset()
    sbeta.reset()
    sG.reset()
    sn.reset()
    snsteps.reset()
    # sphase.reset()
button.on_clicked(reset)

show()

