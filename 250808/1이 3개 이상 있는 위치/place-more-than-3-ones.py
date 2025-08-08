n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

def valid(x,y):
    if x<0 or x>=n or y<0 or y>=n:
        return False
    else:
        return True

dx,dy = [1,0,-1,0],[0,1,0,-1]
x,y=0,0
count=0

while (y <n):
    oneCount=0
    for dir in range(4):
        nx, ny = x+dx[dir], y+dy[dir]
        if valid(nx,ny) and grid[nx][ny]==1:
            oneCount +=1
    if oneCount >=3:
        count+=1
    x +=1
    if x==n:
        x,y = 0, y+1
print(count)
