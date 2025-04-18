def sec(N):
    nn = 0
    c = 0
    for _ in range(N):
        n = int(input())
        if n != nn:
            c += 1
            nn = n
    return c

q = int(input())

print(sec(q))
