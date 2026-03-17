for n in range(1,30,2):
    for m in range(0,30,2):
        i=2**m*3**n
        if 200000000<=i<=400000000:
            print(i)