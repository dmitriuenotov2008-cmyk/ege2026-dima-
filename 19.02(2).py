f=open('69932.txt').readline()
maxline=[]
for i in range(1,len(f)):
    if not(f[i]=='0'and f[i+1]=='-*'):
        if not(f[i]=='-*'and f[i+1]=='0'):
            if f[i]>0 and f[i+1]=='*':
                if not(f[i]=='-*' and f[i+1]=='-*'):
                    maxline.append#как сделать счетчик символов?