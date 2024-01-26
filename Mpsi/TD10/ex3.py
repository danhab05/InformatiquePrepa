def to_base10(b, L):
    b10 = 0
    n = len(L)
    for i in range(n):
        b10 += b**(n-i-1)*L[i]
    return b10

        
    
def from_base10(b, n):
    L = []
    q = n // b
    r = n % b
    while n != 0:
        q = n // b
        r = n % b
        n = q
        L.append(r)
    L.reverse()
    return L
print(from_base10(2, 13))

def from_base10rec(b, n):
    if n == 0:
        return n%b
    q = n//b
    r = n%b
    return from_base10rec(r, q)

print(from_base10rec(2, 13))
