def minimum(L, i):
    minList, indice = L[i], i
    for k in range(i+1, len(L)):
        if L[k]<=minList:
            minList, indice = L[k], k 
    return indice

# print(minimum([5,1,-8,2,-4,7], 3))
# Q1 done

def echange(L, i, j):
    L[i], L[j] = L[j], L[i]

L = [5,1,-8,2,-4,7]
# echange(L, 2, 4)
# print(L)
# Q2 done

def tri_selection(L):
    for i in range(len(L) - 1):
        indice = minimum(L, i)
        echange(L, i, indice)

tri_selection(L)
print(L)
# Q3 done

def tri_selection(L):
    for i in range(len(L) - 1):
        indice = minimum(L, i)
        echange(L, i, indice)
