def jogo(p,d1,d2):
    total = d1 + d2
    if total % 2 == 0:
        if p == 1:
            return 1
        else:
            return 0
    else:
        if p == 1:
            return 0
        else:
            return 1

p = int(input(""))
d1 = int(input(""))
d2 = int(input(""))

print(jogo(p,d1,d2))
