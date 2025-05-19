import sys
input = sys.stdin.readline

def race(L, move):
    cur =0
    for _ in range(move):
        v,t = map(int,input().split())
        for i in range(t):
            cur +=v
            L.append(cur)

N,M = map(int,input().split())
A=[0]
B=[0]

race(A,N)
race(B,M)

count=1
state=0
if(A[1] > B[1]):
    state=1
elif(A[1] < B[1]):
    state=2
else:
    state=3
for a,b in zip(A[1:],B[1:]):
    if(state ==1 and not(a >b)):
        state = 2 if a <b else 3
        count+=1
    elif(state ==2 and not(a <b)):
        state = 1 if a>b else 3
        count+=1
    elif(state ==3 and not (a==b)):
        state =1 if a >b else 2
        count+=1
print(count)
        