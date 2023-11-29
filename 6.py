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