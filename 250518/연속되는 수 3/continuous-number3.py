N = int(input())
arr =[]
for _ in range(N):
    a = int(input())
    arr.append(1 if a >0 else 0) 
arr.append(1001)

maxCount =0
count =1
prev = arr[0]
for i in arr[1:]:
    if(prev == i):
        count+=1
    else:
        if(count > maxCount):
            maxCount =count
        count =1
        prev =i
print(maxCount)
