N, M, K = map(int, input().split())
stu = [0 for _ in range(101)]
for _ in range(M):
    pen = int(input())
    stu[pen]+=1
    if(stu[pen] >=K):
        print(pen)
        exit()
print(-1)