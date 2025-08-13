n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]

# Please write your code here.

dx, dy = [0,1,0,-1],[1,0,-1,0]  # 시계방향 회전

def verify(x,y):
    if x<0 or x >=n or y<0 or y >=m or arr[x][y]!=0:
        return False
    else:
        return True

x,y =0,0
d =0
for i in range(1, n*m+1):   # 1부터 n*m+1 까지
    arr[x][y] = i

    nx,ny = x+dx[d], y+dy[d]
    if verify(nx,ny):   # 회전 해야됨
        x,y = nx,ny
    else:
        d = (d+1)%4
        x,y = x+dx[d], y+dy[d]
    
for line in arr:
    print(*line)