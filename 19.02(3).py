f=open('24_59848.txt').readline()
alf='0123456789ABCDEFGHIJKLMN'
c=0
a=0
for i in range(1,len(f)):
    if f[i] in alf:
        c+=1
        if c>a:
            a=c
    else:
        c=0
a=max(c,a)
print(a)