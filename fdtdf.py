# cording: utf-8
# Finate-defference time domein method
# Sound field analysis
# by Dr.H. Yamazaki
# June 7th 2020

from pylab import *
from scipy import *
from matplotlib import cm

X=40
Y=30
dx=1.0
dy=1.0
f=1000.0
dt=1/f
ro=1.21
C=343.0
K=ro*C*C
ro1=2.3		# concrete
Z=ro1*C
N=5000

Q = 0.5+0.5*cos(arange(-pi,pi,2*pi*dt))
#Q = rand(N)
n=len(Q)
t=arange(0,n*dt,dt)

P=zeros((X,Y),"float64")
ux=zeros((X+1,Y),"float64")
uy=zeros((X,Y+1),"float64")

mic=[]
for n in range(N):
    if n<len(Q):
        P[20,15] += Q[n]

    mic.append(P[1,1])

    ux[1:X,:]=ux[1:X,:]-dt/ro/dx*(P[1:X,:]-P[0:X-1,:])

    uy[:,1:Y]=uy[:,1:Y]-dt/ro/dy*(P[:,1:Y]-P[:,0:Y-1])

    ux[0,:]=-P[0,:]/Z
    ux[X,:]=P[X-1,:]/Z

    uy[:,0]=-P[:,0]/Z
    uy[:,Y]=P[:,Y-1]/Z

    P[:X,:Y]=P[:X,:Y]-K*dt/dx*(ux[1:X+1,:]-ux[:X,:])-K*dt/dy*(uy[:,1:Y+1]-uy[:,:Y])

figure(1)
plot(Q,'-k')
xlabel('time[s]')
ylabel('Rerative sound pressure')
grid()
show()

figure(2)
contourf(P.T,aspect="equal", cmap=cm.jet)
xlim(0,X-1)
ylim(0,Y-1)
xlabel('X sample')
ylabel('Y sample')
show()

