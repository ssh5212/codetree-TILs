arr = list(map(int, input().split()))

new_arr = []
for i in arr:
    if i != 0:
        new_arr.append(i)
    else:
        break

for i in range(len(new_arr) -1, -1, -1):
    print(new_arr[i], end=" ")