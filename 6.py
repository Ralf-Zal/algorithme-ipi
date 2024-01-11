tab = [2,5,60,20,31,14,2,8,9,42]
number = int(input("entrée le nombre que vous voulez chercher : "))
i = 0
nombre_total = 0
while i <= 9:
    if tab[i] == number :
        nombre_total = nombre_total+1
    i = i + 1
if nombre_total > 0:
    print("votre nombre est présent ",nombre_total," de fois")
else:
    print("votre n'existe pas dans le tableau")
