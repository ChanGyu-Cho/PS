N = int(input())
arr =[]
for _ in range(N):
    arr.append(int(input()))
arr.append(0)

maxCount =0
count =1
prev = arr[0]
for i in arr[1:]:
    if(prev < i):
        count +=1
    else:
        if(count > maxCount):
            maxCount =count
        count =1
    prev =i
print(maxCount)
