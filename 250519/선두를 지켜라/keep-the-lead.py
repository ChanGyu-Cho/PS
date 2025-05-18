N, M = map(int,input().split())
A =[0]
B =[0]
Acur=0
for i in range(N):
    v,t = map(int, input().split())
    for _ in range(t):  # 1초만큼
        Acur +=v
        A.append(Acur)
Bcur=0
for i in range(M):
    v,t = map(int, input().split())
    for _ in range(t):  # 1초만큼
        Bcur +=v
        B.append(Bcur)

changeCount=0
prev =-1    # a선두 0, b선두 1, 초기 -1
for a,b in zip(A,B):
    if(a==b):
        continue
    elif(a>b and prev !=0):
        changeCount +=1
        prev =0
    elif(a<b and prev !=1):
        changeCount +=1
        prev =1
print(changeCount-1)
