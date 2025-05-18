N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))
arr.append(1001)

prev = arr[0]
maxCount =0
count =1
for i in arr[1:]:
    if(prev == i):
        count +=1
    elif(prev != i):
        if(count > maxCount):
            maxCount =count
        count =1
        prev = i
print(maxCount)
