n = int(input())

flag = 0

i = 1
while True:
    print(n * i, end=" ")

    if (i * n) % 5 == 0:
        flag += 1

        if flag == 2:
            break
    
    i += 1