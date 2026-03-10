a=0 
for i in range(84052,84131):
    d=0
    for j in range(1,i+1):
        if i%j==0:
            d+=1
    if d>a:
        a=d
        n=i
print(a,n)