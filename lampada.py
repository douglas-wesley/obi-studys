def lam(num):
    l1 = False
    l2 = False

    for n in range(num):
        val = int(input(""))
        if val == 1:
            l1 = not l1
        elif val == 2:
            l2 = not l2

    print("1" if l1 else "0")
    print("1" if l2 else "0")
    return "Done!"

x = int(input())
print(lam(x))
