import sys

n = int(input())

arr = list(map(int, input().split()))

two_counter = 0

for i in range(len(arr)):
    if arr[i] == 2:
        two_counter += 1

    if two_counter == 3:
        print(i + 1)
        sys.exit()