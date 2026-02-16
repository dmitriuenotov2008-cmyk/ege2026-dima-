s=open('24(564645).txt').readline()
t=0
maxline=[]
for x in range(1,len(s)):
    if (s[x-1]=='C' or s[x-1]=='D' or s[x-1]=='F') and (s[x]=='A' or s[x]=='O'):
        t+=1
        maxline.append(t)
print(max(maxline))
