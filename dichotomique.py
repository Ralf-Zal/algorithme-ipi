#Exercice à réaliser
#-Soit le tableau suivant : [1, 1, 2, 3, 5, 8, 13, 21, 34]
#-Faites saisir un entier et dites s’il est présent dans le tableau ci-dessus, et si oui à quelle position,
#en utilisant la méthode de la recherche dichotomique. 
tab = [1, 1, 2, 3, 5, 8, 13, 21, 34]
i = round(len(tab) / 2)
inf = 0
maximum = len(tab)-1
print(i)
print(maximum)
number = int(input("saisir votre nombre : "))
if number == tab[i]:
    print("votre nombre se trouve dans le tab[",i,"]")
elif number > tab[i] :
    while i  != maximum:
        if number == tab[i]:
            print("votre nombre se trouve dans tab[",i,"]")
            break
        i= i+1
elif number < tab[i] :
    while i  != 0:
        if number == tab[i]:
            print("votre nombre se trouve dans tab[",i,"]")
            break
        i= i-1
if number != tab[i] and i == 0 or number != tab[i] and i == maximum:
    print("le nombre n'est pas dans le tableaux")
