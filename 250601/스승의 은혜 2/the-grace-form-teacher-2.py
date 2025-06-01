N, B = map(int, input().split())
P = [int(input()) for _ in range(N)]

# Please write your code here.

maxDep = 0
visited = [False for _ in range(N)]

def selStu(dep, SUM):
    global maxDep
    if(dep == N+1):
        return
    if(SUM >= B):
        return
    maxDep = max(maxDep, dep)
    if(maxDep == N):
        return
    for stu in range(N):
        if(not visited[stu]):
            visited[stu] = True
            selStu(dep+1, SUM+P[stu])
            visited[stu] = False

for stu in range(N):   # 학생 하나씩 반값 선택
    visited[stu] = True
    SUM = P[stu]//2
    if(SUM > B):
        continue
    maxDep = 1
    selStu(2, SUM) # 깊이 1로 재귀
    visited[stu] = False
print(maxDep)