f=open('24.txt').readline()
k=0
s=0
m=0
for i in range(0, len(f)):
    if f[i]=="C":
        k+=1
    if (f[i]!="A") and (i!=len(f)):
        s+=1
    elif k>=3:
        m=max(s,m)
        s=0
        k=0
    else:
        s=0
        k=0
print(m)