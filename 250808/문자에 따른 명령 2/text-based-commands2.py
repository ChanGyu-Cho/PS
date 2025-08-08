dirs = input()

# Please write your code here.

dx,dy = [1,0,-1,0], [0,1,0,-1]  # 북쪽은 1, +는 반시계회전
d=1
x,y= 0,0

for dir in dirs:
    if dir =="L":   # 반시계
        d = (d+1)%4
    elif dir == "R":
        d = (d+3)%4
    else:
        x,y = x+dx[d], y+dy[d]
print(x,y)