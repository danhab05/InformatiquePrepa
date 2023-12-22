def partitiontonton(L):
    p = len(L) - 1
    pivot = L[p]  # dernier element de la liste
    n = len(L)
    i = 0
    j = p - 1
    while i < j:
        if L[i] > pivot:
            if L[j] < pivot:
                L[i], L[j] = L[j], L[i]
            else:
                j -= 1
        else:
            i += 1 
    L[i], L[p] = L[p], L[i]
    
# L = [22,11,88,66,55,77,33,44]
# partitiontonton(L)
# print(L)
        
        
def partition(L, g, d):
    pivot = L[g] 
    j = d
    i = g+1
    while i <=j: 
        if L[i] > pivot:
            if L[j] < pivot:
                L[i], L[j] = L[j], L[i]
            else:
                j -= 1
        else:
            i += 1 
            
    L[j], L[g] = L[g], L[j]
    return j

# L = [8,4,18,11,15,5,17,1,10,7] # pivot = 8
# partition(L, 0, 9)
# print(L)
        
def tri_rapide(L, *args):
    if args == ():
        g,d = 0, len(L) - 1
    else:
        g,d = args
    if len(L) <= 1:
         return 
    if g < d:
        i = partition(L, g, d)
        tri_rapide(L, g, i)
        tri_rapide(L, i+1, d)


L = [8,3,6,2,5,9,4,7]
print(L)
tri_rapide(L)
print(L)


