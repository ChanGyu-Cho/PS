n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
maxSum =0

for i in range(n):
    for j in range(n):
        for k in range(n):
            if(i==j or j==k or k==i):   # 겹치는 모든 케이스 통과
                continue
            a,b,c = str(arr[i]), str(arr[j]), str(arr[k])

            while(len(a) != 5):
                a = "0"+a
            while(len(b) != 5):
                b = "0"+b
            while(len(c) != 5):
                c = "0"+c

            passFlag = True
            for x,y,z in zip(a,b,c):
                s = int(x)+int(y)+int(z)
                if(s>=10):
                    passFlag = False
                    break

            if(passFlag):
                S = int(a)+int(b)+int(c)
                maxSum =max(maxSum, S)
if maxSum ==0:
    print(-1)
else:
    print(maxSum)


