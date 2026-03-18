f=open('74.txt')
c=[]
for i in f:
    c.append(int(i))
c.sort()
a=[]
lim=8460
s=0
t=0
for j in c:
    if s+j<=lim:
        s+=j
        t+=1
        a.append(j)
print(t,max(a))