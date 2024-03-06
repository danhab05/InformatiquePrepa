def somme(n:int) -> int:
    s = 0
    for k in range(1, n+1):
        s += k
    return s    
# print(somme(5))


def indicie_minimum(l:list, j:int=0) -> int:

    minList, indice = l[j], j
    for k in range(j+1, len(l)):
        if l[k]<=minList:
            minList, indice = l[k], k 
    return indice

# print(indicie_minimum([12,52,3,2323,6,2,21,55], 6))

def tri_selection(l):
    
    for j in range(len(l) - 1):
        mini = indicie_minimum(l, j)
        l[j], l[mini] = l[mini], l[j]

"""
On propose l'invariant suivant, en sortie de l'iteration j, le tableau l[:j+1] est trié et 
ses éléments sont plus petits que ceux de l[j+1:]

Initialisation: j = 0, l[:0] est vide, donc trié et l[0:] est le tableau complet, donc l'invariant est vrai

Conservation: on suppose que l[:j] est trié et que l[j:] est plus grand que l[j:]
    - L'iteration j+1, va placer les elements de l[:j+1] a la fin de la partie triée
    donc L[j+1:] 

Sortie de la boucle:
    - Derniere valeur de i, i = len(l) - 2, l[:len(l) - 2 + 1] = l[:len(l) - 1] et comme les elements de 
    l[:len(l) - 2] sont plus grands, sachant qu'il y en a que 1 la liste l est donc triée

conclusion: 
    - L'algorithme conduit bien au resultat souhaité

"""

# tri_selection([2,533,3,52,1,3535,533])


def fact(n):
    if n == 1:
        return n

    return n * fact(n-1)


# 
# 
# (fact(3))

"""
    Init: Si n = 1, on a 1! = 1 cest bon

    On suppose que fact(n-1) donne (n-1)!

    l'appel fac(n) donne donc nfact((n-1))=n*(n-1)! = n!

"""



def exp_rap(a,n):
    if n == 0:
        return 1

    if n % 2 == 0:
        return exp_rap(a*a, n//2)
  
    return a * exp_rap(a*a, (n-1)//2)

"""
On prend pour variant de boucle, n

"""

"""
Si n = 0, on a a^0 = 1 cest bon

si exp(a, n-1) = a^(n-1) vrao

alors exp(a, n) = 
                    - exp(a, n) = (a^2)^(n/2) = a^n
                    - exp(a, n) = a*(a^2)^((n-1)/2) = a^n

"""



def multiplie(x,y):
    if x == 0:
        return 0
    if x % 2 == 0:
        return multiplie(x//2, y+y)
    return multiplie((x-1)//2, y+y) + y

"""
On prend pour variant de boucle x qui diminue
ic
"""


def fonction ( n ) :
# l’ argument n doit être un entier naturel
    r = 2
    i = 0
    while i < n :
        r = r * r
        i = i + 1
    return r

print(fonction(3))
"""
1) il semble que ca renvoie 2^2^n
"""

"""
2) si n = 0 alors n-i = 0 donc on renvoi 2 c qui est bien 2^2^0
prenons n-i comme variant, dans le pire des cas i vaut n-1 donc le variant vaut 1 donc la boucle s'arrete
"""

"""
3)init: 2^2^0 = 2 ce qui est bien renvoyé

suposons que ri = 2^2^i

ri+1 = ri * ri = 2^2^i * 2^2^i = 2^2^(i+1) donc c bon

terminaison: dans le pire des cas i vaut n-1 donc r = 2^2^(n-1) donc rn = 2^2^n ce qui est bien ce que lon cherche c bon
"""


def maximum ( L ) :
    maxi = L [0]
    for i in range (1 , len( L ) ) :
        if L [ i ] > maxi :
            maxi = L [ i ]
    return maxi
    
"""
boucle for donc ca se termine
"""

"""
on propose, maxi contient le macimum de L[:i] a chaque debut diteration 

init: avant la premiere iteration, i vaut 1 donc L[:1]= [L[0]] ce qui est bien le max

on suppose maxi contient le max de  L[:i]
si L[i+1] > maxi alors on stock maxi = L[i+1]
sinon on conserve la valeur precedente
on obtient donc maxi qui vaudra le max de L[i+1]

en sortie de boucle i vaut len(L) - 1 donc maxi est le max de L[:len(L) -1]
on verifie a nouveau et on obtiendra

maxi est le mac de L[:len(L)]=L donc max est bien lelement max de la liste 

"""