f=open('1_24(3).txt').readline()
k=0
minline=[]
for x in range(1,len(f)-1):
    if f[x]+f[x+1]=="TT":
        k+=1
        if k==150:
            minline.append(x)
print(minline)