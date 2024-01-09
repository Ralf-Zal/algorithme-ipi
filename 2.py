qte = int(input("saisir la quantité de votre produit: "))
question = input("voulez que votre livrasons soit rapide : ")
if qte < 50:
    if question == "oui" :
        print("2jour")
    else:
        print("4jour")
elif qte >=50 and qte < 100:
    if question == "oui":
        print("3jour")
    else:
        print("5jour")
else:
    if question == "oui":
        print("5jour")
    else:
        print("7jour")
