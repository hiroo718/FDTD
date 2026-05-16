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
dx=1
dy=1
f=1000.0
dt=1/f
ro=1.21
C=343
K=ro*C*C
Z=7.8*C*C
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

    mic.append(P[0,0])

    for x in range(X-1):
        for y in range(Y):
            ux[x+1,y]=ux[x+1,y]-dt/ro/dx*(P[x+1,y]-P[x,y])

    for x in range(X):
        for y in range(Y-1):
            uy[x,y+1]=uy[x,y+1]-dt/ro/dy*(P[x,y+1]-P[x,y])

    for j in range(Y):
        ux[0,j]=-P[0,j]/Z
        ux[X,j]=P[X-1,j]/Z
    for i in range(X):
        uy[i,0]=-P[i,0]/Z
        uy[i,Y]=P[i,Y-1]/Z

    for x in range(X):
        for y in range(Y):
            P[x,y]=P[x,y]-K*dt/dx*(ux[x+1,y]-ux[x,y])-K*dt/dy*(uy[x,y+1]-uy[x,y])

figure(1)
plot(P,'-k')
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

