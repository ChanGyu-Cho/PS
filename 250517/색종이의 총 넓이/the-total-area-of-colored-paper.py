N = int(input())
X =[]
Y =[]
for _ in range(N):
    x,y = map(int, input().split())
    X.append(x)
    Y.append(y)

coor = [[0 for _ in range(1000)] for _ in range(1000)]

for x,y in zip(X,Y):
    for i in range(x, x+8):
        for j in range(y, y+8):
            coor[i][j] +=1
count =0
for line in coor:
    for block in line:
        if(block >=1):
            count +=1
print(count)