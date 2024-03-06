arr = ['L', 'E', 'B', 'R', 'O', 'S']

word = input()
ans = -1
for i in range(len(arr)):
    if arr[i] == word:
        ans = i

if ans == -1:
    print('None')
else:
    print(ans)