arr = list(map(int, input().split()))

ans1 = 0
ans2 = 0

for i in range(len(arr)):
    if i % 2 == 0:
        ans1 += arr[i]
    else:
        ans2 += arr[i]

if ans1 > ans2:
    print(ans1 - ans2)
else:
    print(ans2 - ans1)