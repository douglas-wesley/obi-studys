def juvenal(N):
    vals = input().split(' ')
    vals_int = [int(x) for x in vals]

    for j in range(1,N):
        if j not in vals_int:
            return int(j)


q = int(input())

print(juvenal(q))
