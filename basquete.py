def bas(D):
    if D <= 800:
        return 1
    elif D > 800 and D <= 1400:
        return 2
    else:
        return 3

a = int(input())

print(bas(a))
