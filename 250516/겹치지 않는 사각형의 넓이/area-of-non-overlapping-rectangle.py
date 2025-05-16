x1 = [0] * 3
y1 = [0] * 3
x2 = [0] * 3
y2 = [0] * 3

x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())
x1[2], y1[2], x2[2], y2[2] = map(int, input().split())

# Please write your code here.

coor = [[0 for _ in range(1000)] for _ in range(1000)]

for i in range(2):
    for x in range(x1[i], x2[i]):
        for y in range(y1[i], y2[i]):
            coor[x][y] +=1

for x in range(x1[2], x2[2]):
        for y in range(y1[2], y2[2]):
            coor[x][y] -=1

count =0
for line in coor:
    for block in line:
        if(block >0):
            count +=1
print(count)
