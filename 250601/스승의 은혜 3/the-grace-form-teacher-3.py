N, B = map(int, input().split())
gifts = [tuple(map(int, input().split())) for _ in range(N)]
P = [gift[0] for gift in gifts]
S = [gift[1] for gift in gifts]
"""
단순하게 학생 하나씩 제외해보기
+ 조합(백트래킹) 문제
"""
# Please write your code here.

maxDep = 0
visited = [False for _ in range(N)]

def selStu(dep, SUM):
    global maxDep
    if(dep == N):
        return
    if(SUM > B):
        return
    maxDep = max(maxDep, dep)
    for stu in range(N):
        if(not visited[stu]):
            visited[stu] = True
            selStu(dep+1, SUM+P[stu]+S[stu])
            visited[stu] = False

for stu in range(N):   # 학생 하나씩 반값 선택
    visited[stu] = True
    selStu(1, P[stu]//2+S[stu]) # 깊이 1로 재귀
    visited[stu] = False
print(maxDep)