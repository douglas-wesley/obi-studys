def mor(x1,y1,x2,y2):
    res1 = x1*y1
    res2 = x2*y2
    if res1 > res2:
        return res1
    else:
        return res2

a = int(input("Digite um número"))
b = int(input("Digite um número"))
c = int(input("Digite um número"))
d = int(input("Digite um número"))

print(mor(a,b,c,d))
