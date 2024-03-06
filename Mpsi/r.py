def isHappy(n):
# def isHappy(self, n):
    old = []
    while True:
        print(n)
        n = summ(n)
        if n in old:
            break
        old.append(n)

    if n == 1:
        return True
    return False

def summ(n):
# def summ(self, n):
    num = str(n)
    nnn = 0
    for el in num:
        nnn += int(el)**2
    return nnn


def isHappyRec(n):
    if n == 1:
        return True
    




print(isHappy(3))