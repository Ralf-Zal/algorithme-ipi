tab = [10,23,53,54,4,8,3,1,78,10]
i = 0
a = 0
while i <= 9:
    if tab[i] >= 10:
        a = a + 1
    else:
        a = a + 0
    i = i+1

print("le nombres d'élève ui ont obtenue la moyennes  est :",a)
