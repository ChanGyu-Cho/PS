arr = list(map(int, input().split()))
"""
2,2,1로 팀
최대-최소 차이가 최소가 되게
모든 팀의 능력치가 서로 다르게
5C2*2+5 횟수의 완전 탐색 가능
"""
# Please write your code here.

visited = [False for _ in range(5)]
group = [0 for _ in range(5)]
global min_max
min_max = 10**10

def rcur(curNum, dep):
    global min_max
    if(dep == 5):
        g1,g2,g3 = group[0]+group[1], group[2]+group[3], group[4]
        if(g1-g2 ==0 or g2-g3==0 or g3-g1==0):
            return
        min_max = min(min_max, max(g1,g2,g3)-min(g1,g2,g3))
        return
    
    for i in range(5):
        if(not visited[i]):
            visited[i]=True
            group[dep] = arr[i]
            rcur(i, dep+1)  # recursion
            visited[i] = False
            group[dep] = 0

for i in range(5):
    visited[i]=True
    group[0] = arr[i]
    rcur(i, 1)
    visited[i]=False
    group[0] = 0
if min_max == 10**10:
    print(-1)
else:
    print(min_max)