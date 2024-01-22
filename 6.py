#Notes Faîtes saisir une note sur 20, de type réel.
#Convertissez cette note en lettre selon le tableau ci-dessous et affichez la lettre qui correspond à la note.
#Note <= 5 Lettre E 5 < Note <= 8 Lettre D 8 < Note <= 11 Lettre C 11 < Note <= 14 Lettre B 14 < Note Lettre A
while True :
    note = float(input("entré la note de l'élève : "))
    if note <= 5 and note >= 0:
        print("E")
    elif note > 5 and note <= 8 :
        print("D")
    elif note > 8 and note <= 11 :
        print("C")
    elif note > 11 and note <= 14 :
        print("B")
    elif note > 14 and note <= 20 :
        print("A")
    else:
        print("la note ne peut etre inférieur a 0 et supérieur a 20")  
