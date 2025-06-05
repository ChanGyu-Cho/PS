N = int(input())
str = input()
"""
두번 이상 나타나지 않는 최소 길이
즉, 같은 문자열이 2번 나타나면 패스, 1번 나타나면 그 문자열
우선 완전탐색, 1~N//2 +1/까지 반복(2번 나와야 하므로, 최대 N//2)
    해당 하는 길이 만큼 탐색해서 dic에 저장
마지막 dic 길이순 정렬, 처음 1이 나오는 key 리턴
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