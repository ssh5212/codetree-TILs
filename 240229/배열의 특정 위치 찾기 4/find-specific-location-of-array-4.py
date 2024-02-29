arr = list(map(int, input().split()))

ans_sum = 0
ans_cnt = 0

for i in arr:
    if i != 0:
        if i % 2 == 0:
            ans_cnt += 1
            ans_sum += i
    else:
        break

print(f'{ans_cnt} {ans_sum}')