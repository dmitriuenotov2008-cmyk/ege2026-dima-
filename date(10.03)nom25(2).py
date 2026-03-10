otv=[]
for m in range(1,50):
    for n in range(1,50):
        if m%2==0 and n%2==1:
            n1=2**m*3**n
            if 400000000<=n1<=600000000:
                otv.append(n1)
print(otv)