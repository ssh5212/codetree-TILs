n = int(input())
arr = list(map(int, input().split()))

num_arr = [0] * 10

for i in arr:
    num_arr[i] += 1

for i in range(1, 10):
    print(num_arr[i])