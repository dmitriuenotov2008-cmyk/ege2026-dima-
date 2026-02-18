f=open('1_24.txt').readline()
f=f.replace('Q','X').replace('R','X').replace('W','X').replace('1','9').replace('2','9').replace('4','9')
a=0
for i in range(1,len(f)):
    if f[i-1]!=f[i]:
        a+=1
print(a)