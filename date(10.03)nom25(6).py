from fnmatch import *
for i in range (0, 10**10, 4891):
    if fnmatch(str(i),'1?2711*0'):
        print(i)