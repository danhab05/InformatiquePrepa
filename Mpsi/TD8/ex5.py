# Q1
def minimum(L):
    minEl = L[0]
    for el in L[1:]:
        if el < minEl:
            minEl = el

    return minEl

def maximum(L):
    maxEl = L[0]
    for el in L[1:]:
        if el > maxEl:
            maxEl = el

    return maxEl

# Q2
def comptage(it):
    D = {}
    for x in it:
        if x not in D:
            D[x] = 1
        else:
            D[x] += 1
    return D

def tri_denombrement(m, M):
    L2 = []
    for a in range(m, M+1):
        if a in dic:
            n = dic[a]
            L2 += [a]*n
    return L2
L = [2, 3, 8, 7, 1, 2, 2, 0, 7, 3, 9, 8, 2, 1]
M, m, dic = maximum(L), minimum(L), comptage(L)
print(tri_denombrement(m, M))
