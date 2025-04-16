def drone(A,B,C,H,L):
    area = H*L
    
    if A*B < area:
        return 'S'
    elif A*C < area:
        return 'S'
    elif B*C < area:
        return 'S'
    else: 
        return 'N'

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

print(drone(a,b,c,d,e))
