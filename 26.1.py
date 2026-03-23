f=open('26(1).txt')
n=f.readline()
st_p=28800
fin_p=50400
zap=[0]*86400
c=0
for i in f:
    nz,finz=map(int,i.split())
    if nz<st_p and finz>st_p:
        c+=1
    if nz>=st_p and nz<=fin_p:
        zap[nz-st_p]+=1
    if finz>=st_p and finz<=fin_p:
        zap[finz-st_p]-=1
m=0
t=0
for i in range(86400):
    c+=zap[i]
    if c>m:
        m=c
        t=0
    if c==m:
        t+=1
print(m,t)