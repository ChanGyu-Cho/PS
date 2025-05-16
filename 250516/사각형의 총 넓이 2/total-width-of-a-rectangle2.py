n = int(input())
X1, Y1, X2, Y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    X1.append(a)
    Y1.append(b)
    X2.append(c)
    Y2.append(d)

# Please write your code here.

coor = [[0 for _ in range(1000)] for _ in range(1000)]

for x1,y1,x2,y2 in zip(X1, Y1, X2, Y2):
    for i in range(x1,x2):
        for j in range(y1,y2):
            coor[i][j] +=1

count=0
for i in coor:
    for j in i:
        if(j>=1):
            count+=1
print(count)