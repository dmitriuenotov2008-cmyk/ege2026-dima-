f=open('24(12).txt').readline().split('A')
c=[]
for i in f:
    if i.count('E')>=3:
        c.append(i)
print(len(max(c)))