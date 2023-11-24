def puissance(a,n):
    if n == 0:
        return 1
    return a * puissance(a, n-1)
# Q1 ok

def exp_rap(a, n):
    if n == 0:
        return 1
    if n%2 == 0:
        return a*exp_rap(a, n//2)

    return a*exp_rap(a*a, (n-1)//2)


print(exp_rap(3,3))
