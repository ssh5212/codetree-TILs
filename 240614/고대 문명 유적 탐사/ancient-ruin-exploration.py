from collections import deque


def arr_copy(arr1, arr2):
    for i in range(5):
        for j in range(5):
            arr1[i][j] = arr2[i][j]


def rotate(x, y, rr, arrs):

    for i in range(nn):
        for j in range(nn):
            arrs[i][j] = arr_ori[i][j]

    ror = [[0] * 3 for _ in range(3)]
    result = [[0] * 3 for _ in range(3)]

    for i in range(3):
        for j in range(3):
            ror[i][j] = arrs[i + x][j + y]

    # 90도 회전
    if rr == 0:
        for i in range(3):
            for j in range(3):
                result[j][3 - i - 1] = ror[i][j]
    # 180도 회전
    elif rr == 1:
        for i in range(3):
            for j in range(3):
                result[3 - i - 1][3 - j - 1] = ror[i][j]
    # 270도 회전
    else:
        for i in range(3):
            for j in range(3):
                result[3 - j - 1][i] = ror[i][j]

    # arr에 회전 결과 적용
    for i in range(3):
        for j in range(3):
            arrs[i + x][j + y] = result[i][j]


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y):
    global v, nn
    q = deque()
    q.append([x, y, arr[x][y]])

    items = [] # 바꿀 아이템 저장
    items.append([x, y])

    v[x][y] = True

    while len(q) != 0:
        px, py, pc = q.popleft()

        for d in range(4):
            nx = dx[d] + px
            ny = dy[d] + py

            if nx < 0 or nx >= nn or ny < 0 or ny >= nn or v[nx][ny] == True or arr[nx][ny] != pc:
                continue

            v[nx][ny] = True
            items.append([nx, ny])
            q.append([nx, ny, pc])

    if len(items) >= 3:
        for i, j in items:
            arr[i][j] = 0

        return len(items)
    return 0


def fill():
    global nn, now_wc
    for j in range(nn):
        for i in range(nn - 1, -1, -1):
            if arr[i][j] == 0:
                arr[i][j] = wall[now_wc]
                now_wc += 1


def find():
    global nn, v

    f_ans = 0
    fir_ans = 0

    turn = 0
    while True:
        now_ans = 0
        v = [[False] * nn for _ in range(nn)]
        for i in range(nn):
            for j in range(nn):
                if arr[i][j] != 0 and v[i][j] != True:
                    now_ans += bfs(i, j)

        if turn == 0:
            fir_ans = now_ans

        turn += 1

        f_ans += now_ans
        if now_ans == 0:
            break

        # 벽면 채우기
        fill()
    return fir_ans, f_ans


def print_arr(arrs):
    for i in range(len(arrs)):
        for j in range(len(arrs)):
            print(arrs[i][j], end=" ")
        print()


kk, mm = list(map(int, input().split()))
nn = 5 # 유적 크기
arr_ori = []

for i in range(nn):
    arr_ori.append(list(map(int, input().split())))

wall = list(map(int, input().split()))

tc = 0
wc = 0 # 벽면 숫자 사용 개수 카운팅

# 탐사 횟수만큼 반복
while tc < kk:
    tc_f_ans = 0
    tc_ans = 0
    tc_x = 0
    tc_y = 0
    tc_r = 0
    tc_wc = 0
    tc_arr = [[0] * nn for _ in range(nn)]
    # 회전할 시작점 선택
    for i in range(3):
        for j in range(3):
            arr = []
            v = []

            # 3가지 방향으로 회전
            for r in range(3):
                ans = 0
                now_wc = wc

                arr = [[0] * nn for _ in range(nn)]
                rotate(i, j, r, arr)

                # 유적 찾기
                fir_ans, ans = find()

                if ans == 0:
                    continue

                if fir_ans > tc_f_ans:
                    tc_f_ans = fir_ans
                    tc_ans = ans
                    tc_x = i
                    tc_y = j
                    tc_r = r
                    tc_wc = now_wc
                    arr_copy(tc_arr, arr)

                elif fir_ans == tc_f_ans:
                    if tc_r > r:
                        tc_f_ans = fir_ans
                        tc_ans = ans
                        tc_x = i
                        tc_y = j
                        tc_r = r
                        tc_wc = now_wc
                        arr_copy(tc_arr, arr)

                    elif tc_r == r:
                        if tc_y > j:
                            tc_f_ans = fir_ans
                            tc_ans = ans
                            tc_x = i
                            tc_y = j
                            tc_r = r
                            tc_wc = now_wc
                            arr_copy(tc_arr, arr)

                        elif tc_y == j:
                            if tc_x > i:
                                tc_f_ans = fir_ans
                                tc_ans = ans
                                tc_x = i
                                tc_y = j
                                tc_r = r
                                arr_copy(tc_arr, arr)

    if tc_ans == 0:
        break

    # ori 수정하기
    arr_copy(arr_ori, tc_arr)
    print(tc_ans, end=" ")
    wc = tc_wc
    tc += 1