n = int(input())

ans_cnt = 0
for _ in range(n):
    arr = list(map(int, input().split()))

    if (sum(arr) / len(arr)) >= 60:
        print("pass")
        ans_cnt += 1
    else:
        print("fail")

print(ans_cnt)