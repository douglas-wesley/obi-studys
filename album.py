def alb(N,M):
    lfig = []
    for _ in range(M):
        x = int(input())
        if x not in lfig:
            lfig.append(x)
            
    return N - len(lfig)


q = int(input())
p = int(input())

print(alb(q,p))
