# À exécuter une fois pour toute
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
#import os

# changement du répertoire de travail. Modifier de façon à indiquer le répertoire où se trouvent les images.
#os.chdir('/home/Dropbox/cours/info/python/')

## Exemples pour le chargement et l'affichage d'une image

# charge une image sous forme de liste de listes
image = (mpimg.imread('./guepiersNB.jpg')).tolist()
# affichage des dimensions de l'image
print('w=', len(image[0]),' h=', len(image))
# affichage de l'image
plt.imshow(image, cmap='gray', clim=(0,255))
plt.show()

## Pour se chauffer...

def dim(img:list) -> tuple:
    '''Renvoie le couple (largeur,hauteur) de l'image'''



## Réduction de moitié de la largeur (version naïve)

def reduction_moitie_ligne(l:list) -> list:
    pass

def reduction_moitie_image(img:list) -> None:
    pass

# test
image = (mpimg.imread('./guepiersNB.jpg')).tolist()
reduction_moitie_image(image)
plt.imshow(image,cmap='gray',clim=(0,255))
plt.show()

## Calcul de l'énergie

def energie(img:list) -> list:
    '''Calcule l'énergie d'une image img'''
    pass
    
        
      
## Manipulations de listes

def enlever(l:list,i:int) -> list:
    pass
    
def indice_min(l:list) -> int:
    pass

## Réduction ligne par ligne
# À partir d'ici, il est demandé de compléter les signatures des fonctions

def reduction_ligne_par_ligne(img):
    pass
    
def itere_reduction_ligne_par_ligne(img, n):
    pass
    

## Réduction par colonne

def meilleure_colonne(e):
    pass
    
def reduction_meilleure_colonne(img):
    pass
    
def itere_reduction_meilleure_colonne(img, n):
    pass
    

## Seam carving

def energie_chemins_partiels(e:list) -> list:
    """Calcule l'image des énergies des meilleurs chemins partiels du haut de l'image jusqu'à chaque pixel. e est une image des énergies."""
    pass


def indice_min_entre(l:list, d:int, f:int) -> int:
    """Renvoie un indice où apparaît le minimum d'une liste non vide de nombres l entre les indices d (inclus) et f (exclu)."""
    pass


def chemin_minimal(e:list) -> list:
    """Calcule un chemin d'énergie minimale dans une image des énergies e. Le résultat renvoyé est la suite des abscisses des pixels du chemin, de bas en haut"""
    pass


def seam_carving(img:list, n:int) -> None: 
    """applique n fois le retrait de chemin minimal à l'image img. Effet de bord : modifie l'image"""
    pass


