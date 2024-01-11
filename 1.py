#Faîtes saisir 3 nombres entiers.
#Rédigez l’algorithme qui permet de calculer la somme et la moyenne des 3 nombres saisis

a = input("saisir 3 nombres :")
a = a.split(" ")
a[0] = int(a[0])
a[1] = int(a[1])
a[2] = int(a[2])

r = a[0]+a[1]+a[2]
r = r/3
print(r)
