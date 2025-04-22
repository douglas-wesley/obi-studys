def tor():
    w = 0
    for _ in range(6):
        j = str(input())
        if j in 'Vv':
            w += 1
    if w >= 5:
        return 1
    elif w >= 3 and w <= 4:
        return 2
    elif w >= 1 and w <= 2:
        return 3
    else:
        return -1

print(tor())
