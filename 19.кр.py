def game(s,h):
    if h==3 and s>=38:
        return 1
    elif h<3 and s>=38:
        return 0
    elif h==3 and s<38:
        return 0
    else:
        if h%2==0:
            return game(s+1,h+1) or game(s*3,h+1)
        else:
            return game(s+1,h+1) or game(s*3,h+1)
for i in range(1,38):
    if game(i,1)==1:
        print(i)
        break