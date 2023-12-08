def rendu_monnaire(s, P):
    liste_somme = []
    i = len(P) - 1
    while s > 0:
        if s >= P[i]:
            liste_somme.append(P[i])
            s -= P[i]
        else:
            i -=1
    return liste_somme


    print(liste_somme)


p = [1,2,5,10,20,50,100,200,500]
s = 493
# p = [1,3,6,12,24,30]
# s = 48
rendu_monnaire(s, p)
