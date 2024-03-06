arr = [0, 0, 0, 0]
for i in range(3):
    di, tm = map(str, input().split())
    tm = int(tm)
    if tm >= 37 and di == 'Y':
        arr[0] += 1
    elif tm >= 37 and di == 'N':
        arr[1] += 1
    elif tm < 37 and di == 'Y':
        arr[2] += 1
    else:
        arr[3] += 1

for i in arr:
    print(i, end =" ")
if arr[0] >= 2:
    print("E")