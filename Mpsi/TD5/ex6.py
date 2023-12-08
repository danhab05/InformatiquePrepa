import matplotlib.plt as plt
from math import *


def polygone(*args):
    X, Y = []
    for arg in args:
        X.append(arg[0])
        y.append(arg[1])
    plt.fill(X, Y, 'b')
    
    
polygone((0,0), (1,0), (0.5))