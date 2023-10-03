import os
import matplotlib.pyplot as plt
print(os.getcwd())
from numpy import *
f = open(os.getcwd() + "/notes.csv", "r")
l = []
for el in f.readlines():
    l.append(float(el.strip()))
l = array(l)
# Q1 done

def moyenne(L):
    som = float(0)
    for el in L:
        som += el
    return som/len(L)
print(moyenne(l))
# Q2 done

def ecart_type(L):
    moy = moyenne(L)
    som = 0
    for el in L:
        som += (el - moy)**2

    return sqrt(som/len(L))
print(ecart_type(l))
# Q3 done

lnum = array(l)
print(mean(lnum))
print(std(lnum))
# Q4
def traitement_note(note, ecs, mos):
    note_modifie = (ecs*(note-moyenne(l))/ecart_type(l)) + mos
    return note_modifie
print(traitement_note(2, 10, 12))
# Q5
plt.hist(l*100/len(l), bins=21, range=(0,20), label="version 1", color="magenta")
plt.yticks(arange(0,22,2))
# plt.xticks()
plt.ylabel("Notes")
plt.xlabel("Nombre d'eleves")
plt.title("Histogramme des notes")
plt.legend()
plt.show()