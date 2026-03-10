c=0
i=600001
while c<5:
    for j in range(17,i):
        if i%j==0 and j%10==7:
            print(i,j)
            c+=1
            break
    i+=1