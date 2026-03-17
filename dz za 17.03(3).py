for i in range(110203,110246):
    c=[]
    for delit in range(1,i+1,):
        if i%delit==0 and delit%2==0:
            c.append(delit)
            if len(c)==4:
                print(c[0],c[1],c[2],c[3])