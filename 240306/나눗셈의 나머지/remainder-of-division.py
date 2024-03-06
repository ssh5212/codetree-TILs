a, b = map(int, input().split())

arr = [0] * b

while(True):
    arr[a % b] += 1
    a = a // b
    
    if a <= 1:
        break

ans = 0
for i in arr:
    ans += i ** 2

print(ans)