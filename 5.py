tab = [2,5,60,20,31,14,2,8,9,42]
petit_nombre = 9999
grand_nombre = 0
a = 0

while a <= 9:
    if petit_nombre > tab[a]:
        petit_nombre = tab[a]
    if grand_nombre < tab[a]:
        grand_nombre = tab[a]
    a = a + 1
print(petit_nombre,"est le plus petit et ",grand_nombre,"est le plus grand")
