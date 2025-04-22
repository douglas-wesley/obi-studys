def escher(N):
    esc = []
    for i in range(N):
        x = int(input())
        if x <= N:
            esc.append(x)
    if len(esc) != N:
        return 'N'
    else:
        return 'S'


q = int(input())

print(escher(q))
