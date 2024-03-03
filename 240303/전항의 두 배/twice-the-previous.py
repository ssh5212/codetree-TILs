a1, a2 = map(int, input().split())

arr = []
arr.append(a1)
arr.append(a2)

for i in range(2, 10):
    arr.append(arr[-1] + arr[-2]*2)

for i in arr:
    print(i, end=" ")