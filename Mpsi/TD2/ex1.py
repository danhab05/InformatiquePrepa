def occurence(mots, texte, i):
    if len(mots) - len(texte) < i:
        return False
    for k in range(len(mots)):
        if texte[i+k] != mots[k]:
            return False
    return True
     
print(occurence("test", "Ceci est un test", 12))
# Q1 done

def recherche_occurence(mots, texte):
    l = []
    for i in range(len(texte)):
        if occurence(mots, texte, i):
            l.append(i)
    return l
# Q2 done
print(recherche_occurence("bonbon", "bonbonbon"))