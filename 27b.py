from math import sqrt

f=open('27_B(1).txt')
n=f.readline()
mass=[]
for line in f:
    parts=line.split()
    nums=[]
    for x in parts:
        x=x.replace(',', '.')
        x=float(x)
        nums.append(x)
    mass.append(nums)

clas1=[]
clas2=[]
clas3=[]

for x, y in mass:
    if x>10 and y<33:
        clas1.append([x,y])
    elif x>10 and y<41 and y>33:
        clas2.append([x,y])
    elif x>10 and y>40:
        clas3.append([x,y])


best_point1=None
best_sum1=float('inf')

for x1, y1 in clas1:
    s1=0
    for x2,y2 in clas1:
        s1+=sqrt((x1 - x2)**2 + (y1 - y2)**2)
    if s1<best_sum1:
        best_sum1=s1
        best_point1=(x1, y1)


best_point2=None
best_sum2=float('inf')

for x1, y1 in clas2:
    s2=0
    for x2,y2 in clas2:
        s2+=sqrt((x1 - x2)**2 + (y1 - y2)**2)
    if s2<best_sum2:
        best_sum2=s2
        best_point2=(x1, y1)


best_point3=None
best_sum3=float('inf')

for x1, y1 in clas3:
    s3=0
    for x2,y2 in clas3:
        s3+=sqrt((x1 - x2)**2 + (y1 - y2)**2)
    if s3<best_sum3:
        best_sum3=s3
        best_point3=(x1, y1)
print(best_point1,best_sum1,best_point2,best_sum2,best_point3,best_sum3)