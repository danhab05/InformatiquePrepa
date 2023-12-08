import numpy as np
import matplotlib.pyplot as plt

# il faut ehcanger le pixel avec son symetrique par rapport a l'axe verticale 
# liés au centre de limage

def sym_vert(image):
    imCp = image.copy()
    for i in range(len(imCp)):
        for j in range(len(imCp[1])):
            r, v, b = imCp[i][j]
            
            imCp[i][j] = np.array([r, v, b])
    return imCp

imPath = "paris.jpg"
paris = plt.imread(imPath)
paris = paris.astype(int)
parisReverse= sym_vert(paris)
# parisReverse = paris
plt.imshow(parisReverse)
plt.show()