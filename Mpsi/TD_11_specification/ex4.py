def appartient(v, L):
    for i in range(len(L)):
        if L[i] == v:
            trouvee  = True
        else:
            trouvee = False
    return trouvee

assert appartient(5, [1,2,3,5,2])

    