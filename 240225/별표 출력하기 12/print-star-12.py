n = int(input())

arr = [[" "]*n for i in range(n) ]

for i in range(n):
    if i % 2 == 0:
        arr[0][i] = '*'
    else:
        for j in range(i + 1):
            arr[j][i] = "*"

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=" ")
    print()