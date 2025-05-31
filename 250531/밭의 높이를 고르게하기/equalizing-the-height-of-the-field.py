N, H, T = map(int, input().split())
arr = list(map(int, input().split()))
"""
T길이 만큼 범위 지정후 탐색
H 높이와의 차의 절댓값의 합을 minVal로 갱신
최소 비용 출력
"""
# Please write your code here.

minVal = 10**10
for i in range(N-T+1):
    Sum=0
    for j in range(i, i+3):
        Sum += abs(H-arr[j])
    minVal = min(minVal, Sum)
print(minVal)