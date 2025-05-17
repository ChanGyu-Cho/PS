N = int(input())
coor = [[0 for _ in range(1000)] for _ in range(1000)]
for i in range(N):
    x1,y1,x2,y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            coor[x][y] =(i%2)+1
count =0
for line in coor:
    for box in line:
        if(box ==2):
            count+=1
print(count)