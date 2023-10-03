import re
f = open ("ainsi_parlait_zarathoustra.txt", "r", encoding ="utf -8")
texte = f . read ()
texte = re.sub(r'[^\w\s]', ' ', texte)
liste_mots = texte.split()
f.close()

def comptage(it):
    D = {}
    for x in it:
        if x not in D:
            D[x] = 1
        else:
            D[x] += 1
    return D

# print(comptage(liste_mots))
# Q1

def plusFrequent(d, k):
    higherRank = 0
    motPlusUtilise = ""
    for mots in d.keys():
        if len(mots) == k:
            if d[mots] > higherRank:
                higherRank = d[mots]
                motPlusUtilise = mots
            
    return motPlusUtilise

# print(plusFrequent(comptage(liste_mots), 7))
# Q2, le mots le plus frequent est "volonté"


def plusFrequentK(d):
    dicMots = {}
    for k in range(1, 29):
        higherRank = 0
        motPlusUtilise = ""
        for mots in d.keys():
            if len(mots) == k:
                if d[mots] > higherRank:
                    higherRank = d[mots]
                    motPlusUtilise = mots
        if higherRank != 0:
            dicMots[motPlusUtilise] = higherRank

    return dicMots

dicMotTaille = plusFrequentK(comptage(liste_mots))
print(dicMotTaille)
# q3 le mots le plus long a 16 lettres