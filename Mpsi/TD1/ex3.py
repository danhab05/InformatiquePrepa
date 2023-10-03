def comptage(it):
    D = {}
    for x in it:
        if x not in D:
            D[x] = 1
        else:
            D[x] += 1
    return D

# print(comptage([2,5,6, 6, 6]))


"""
 Question 1, la fonction comptage stocke 
 dans un dictionnaire le nombre de fois ou un 
 element est present. Et les stock sous forme de valeurs le nombre d'iteration 
 associé a la clé qui stock l'element 
"""

alphabet = "abcdefghijklmnopqrstuvwxyz"

def encodeCesar(chaine, n):
    encoded = ""
    for el in chaine:
        if el in alphabet:
            i = alphabet.index(el)
            encoded += alphabet[(i+n)%26]
    return encoded

def decode(chaine, n):
    return encodeCesar(chaine, -n)


# msg = encodeCesar("salutwxyz", 15)
# print(msg)
# print(decode(msg, 15))


def decodeCesarAuto(chaine):
    finalAtThistime = "e"
    for n in range(25):
        encoded = ""
        for el in chaine:
            if el in [" "]:
                encoded += " "
            elif el in [ ","]:
                encoded += ","
            else:
                if el in alphabet:
                    i = alphabet.index(el)
                    encoded += alphabet[(i+n)%26]
        try:
            if comptage(encoded)["e"] > comptage(finalAtThistime)["e"]:
                finalAtThistime = encoded
        except:
            pass
    return finalAtThistime


print(decodeCesarAuto("azgdxdovodjin, ezpiz kzmnjiiz, nd qjpn gdnzu xz ozsoz xzgv diydlpz lpz qjpn vqzu np yzxjyzm gz xjyz yz xznvm, xjiodipzu v qjpn zszmxzm zi ktocji, qjpn mzgzqzmzu ojpn gzn yzadn"))










