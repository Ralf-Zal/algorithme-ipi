tab = [1,20,5,3,1,6,8,9,4,50]
i = 0

while i <= 9:
    b = tab[i]
    a = tab[i] / 2
    a = str(a)
    a = a.find(".5")
    if a == 1:
        print(b,"est impaire")
    elif a == -1:
        print(b,"est pair")
    i = i+1
