n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.
compass = {'W': [-1,0], 'S':[0,-1], 'N':[0,1], 'E':[1,0]}
cur = [0,0]

for i in range(n):
    DIR, DIST = dir[i], dist[i]
    x,y = compass[DIR]
    cur[0] +=DIST*x
    cur[1] +=DIST*y
print(*cur)
