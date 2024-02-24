n = int(input())

for i in range(n):
    if i % 2 == 0:
        for j in range(n-(i//2)):
            print("*", end=" ")
        print()
    if i % 2 == 1:
        for j in range(i//2 + 1):
            print("*", end=" ")
        print()
for i in range(n-1, -1, -1):
    if i % 2 == 0:
        for j in range(n-(i//2)):
            print("*", end=" ")
        print()
    if i % 2 == 1:
        for j in range(i//2 + 1):
            print("*", end=" ")
        print()