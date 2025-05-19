import sys
input = sys.stdin.readline

def verf(nex):
    if(nex[0] <0 or nex[0]>N-1 or nex[1] <0 or nex[1]>N-1):
        return False
    else:
        return True

offset =[[-1,0],[0,1],[1,0],[0,-1]]

N, T = map(int, input().split())
move=input()

coor=[]
for _ in range(N):
    coor.append(list(map(int,input().split())))

cur = [N//2,N//2]
S =coor[cur[0]][cur[1]]
d = 0
for com in move:
    if(com == "F"):
        nex =[cur[0]+offset[d][0], cur[1]+offset[d][1]]
        if(verf(nex)):
            S += coor[nex[0]][nex[1]]
            cur = nex
    else:
        d += -1 if com=="L" else 1
        d = (d+4)%4
print(S)
    
