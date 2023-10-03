
# Question 1
def recherche(L, e):
    for x in L:
        if x == e:
            return True
    return False

# print(recherche([2,3,5], 5))

# question2: 2n+1

# question 3
def nb_occurences(L, e):
    count = 0
    for x in L:
        if x == e:
            count += 1
    return count

print(nb_occurences([1,2,3,1,6,2,1,3,3,2,3,5,1], 3))



