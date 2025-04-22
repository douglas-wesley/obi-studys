def pla(X,N):
    new_quote = X 
    for _ in range(N):
        i = int(input())
        old_quote = new_quote-i 
        new_quote = old_quote + X
    return new_quote 

q = int(input())
p = int(input())

print(pla(q,p))


