n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.
dx,dy = [1,0,-1,0],[0,1,0,-1]   # E,N,W,S
x,y = 0,0

for i, d in enumerate(dir):
    if d=="E":
        numDir = 0
    elif d=="N":
        numDir = 1
    elif d=="W":
        numDir = 2   
    else:
        numDir = 3
    x,y = x+dist[i]*dx[numDir], y +dist[i]*dy[numDir]
print(x,y)