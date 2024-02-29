arr = list(map(int, input().split()))

ans = 0
count = 0

for i in arr:
    if i < 250:
        ans += i
        count += 1
    else:
        break

print(f'{ans} {(ans / count):.1f}')