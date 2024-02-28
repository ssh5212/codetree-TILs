n = int(input())

for i in range(1, n + 1):
    for j in range(1, n+1):
        if i + j == n + 2:
            break
        
        if i + j == n + 1:
            print(f'{i} * {j} = {i * j}')
        else:
            print(f'{i} * {j} = {i * j}', end=" / ")