f=open('24(11).txt').readline()
m=0
f=f.replace('A','1')
f=f.replace('B','1')
f=f.replace('C','1')
while '11' in f:
    f=f.replace('11', '1 1')
f=f.split()
for i in range(len(f)):
    m=max(m,len(f[i]))
print(m)