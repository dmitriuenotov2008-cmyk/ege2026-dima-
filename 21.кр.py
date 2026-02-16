def game1(s,h):
    if (h==3 or h==5) and s>=38:
        return 1
    elif h<5 and s>=38:
        return 0
    elif h==5 and s<38:
        return 0
    else:
        if h%2==0:
            return game1(s+1,h+1) or game1(s*3,h+1)
        else:
            return game1(s+1,h+1) and game1(s*3,h+1)

def game2(s,h):
    if h==3 and s>=38:
        return 1
    elif h<3 and s>=38:
        return 0
    elif h==3 and s<38:
        return 0
    else:
        if h%2==0:
            return game2(s+1,h+1) or game2(s*3,h+1)
        else:
            return game2(s+1,h+1) and game2(s*3,h+1)
for i in range(1,38):
    if game1(i,1)==1:
        print(i)
print('qewrqwerqwerq')
for j in range(1,38):
    if game2(j,1)==1:
        print(j)