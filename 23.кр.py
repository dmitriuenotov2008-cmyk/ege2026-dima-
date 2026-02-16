def nom23(x,y):
    if x==y:
        return 1
    elif x>y:
        return 0
    else:
        return nom23(x+1,y)+nom23(x*2,y)+nom23(2*x+1,y)+nom23(x*10,y)
print(nom23(1,15))