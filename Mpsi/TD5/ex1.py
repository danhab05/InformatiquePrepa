def maxi_iter(l):
    elmax = l[0]
    for it in l:
        if it > elmax:
            elmax = it
            
    return elmax

def maxi_rec(l):
    if len(l)==1:
        return l[0]
    
    mf = maxi_rec(l[1:])
    if l[0]>mf:   
        return (l[0])
   
    return mf
    
def maxi_rec2(l, i=0):
    if len(l)-1==i:
        return l[i]
    
    mf = maxi_rec2(l, i+1)
    if l[i]>mf:   
        return (l[i])
    return mf


print(maxi_rec2([5555,34,572,555,2,2, 222], 4))
