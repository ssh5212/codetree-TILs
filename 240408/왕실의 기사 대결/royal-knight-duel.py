# 기사 번호 1번부터 시작함
# 지도 (1,1) 부터 시작함
from collections import deque


def night_arr_to_list():
    global night_list
    night_list = [[] for i in range(nn + 1)]

    for i in range(len(night_arr)):
        for j in range(len(night_arr[0])):
            if night_arr[i][j] >= 1:
                night_list[night_arr[i][j]].append([i, j])


def print_arr(li):
    for i in range(len(li)):
        for j in range(len(li[0])):
            print(li[i][j], end=" ")
        print()


def move():
    global flag, ii, dd
    q = deque()

    # v = [False] * (nn + 1)

    for i in night_list[ii]:
        q.append(i)
    move_set.add(ii)

    for i in night_list[ii]:
        move_list_data = [i[0], i[1], ii]
        move_list.append(move_list_data)

    while(len(q) != 0):
        px, py = q.popleft()

        nx = dx[dd] + px
        ny = dy[dd] + py

        # 하나라도 벽을 만나면
        if map_arr[nx][ny] == 2:
            flag = True
            break

        # 이동하려는 위치에 기사가 있고 추가된 적이 없다면
        if night_arr[nx][ny] != 0 and night_arr[nx][ny] not in move_set:
            for i in night_list[night_arr[nx][ny]]:
                q.append(i)
            move_set.add(night_arr[nx][ny])

            for i in night_list[night_arr[nx][ny]]:
                move_list_data = [i[0], i[1], night_arr[nx][ny]]
                move_list.append(move_list_data)



def update():
    global night_arr
    night_arr = [[0] * (ll + 2) for i in range(ll + 2)]
    # 이동해야 할 기사 업데이트
    for r, c, night_num in move_list:
        night_arr[r + dx[dd]][c + dy[dd]] = night_num

        # 내가 공격자라면 데미지 추가 무시
        if night_num == ii:
            continue
            
        # 데미지 주기
        if map_arr[r + dx[dd]][c + dy[dd]] == 1:
            night_hp[night_num] -= 1

            if night_hp[night_num] <= 0:
                dead_set.add(night_num)



    # 기존 기사 업데이트
    for i in range(1, len(night_list)):
        if i not in move_set:
            for jx, jy in night_list[i]:
                night_arr[jx][jy] = i

    # 리스트 업데이트
    night_arr_to_list()


def delete():
    for now in dead_set:
        for i in night_list[now]:
            night_arr[i[0]][i[1]] = 0

    # 리스트 업데이트
    night_arr_to_list()


ll, nn, qq = list(map(int, input().split()))

night_hp = [0] * (nn + 1) # 기사 체력 저장
ori_night_hp = [0] * (nn + 1) # 원본 기사 체력 저장
night_list = [[] for i in range(nn + 1)] # 기사 위치 저장

map_arr = [] # 지도 정보 저장
night_arr = [[0] * (ll + 2) for i in range(ll + 2)] # 지도 내 기사 정보 저장

map_arr.append([2] * (ll + 2))
for i in range(ll):
    add_list = [2]
    add_list.extend(list(map(int,input().split())))
    add_list.extend([2])

    map_arr.append(add_list)
map_arr.append([2] * (ll + 2))


for numb in range(1, nn + 1):
    rr, cc, hh, ww, kk = list(map(int, input().split()))

    night_hp[numb] = kk
    ori_night_hp[numb] = kk
    for i in range(hh):
        for j in range(ww):
            night_list[numb].append([rr+i, cc+j])
            night_arr[rr + i][cc + j] = numb


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

attack_list = []
for _ in range(qq):
    ii, dd = list(map(int, input().split()))

    # 체력이 0이하인 경우 무시
    if night_hp[ii] <= 0:
        continue

    # 밀어보고 판단
    flag = False
    move_set = set()
    move_list = []

    move()

    if flag == True:
        continue

    # 체스판 업데이트 & 데미지
    dead_set = set()
    update()

    # 죽은 캐릭터 제거
    delete()


ans = 0

for i in range(len(night_hp)):
    if night_hp[i] > 0:
        ans += (ori_night_hp[i] - night_hp[i])
print(ans)