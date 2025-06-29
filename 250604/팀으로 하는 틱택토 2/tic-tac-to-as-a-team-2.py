inp = [input() for _ in range(3)]
"""
2명이 한팀, 팀으로 이길 가짓수
2개 숫자 조합으로 이루어 져야함
3,3,2번 검사, 두 팀의 조합이 연속될 경우 승리 카운트
중복 팀 승리 경우를 위해, 두 팀의 조합을 저장
frozenset을 key로 하는 dic 이용
"""
# Please write your code here.
comb = {}

for i in range(3):
    line = set()
    for j in range(3):
        line.add(inp[i][j])
    if(len(line) == 2):
        lline = list(line)
        comb[frozenset((lline[0], lline[1]))] = True

for j in range(3):
    line = set()
    for i in range(3):
        line.add(inp[i][j])
    if(len(line) == 2):
        lline = list(line)
        comb[frozenset((lline[0], lline[1]))] = True

line = set()
for i in range(3):
    line.add(inp[i][i])
if(len(line) == 2):
    lline = list(line)
    comb[frozenset((lline[0], lline[1]))] = True
line = set()
for i in range(3):
    line.add(inp[i][-i+2])
if(len(line) == 2):
    lline = list(line)
    comb[frozenset((lline[0], lline[1]))] = True

print(len(comb))