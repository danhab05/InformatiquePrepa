
def division(L):
    global L1, L2
    n = len(L) // 2
    L1 = L[:n]
    L2 = L[n:]
    return L1, L2

# Q1 done
def fusion(L1, L2):
    L = []
    i = 0
    j = 0
    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            L.append(L1[i])
            i += 1
        else:
            L.append(L2[j])
            j += 1
    return L+L1[i:] + L2[j:]


def tri_fusion(L):
    if len(L) == 1:
        return L
    L1, L2 = division(L)
    return fusion(tri_fusion(L1), tri_fusion(L2))

import random as rd
L = [i for i in range(20)]
rd.shuffle(L)
print(L)
# L1, L2 = division(L)
# L1, L2 = [1, 2, 6], [3, 5, 9]
# print(fusion(L1, L2))
print(tri_fusion(L))