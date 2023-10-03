from random import randint

characteres = "abcdefghijklmnopqrstuvwxyz "
def generation_texte_ameatpore(N):
    char = ""
    for i in range(N):
        char += characteres[randint(0, 26)]
    return char
print(generation_texte_ameatpore(40))
# Q1 done

