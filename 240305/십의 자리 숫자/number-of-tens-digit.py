num_list = list(map(int, input().split()))

arr = [0] * 10

for i in num_list:
    if i == 0:
        break

    now_num = i // 10

    arr[now_num] += 1

for i in range(1, 10):
    print(f'{i} - {arr[i]}')