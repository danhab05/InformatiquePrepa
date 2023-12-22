def insertion(L, x, n):
    if x > L[n-1]:
        L[n] = x
    else:
        L[n] = L[n-1]
        insertion(L, x, n-1)
    
    

        
def triinsertion(L, n):
    