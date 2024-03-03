n = int(input())

arr = []
arr.append(1)
arr.append(n)

while True:
    if arr[-1] > 100:
        break
    else:
        arr.append(arr[-1] + arr[-2])

for i in arr:
    print(i, end=" ")