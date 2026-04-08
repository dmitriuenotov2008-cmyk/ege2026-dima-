from math import sqrt

f=open('27_A.txt')
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

for y, x in mass:
    if x<92 and y>40:
        clas1.append([x,y])
    else:
        clas2.append([x,y])

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

print(len(clas1),best_sum1)
print(len(clas2),best_sum2)

