def p(a,b):
    if b == 0:
        return a
    return p(a+1, b-1)

# cette fonction renvoie la somme b+a

print(p(2,99))

def q(a,b):
    if b == 1:
        return a
    return a+q(a,b-1)

print(q(2,99))
# cette fonction renvoie le produit b*a
