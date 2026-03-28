f = open('26(3).txt')
N,K = map(int,f.readline().split())
cells = []
for i in range(N):
    price = int(f.readline())
    cells.append([price,i+1,0])
cells.sort()
r = []
for i in range(K):
    start,duration = map(int,f.readline().split())
    r.append([start,duration])
r.sort()
t = 0
l = 0
for re in r:
    start = re[0]
    duration = re[1]
    if start >= 18*60:
        break
    for cell in cells:
        if cell[2] <= start:
            t += cell[0]
            l = cell[1]
            cell[2] = start+duration
            break
print(t,l)