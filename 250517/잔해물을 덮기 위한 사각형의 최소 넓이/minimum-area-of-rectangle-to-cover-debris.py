coor = [[0 for _ in range(2002)] for _ in range(2002)]
ax1,ay1,ax2,ay2 = map(int, input().split())
bx1,by1,bx2,by2 = map(int, input().split())
   
for i in range(ax1, ax2):
    for j in range(ay1,ay2):
        coor[i][j] +=1
for i in range(bx1, bx2):
    for j in range(by1,by2):
        coor[i][j] +=2
uponCount=0
if(coor[ax1][ay1]==3):
    uponCount+=1
if(coor[ax1][ay2-1]==3):
    uponCount+=1
if(coor[ax2-1][ay1]==3):
    uponCount+=1
if(coor[ax2-1][ay2-1]==3):
    uponCount+=1

if(uponCount ==1 or uponCount ==0):
    print((ax2-ax1)*(ay2-ay1))
elif(uponCount >=2):
    count=0
    for line in coor:
        for box in line:
            if(box ==1):
                count+=1
    print(count)

