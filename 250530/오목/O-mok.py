board = [list(map(int, input().split())) for _ in range(19)]

# Please write your code here.
N = 19
    
def ver(cor, i,j):
    verFlag = True
    for x in range(i,i+5):
        if(board[x][j] !=cor):
            verFlag = False
            break
    if(verFlag):
        print(cor)
        print(i+3, j+1)
        exit(0)

def dia(cor,i,j):
    diaFlag = True
    for x,y in zip(range(i,i+5), range(j,j+5)):
        if(board[x][y] !=cor):
            diaFlag = False
            break
    if(diaFlag):
        print(cor)
        print(i+3, j+3)
        exit(0)

def hor(cor,i,j):
    horFlag = True
    for y in range(j,j+5):
        if(board[i][y] != cor):
            horFlag = False
            break
    if(horFlag):
        print(cor)
        print(i+1, j+3)
        exit(0)

for i in range(N):
    for j in range(N):
        cor = board[i][j]
        if not cor==0:
            if j<15:
                hor(cor,i,j)
            if i<15 and j<15:
                dia(cor, i,j)
            if i<15:
                ver(cor,i,j)
print(0)