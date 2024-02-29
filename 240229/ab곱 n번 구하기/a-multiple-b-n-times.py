n = int(input())

for _ in range(n):
    a, b = map(int, input().split(" "))

    ans = 1
    for i in range(a, b + 1):
        ans *= i

    print(ans)