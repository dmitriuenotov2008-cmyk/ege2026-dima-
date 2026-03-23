f=open("26_1(1).txt")
n=int(f.readline())
a=1633305600
b=a+604800
c=0
d=[0]*604801
for i in f:
    x,y=map(int,i.split())
    if x<a and (y>a or y==0): 
        c+=1
    if x >= a and x <= b:
        d[x-a]+=1
    if y != 0 and y >= a and y <= b:
        d[y-a]-=1
m=0
t=0
for i in range(604801):
    c+=d[i]
    if c>m: 
        m=c
        t=0
    if c==m: 
        t+=1
print(m,t)