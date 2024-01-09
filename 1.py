tarif = float(input("entrée le prix du produit : "))
if tarif < 20 :
    result = tarif * 1.10
elif tarif >= 20 and tarif < 50 :
    result = tarif*1.075
elif tarif >=50 and tarif < 100:
    result = tarif*1.05
else:
    result = tarif*1.025
print("le prix est monté a :",result)
