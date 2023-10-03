import numpy
from random import randint

def deux_ppv(L):
    value = abs(L[0] - L[1])
    for i in range(len(L) - 1):
        if abs(L[i+1] - L[i]) > value:
            value = (L[i+1], L[i])
    print(value)

deux_ppv([23,418,126,30])
                              
