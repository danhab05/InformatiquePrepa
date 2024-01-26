from random import randint

def insertion(L, x, n):
    if n == 0 or x > L[n-1]:
        L[n] = x
    else:
        L[n] = L[n-1]
        insertion(L, x, n-1)
    
    
def tri_insertion(L, n):
    if n > 1:
        tri_insertion(L, n-1)
        insertion(L, L[n-1], n-1)

L = [randint(0,99) for _ in range(40)]
print(L)
tri_insertion(L, len(L))
print(L)


def premier(n):
    L = list(range(3, n+1))
    k = [2]
    