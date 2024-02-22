arr = []

for _ in range(4):
    arr.append(list(map(int, input().split(" "))))

for i in range(4):
    ans = 0
    for j in range(4):
        ans += arr[i][j]
    print(ans)