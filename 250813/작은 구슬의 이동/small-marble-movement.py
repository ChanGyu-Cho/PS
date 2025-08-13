n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)
"""
n은 격자 크기, t는 이동 횟수
r,c는 raw col, d는 direction
"""

# Please write your code here.
dx,dy = [0,1,0,-1],[1,0,-1,0]   # R,D,L,U

def verify(r,c):
    if r<1 or r>n or c<1 or c>n:
        return False
    else:
        return True
dir = -1
if d == "R":
    dir = 0
elif d == "D":
    dir = 1
elif d == "L":
    dir = 2
elif d =="U":
    dir = 3

for _ in range(t):
    nx, ny = r+dx[dir], c+dy[dir]

    if verify(nx, ny):
        r, c = nx, ny
    else:
        dir = (dir+2)%4
print(r,c)