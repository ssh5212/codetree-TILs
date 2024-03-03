n = int(input())
arr = list(map(int, input().split()))
arr2= []
for i in arr:
    if i % 2== 0:
        arr2.append(i)

for i in arr2:
    print(i, end=" ")