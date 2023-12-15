def insert(L, i, val):
    while L[i]>val and i > -1:
        L[i+1] = L[i]
        i -= 1
    L[i+1] = val

# L = [2, 2, 4, 5, 66, 22, 20, 21]
# print(L)
# insert(L, 3, 3)
# print(L)

def tri_insertion(L):
    for i in range(1, len(L)):
        val = L[i]
        insert(L, i-1, val)

L = [2, 1, 5, 66, 22]
tri_insertion(L)
print(L)