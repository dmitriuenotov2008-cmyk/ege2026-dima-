a=open('24(13).txt').readline().split('A')
c=0
for i in range(len(a)):
    c=max(len(a[i-1])+len(a[i])+1,c)
print(c)