arr = list(map(int, input().split()))

for i in range(len(arr)):
    if arr[i] == 0:
        ans = 0
        for j in range(i - 1, i - 4, -1):
            ans += arr[j]
        print(ans)
        break