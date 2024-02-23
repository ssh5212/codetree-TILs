n = int(input())

for i in range(n):
    print("*",end="")
    for j in range(i):
        print("**",end="")
    print()