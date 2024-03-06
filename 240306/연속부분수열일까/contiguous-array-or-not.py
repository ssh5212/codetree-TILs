n1, n2 = map(int, input().split())

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

ans = 'No'

for i in range(len(arr1)):
    if i + len(arr2) - 1 > len(arr1) - 1:
        break
    if arr1[i] == arr2[0]:
        for j in range(len(arr2)):
            if arr1[i + j] != arr2[j]:
                break
            if j == len(arr2) - 1:
                ans = 'Yes'

print(ans)