n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
"""
모든 x,y의 짝수에 대해 나눠보기
각 point에 대해 x,y 기준으로 4등분해서 각 지점의 값 MAX와 비교
이후 maxMin과 MAX 비교
"""
# Please write your code here.
maxMin = 10**10

for x in range(2, 101, 2):
    for y in range(2, 101, 2):
        c1,c2,c3,c4 =0,0,0,0
        for xp, yp in points:
            
            if(xp<x and yp<y):
                c1+=1
            elif(xp>x and yp<y):
                c2+=1
            elif(xp<x and yp>y):
                c3+=1
            elif(xp>x and yp>y):
                c4+=1
        maxMin = min(maxMin,max(c1,c2,c3,c4))
print(maxMin)
