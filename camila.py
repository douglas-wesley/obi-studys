def cam(I1,I2,I3):
    if I1 < I2 < I3 or I3 < I2 < I1:
        return I2
    elif I2 < I1 < I3 or I3 < I1 < I2:
        return I1
    else:
        return I3

q = int(input())
p = int(input())
r = int(input())

print(cam(q,p,r))

