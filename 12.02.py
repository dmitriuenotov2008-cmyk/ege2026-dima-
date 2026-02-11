for x in range(95632,95651):
    k=0
    a=[]
    for i in range(1,x+1):
        if x%i==0:
            if i%2!=0:
                k+=1
                a.append(i)
                if k>6:
                    break
print(a)