def pil(A,B,C):
    if (B - A) < (C - B):
        return 1
    elif (B - A) > (C - B):
        return -1
    elif (B - A) == (C - B):
        return 0

a = int(input())
b = int(input())
c = int(input())

print(pil(a,b,c))
