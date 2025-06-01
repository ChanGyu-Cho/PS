N, B = map(int, input().split())
gifts = [tuple(map(int, input().split())) for _ in range(N)]
gifts = sorted(gifts, key=lambda x: x[0]+x[1])
P = [gift[0] for gift in gifts]
S = [gift[1] for gift in gifts]
"""
단순하게 학생 하나씩 제외해보기
+ 조합(백트래킹) 문제
"""
# Please write your code here.

maxCount = 0

for halfStu in range(N):   # 학생 하나씩 반값 선택
    SUM = P[halfStu]//2 +S[halfStu]
    if(SUM >B):
        continue
    count =1
    for stu in range(N):
        if(halfStu == stu):
            continue
        SUM += P[stu] +S[stu]
        if(SUM >B):    # 제한 넘기면, 어차피 다음은 더큰 선물이기에 파기
            break
        count +=1
    maxCount = max(maxCount, count)
    
print(maxCount)