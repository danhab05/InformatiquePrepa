from random import randint

def deux_ppv(L):
    value = abs(L[0] - L[1])
    for i in range(len(L)):
        for j in range(i + 1, len(L)):
            if abs(L[i] - L[j]) < value:
                ppv = L[i], L[j]
                value = abs(L[i] - L[j])
    return ppv

print(deux_ppv([29, 23,418,126,30]))
                              
