# question 1
def maximum(L):
    n = len(L)
    maxi = L[0]
    for i in range(1, n):
        if L[i] > maxi:
            maxi = L[i]
    return maxi
        
def maximum_pos(L):
    n = len(L)
    maxi = L[0]
    
    for i in range(1, n):
        if L[i] > maxi:
            maxi = L[i]
    return maxi, i
        
print(maximum_pos([2, 5, 22, 5, 0]))


# question 2
def premier_deuxieme_maximum(L):
    n = len(L)
    m1, m2, p1, p2 = L[0], L[1], 0, 
    if m2 > m1:
        m1, m2, p1, p2 = m2, m1, p2, p1
    for i in range(2, n):
        e = L[i]
        if e > m1:
            m1 = e
            p1 = i
        elif e > m2:
            m2 = m1
            p2 = i
    return (m1, p1), (m2, p2)

print(premier_deuxieme_maximum([2, 88, 67, 9, 10 ]))