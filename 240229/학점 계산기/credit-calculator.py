n = int(input())

arr = list(map(float, input().split()))

arr_sum = sum(arr)

ans = (arr_sum / len(arr))

print(f'{ans:.1f}')

if ans >= 4:
    print("Perfect")
elif ans >= 3:
    print("Good")
else:
    print("Poor")