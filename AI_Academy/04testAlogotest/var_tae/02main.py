arr = [int(value) for value in input().split()]

answer = -1

chk_arith = []  # 등차 검증
chk_geomt = []  # 등비 검증
idx = arr.index(-1)  # -1의 위치 찾고

# -1 찾을때 까지 찾아라
for i in range(len(arr) - 1, idx, -1):
    if i - 1 != idx:
        chk_arith.append(arr[i] - arr[i - 1])  # 등차 패턴 찾기용 리스트에 입력
        chk_geomt.append(arr[i] // arr[i - 1])  # 등비 패턴 찾기용 리스트에 입력

# -1 의 다음 위치부터 또 탐색
for j in range(idx - 1, 0, 1):
    if j - 1 != 0:
        chk_arith.append(arr[i] - arr[i - 1])
        chk_geomt.append(arr[i] // arr[i - 1])

# hash set 개념으로 패턴 하나 구하고
ptn_arith = set(chk_arith)
ptn_geomt = set(chk_geomt)

# 값이 한개야 , 패턴이 한개야
if len(ptn_arith) == 1:
    if idx - 1 > 0:  # 양의 정수 값의 위치 잇으면 앞의 위치에서 하나 pop
        answer = arr[idx - 1] + ptn_arith.pop()
    else:  # 아니면 하나 뺀 위치에서 pop
        answer = arr[idx + 1] - ptn_arith.pop()
else:
    if idx - 1 > 0:
        answer = arr[idx - 1] * ptn_geomt.pop()
    else:
        answer = arr[idx + 1] // ptn_geomt.pop()

print(int(answer))
