N, M = map(int, input().split())
Max= 2000002
A =[int(1e9) for _ in range(Max)]
B =[int(1e9) for _ in range(Max)]
Time =0

Acur=0
Atime=0
for _ in range(N):
    d, t = input().split()
    Time +=int(t)
    sign = -1 if(d=="L") else 1
    for _ in range(int(t)):
        Acur = Acur + sign*1
        Atime+=1
        A[Atime]= Acur

Bcur=0
Btime=0
for _ in range(M):
    d, t = input().split()
    sign = -1 if(d=="L") else 1
    for _ in range(int(t)):
        Bcur = Bcur + sign*1
        Btime+=1
        B[Btime]= Bcur

for i in range(1, Time+1):    # i는 시간(초), 시작 0초 제외
    if(A[i] == B[i]):       # i초에 서로 위치가 같다면
        print(i)
        exit()
print(-1)
