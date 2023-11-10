

def multiplie(x, y):
    if x == 0:
        return 0
    if x%2==0 and x > 0:
        return multiplie(x/2 * 2*y, 1)
    else:
        return multiplie((x-1)/2 * 2*y, 1)


