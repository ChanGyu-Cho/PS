X, Y = map(int, input().split())

# Please write your code here.

count=0
for num in range(X,Y+1):
    sNum = str(num)
    palFlag = True
    for i in range((len(sNum)+1)//2):
        if(sNum[i] !=sNum[-(i+1)]):
            palFlag=False
            break
    if(palFlag):
        count+=1
print(count)