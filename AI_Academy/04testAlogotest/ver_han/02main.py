# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
arr = [int(value) for value in input().split()]
answer = -1  # 숨겨진 원소의 값을 찾아서 저장하세요.
tmp = 0
val1 = []
val2 = []
j = arr.index(-1)

for i in range(len(arr) - 1, j, -1):
    if i - 1 != j:
        val1.append(arr[i] - arr[i - 1])
for i in range(j - 1, 0, -1):
    if i - 1 != 0:
        val1.append(arr[i] - arr[i - 1])

val1 = set(val1)

if j - 1 > 0:
    answer = arr[j - 1] + val1.pop()
else:
    answer = arr[j + 1] - val1.pop()

print(answer)
