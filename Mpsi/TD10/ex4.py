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
# print(from_base10(2, 13))

def from_base10rec(b, n):
    if n == 0:
        return n%b
    q = n//b
    r = n%b
    return from_base10rec(r, q)

def add(L1, L2, b):
    n1, n2 = len(L1), len(L2)
    if n1 > n2:
        L1, L2 = L2, L1
    L1= [0]*(n1-n2) + L1
    Lsomme = []
    L1.reverse()
    L2.reverse()
    retenue = False
    for i in range(n1):
        s = L1[i] + L2[i]
        if retenue:
            s += 1
            retenue = False
        if 0 <= s <=1:
            Lsomme.append(s)
        else:
            Lsomme.append(0)
            retenue = s // 
    # for element in L2[:n2]:
    #     Lsomme.append(element)
    Lsomme.reverse()
    return Lsomme

# print(add([1, 0, 0, 1], [1, 1], 3))

def mult(L1, L2, b):
    Ltot = []
    for i in range(len(L2)):
        L = [L1[k]**L2[i] for k in range(len(L1))]
        Ltot.append(L)
    Ltot[1] = [0] + Ltot[1]
    Ltot[1].reverse()
    Ltot[0].reverse()

    return add(Ltot[1],  Ltot[0], b)
# print(mult([1, 0, 0, 1], [1, 1], 2))
# print(mult([1,1,0,1], [1, 0, 1], 10))