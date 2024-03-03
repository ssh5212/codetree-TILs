a, b = map(int, input().split())

arr = [a, b]

for i in range(2, 10):
    arr.append((arr[-1] + arr[-2]) % 10)

for i in arr:
    print(i, end = " ")