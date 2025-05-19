N, M = map(int, input().split())
A=[0]   # index=time
B=[0]

Acur=0
Atotal=0
for _ in range(N):
    t,d = input().split()
    sign= -1 if d=='L' else 1
    Atotal+=int(t)
    for i in range(int(t)):
        Acur +=1*sign
        A.append(Acur)
Bcur=0
Btotal=0
for _ in range(M):
    t,d = input().split()
    sign= -1 if d=='L' else 1
    Btotal+=int(t)
    for i in range(int(t)):
        Bcur +=1*sign
        B.append(Bcur)

# padding
if(Atotal > Btotal):
    for _ in range(Atotal-Btotal):
        B.append(B[-1])
else:
    for _ in range(Btotal-Atotal):
        A.append(A[-1])

prevA=0
prevB=0
count=0
for a,b in zip(A[1:],B[1:]):
    if(prevA != prevB and a==b):
        count+=1
    prevA =a
    prevB =b
print(count)


