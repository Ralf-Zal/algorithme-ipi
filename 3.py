#Faîtes saisir une quantité de produits de type réel, et affichez la.
#Faîtes saisir un prix unitaire hors-taxes de type réel, et affichez le.
#Calculez le montant total hors-taxes de type réel, et affichez-le.
#Appliquez une remise selon le tableau ci-dessous et affichez le prix remisé de type réel.
#Montant total hors-taxes < 200 Taux de remise : 2,5 % 
#200 <= Montant total hors-taxes < 400 Taux de remise : 5 % 
#400 <= Montant total hors-taxes < 700 Taux de remise : 7,5 % 
#700 <= Montant total hors-taxes Taux de remise : 10 % 
#Calculez le montant de la TVA en appliquant un taux de TVA de 20%, et affichez ce montant de TVA.
#Calculez le montant TTC de type réel et affichez-le.
qte = int("saisir une quantité : ")
ht = float("saisir le prix HT : ")
tc = qte * ht
if tc < 200:
    tc *10/0.025
if tc < 400 and tc > 200 :
    tc * 10 / 0.05
if tc < 700 and tc > 400 :
    tc * 10 /0.075
else:
    tc * 10 / 0.010
