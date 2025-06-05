N = int(input())
str = input()
"""
두번 이상 나타나지 않는 최소 길이
즉, 같은 문자열이 2번 나타나면 패스, 1번 나타나면 그 문자열
우선 완전탐색, 1~N(QWEQWE..의 순환구조의 경우, N//2보다 큰 길이가 2개 존재할 수 있음)
    해당 하는 길이 만큼 탐색해서 dic에 저장
key, dic[key]의 list로 key 길이로 정렬
len(key)로 방문 처리, 방문하지 않은 길이이고, 2개 이상 존재하면, 방문처리후 최대 길이 갱신
최대길이+1이 두번이상 나타나지 않는 문자열의 최소 길이
"""
# Please write your code here.

dic = {}

for sld in range(1, N+1):
    for i in range(N-sld+1):
        key = str[i:i+sld]
        if(key in dic):
            dic[key] +=1
        else:
            dic[key] = 1

l = [[key,dic[key]] for key in dic]
l = sorted(l, key = lambda x: len(x[0]))
#print(l)

visited = [False for _ in range(N+1)]
maxLen = 1
for key, count in l:
    if(visited[len(key)]):
        continue
    else:
        if(count >= 2):
            visited[len(key)] = True
            maxLen = max(maxLen, len(key))
print(maxLen+1)