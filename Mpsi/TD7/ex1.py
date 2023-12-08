import numpy as np
import matplotlib.pyplot as plt
def affiche ( image ) :
    plt . close () # ferme les fenê tres graphiques déjà ouvertes
    plt . imshow ( image )
    plt . show ()
def q1Paris():
    # pour paris:
    imPath = "paris.jpg"
    paris = plt.imread(imPath)
    paris = paris.astype(int)
    parisBlue = paris.copy()
    for i in range(50, 400):
        for j in range(250, 450):
            parisBlue[i][j] = np.array([0,0, 255])
    plt.imshow(parisBlue)
    plt.show()

def q1Tigre():
    # pour tigre
    imPath = "tigre.bmp"
    tigre = plt.imread(imPath)
    tigre = tigre.astype(int)
    tigreBlue = tigre.copy()
    for i in range(50, 400):
        for j in range(250, 450):
            tigreBlue[i][j] = np.array([0,0, 255])
    plt.imshow(tigreBlue)
    plt.show()

def inverse(im):
    imCp = im.copy()
    for i in range(len(imCp)):
        for j in range(len(imCp[1])):
            r, v, b = im[i][j]
            imCp[i][j] = np.array([255-r, 255-v, 255-b])
    return imCp


def saturer(im, seuil):
    imCp = im.copy()
    for i in range(len(imCp)):
        for j in range(len(imCp[1])):
            r, v, b = im[i][j]
            r = 255 if r > seuil else 0
            v = 255 if v > seuil else 0
            b = 255 if b > seuil else 0
            imCp[i][j] = np.array([r, v, b])
    return imCp

imPath = "paris.jpg"
paris = plt.imread(imPath)
paris = paris.astype(int)
parisReverse= saturer(paris, 127)
affiche(parisReverse)

def f(x):
    y = x + 0.4*(x-127)
    if y > 0 and y < 255:
        return y
    elif y <= 0:
        return 0
    else:
        return 255
#  car elle 

def contraste(im, f):
    imCp = im.copy()
    for i in range(len(imCp)):
        for j in range(len(imCp[1])):
            r, v, b = im[i][j]
            r = int(f(r))
            v = int(f(v))
            b = int(f(b))
            imCp[i][j] = np.array([r, v, b])
    return imCp



# imPath = "paris.jpg"
# paris = plt.imread(imPath)
# paris = paris.astype(int)
# parisReverse= contraste(paris, f)
# # parisReverse = paris
# plt.imshow(parisReverse)
# plt.show()