f=open('26(2).txt')
n=int(f.readline())
clients=[]
for line in f:
    t,d,w=map(int, line.split())
    clients.append([t,d,w])
clients.sort()
time1=0
time2=0
len1=0
len2=0
count2=0
lost=0
for t,d,w in clients:
    if t>=time1:
        len1=0
        time1=t
    if t>=time2:
        len2=0
        time2=t
    if w==1:
        use=1
    elif w==2:
        use=2
    else:
        if len1<=len2:
            use=1
        else:
            use=2
    if use==1:
        if len1>=14:
            lost+=1
        else:
            time1+=d
            len1+=1
    else:
        if len2>=14:
            lost+=1
        else:
            time2+=d
            len2+=1
            count2+=1
print(count2,lost)