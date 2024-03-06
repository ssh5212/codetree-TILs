n, q = map(int, input().split())
arr = list(map(int, input().split()))

for _ in range(q):
    q_arr = list(map(int, input().split()))

    if q_arr[0] == 1:
        print(arr[q_arr[1] - 1])
    elif q_arr[0] == 2:
        now_ans = -1
        for i in range(len(arr)):
            if arr[i] == q_arr[1]:
                now_ans = i
        if now_ans == -1:
            print(0)
        else:
            print(now_ans + 1)
    else:
        for i in range(q_arr[1] - 1, q_arr[2]):
            print(arr[i], end=" ")
        print()