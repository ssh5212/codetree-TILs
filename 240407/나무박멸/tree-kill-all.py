from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def grow():
    for i in range(n):
        for j in range(n):
            change_arr[i][j] = arr[i][j]

    for i in range(n):
        for j in range(n):
            # 나무가 자란 곳인 경우
            if arr[i][j] > 0:
                for d in range(4):
                    nx = dx[d] + i
                    ny = dy[d] + j

                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        continue

                    # 내 상하좌우의 위치에 나무가 있다면
                    if arr[nx][ny] > 0:
                        change_arr[i][j] += 1

    for i in range(n):
        for j in range(n):
            arr[i][j] = change_arr[i][j]


def diffusion():
    for i in range(n):
        for j in range(n):
            q = deque()

            # 나무가 위치한 곳인 경우
            if arr[i][j] > 0:
                for d in range(4):
                    nx = dx[d] + i
                    ny = dy[d] + j

                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        continue

                    if arr[nx][ny] == 0 and h_arr[nx][ny] == 0:
                        q.append([nx, ny])

            now_len = len(q)

            while(len(q) != 0):
                px, py = q.popleft()
                change_arr[px][py] += arr[i][j] // now_len

    for i in range(n):
        for j in range(n):
            arr[i][j] = change_arr[i][j]


def h_down():
    for i in range(n):
        for j in range(n):
            if h_arr[i][j] > 0:
                h_arr[i][j] -= 1


hx = [-1, -1, 1, 1]
hy = [-1, 1, 1, -1]


def herbicide():
    global ans
    max_h_count = 0
    max_x = 0;
    max_y = 0;

    for i in range(n):
        for j in range(n):

            # 나무가 있는 위치인 경우
            if arr[i][j] > 0:
                h_count = arr[i][j] # 제초제로 제거될 나무 개수

                for h in range(4):
                    for l in range(1, k + 1):
                        nx = hx[h] * l + i
                        ny = hy[h] * l + j

                        if nx < 0 or nx >= n or ny < 0 or ny >= n:
                            break

                        # 비어있거나 벽인 경우
                        if arr[nx][ny] <= 0:
                            break

                        h_count += arr[nx][ny]

                if max_h_count < h_count:
                    max_h_count = h_count
                    max_x = i
                    max_y = j

    arr[max_x][max_y] = 0
    h_arr[max_x][max_y] = c

    # print(max_x, max_y)

    # 제초제 전파
    for h in range(4):
        for l in range(1, k + 1):
            nx = hx[h] * l + max_x
            ny = hy[h] * l + max_y

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                break

            if arr[nx][ny] <= 0:
                h_arr[nx][ny] = c
                break

            arr[nx][ny] = 0
            h_arr[nx][ny] = c

    # print(h_arr)
    # print(arr)
    ans += max_h_count


n, m, k, c = list(map(int, input().split()))
arr = []
ans = 0
h_arr = [[0] * n for i in range(n)]
change_arr = [[0] * n for i in range(n)]

for i in range(n):
    arr.append(list(map(int, input().split())))

# m년 만큼 반복
for _ in range(m):
    # 나무 성장
    grow()

    # 나무 번식
    diffusion()

    # 제초제 약화
    h_down()

    # 제초제 뿌림
    herbicide()

print(ans)