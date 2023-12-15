import numpy as np
import matplotlib.pyplot as plt

imPath = "tigre.bmp"
imTigre = plt.imread(imPath)
imTigre = imTigre.astype(int)


def affiche(image):
    plt . close()  # ferme les fenê tres graphiques déjà ouvertes
    plt . imshow(image)
    plt . show()


def carre(m):
    n = 256
    nLig, nCol, nCoul = m.shape
    im_copie = np.zeros((n, n, nCoul), dtype=int)
    for i in range(n):
        for j in range(n):
            im_copie[i][j] = m[nLig//2 - n//2 + i][nCol // 2 - n//2 + j]

    return im_copie

image_carre = carre(imTigre)
affiche(image_carre)
def rotation_aux(m, x, y, t):
    if t == 1:
        return None
    t = t//2
    rotation_aux(m, x, y, t)
    rotation_aux(m, x+t, y, t)
    rotation_aux(m, x, y+t, t)
    rotation_aux(m, x+t, y+t, t)

    for                                                                          



