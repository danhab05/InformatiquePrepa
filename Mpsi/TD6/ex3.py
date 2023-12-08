def valeur(objet):
    return objet[2]


def invPoids(objet):
    return 1 / objet[1]


def rapport(objet):
    return objet[2] / objet[1]


def glouton(listeObjet, poidsMax, choix):
    poidsTot, valTot, selection = 0, 0, []
    nbObjects = len(listeObjet)
    listeObjetTrie = sorted(listeObjet, key=choix, reverse=True)
    for i in range(nbObjects):
        objet = listeObjetTrie[i]
        poidAvecObjet = poidsTot + objet[1]
        if poidAvecObjet <= poidsMax:
            poidsTot, valTot = poidAvecObjet, valTot+objet[2]
            selection.append(objet[0])
    return poidsTot, valTot, selection
