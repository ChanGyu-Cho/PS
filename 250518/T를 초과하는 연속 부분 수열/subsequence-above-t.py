N, K = map(int, input().split())
arr = list(map(int, input().split()))
arr.append(1001)

maxCount =0
count =0
if(arr[0] > K):
    count+=1
for i in arr[1:]:
    if(i >K):
        count+=1
    else:
        if(count >maxCount):
            maxCount =count
        count =0
print(maxCount)
