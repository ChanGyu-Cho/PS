board = [list(map(int, input().split())) for _ in range(19)]

# Please write your code here.
N = 19

def search(cor, i,j):
    horFlag, verFlag, diaFlag = True, True, True
    #가로
    for x in range(i,i+5):
        if(board[x][j] != cor):
            horFlag = False
            break
    if(horFlag):
        print(cor)
        print(i+3, j+1)
        exit(0)
        return
    # 대각
    for x,y in zip(range(i,i+5), range(j,j+5)):
        if(board[x][y] !=cor):
            diaFlag = False
            break
    if(diaFlag):
        print(cor)
        print(i+3, j+3)
        exit(0)
        return
    # 세로
    for y in range(j,j+5):
        if(board[i][y] !=cor):
            verFlag = False
            break
    if(verFlag):
        print(cor)
        print(i+1, j+3)
        exit(0)
        return


for i in range(N-4):
    for j in range(N-4):
        if not board[i][j]==0:
            search(board[i][j],i,j)
print(0)