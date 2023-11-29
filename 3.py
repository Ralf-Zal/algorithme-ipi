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
#Calculez le montant de la TVA en appliquant un taux de TVA de 20%, et affichez ce montant de TVA.
#Calculez le montant TTC de type réel et affichez-le. 