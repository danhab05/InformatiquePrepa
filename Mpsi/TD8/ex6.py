def valPlusFreq(L):
    c, v = 1, L[0]
    cmax = 1
    for el in L[1:]:
        print(c)
        if el == v:
            c+=1
        else:
            if c > cmax:
                cmax = c
                vf = el
            v, c = el, 1
    if c > cmax:
        vf, cmax = el, c
            
        
    return vf, cmax
print(valPlusFreq([1,2,2,2,5,6]))