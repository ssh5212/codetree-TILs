arr = list(map(int, input().split()))

ans1 = 0
ans2 = 0
for i in range(len(arr)):
    if i % 2 == 1:
        ans1 += arr[i]

    if i % 3 == 2:
        ans2 += arr[i]

print(f'{ans1} {ans2/3:.1f}')