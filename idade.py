def id(M,F1,F2):
    F3 = M - (F1 + F2)
    if F3 > F1 and F3 > F2:
        return F3
    elif F1 > F3 and F1 > F2:
        return F1
    else:
        return F2

a = int(input())
b = int(input())
c = int(input())

print(id(a,b,c))
