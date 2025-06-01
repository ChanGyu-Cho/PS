N, B = map(int, input().split())
P = [int(input()) for _ in range(N)]

# Please write your code here.

maxCount = 0
P.sort()

for halfStu in range(N):   # 학생 하나씩 반값 선택
    SUM = P[halfStu]//2
    if(SUM >=B):
        break
    count =1
    for stu in range(N):
        if(halfStu == stu):
            continue
        SUM += P[stu]
        if(SUM >=B):    # 제한 넘기면, 어차피 다음은 더큰 선물이기에 파기
            break
        count +=1
    maxCount = max(maxCount, count)
    
print(maxCount)