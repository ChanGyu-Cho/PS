n = int(input())
adj = list(map(int, input().split()))

"""
N이하 수들이 단 한번만 출현하는 수열을 복원
주어지는건 원본 수열에서 앞자리 수를 더한 수열인 길이 N-1
가능한 답은 여러개, 사전순 가장 앞선 수열 출력

분리할 2개의 숫자는 i,i+1 각각보다 각각 작아야하며, 합은 i와 같아야 한다
1-i까지 탐색, i, i+1보다 커지면 중단
i=0이 정해지면, 나머지 숫자들도 정해짐
i=0이 가장 큰 경우를 생각해야함

3
"""

# Please write your code here.

for i in range(adj[0]-1, 0, -1):
    arr = set()
    arr.add(i)

    cur = adj[0]-i
    for idx in range(1, n):
        if(idx == n-1):
            arr.add(cur)
            print(*arr)
            exit()
        if(cur > adj[idx] or cur <=0 or cur in arr):
            break
        arr.add(cur)
        cur = adj[idx] - cur

