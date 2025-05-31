N = int(input())
a, b, c = map(int, input().split())

# Please write your code here.

count =0

for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(1, N+1):
            if(abs(i-a) < 3 or abs(j-b) < 3 or abs(k-c) < 3):
                count +=1
print(count)