a=open('24(13).txt').readline()
c=0
bykva=''
for i in sorted('QWERTYUIOPASDFGHJKLZXCVBNM'):
    if a.count('A'+i)>c:
         c=a.count('A'+i)
         bykva=i
print(bykva)