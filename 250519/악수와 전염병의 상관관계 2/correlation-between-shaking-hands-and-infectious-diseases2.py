def verfInfest(i):
    if(infested[i] and handCount[i] !=0):
        return True
    else:
        return False

def infest(i, j):
    infested[j]=1
    handCount[i] -=1

N,K,P,T = map(int,input().split())

infested =[0 for _ in range(N+1)]
infested[P] = 1
handCount = [K for _ in range(N+1)]

handShake=[]
for _ in range(T):
    handShake.append(list(map(int, input().split())))
handShake = sorted(handShake, key = lambda x : x[0])

for hs in handShake:
    t,x,y = hs
    xInfestAble = verfInfest(x)
    yInfestAble = verfInfest(y)
    if(xInfestAble):
        infest(x,y)
    if(yInfestAble):
        infest(y,x)
    
for i in infested[1:]:
    print(i, end="")
