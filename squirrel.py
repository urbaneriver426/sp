def squirrel(N):
    x = 1
    for i in range(1, N+1):
        x = x * i
    x = str(x)
    x = int(x[0])
    return print(x)
