f=open('24(7).txt').readline().split('D')
m=0
s=0
for x in range(len(f)):
    if f[x].count('O')<=2:
        s+=len(f[x])
        m=max(m,s)
    else:
        s=1
print(m)
