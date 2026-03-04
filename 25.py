def f(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    return n > 1
m=1474999
c=0
while c<5:
    s=0
    for i in range(2,int(m**0.5)+1):
        if m%i==0:
            if f(i):
                s += i
            if i != m//i and f(m//i):
                s+=m//i
    if 0 <s<=42000 and s%6==0:
        print(m)
        c+=1
    m-=1