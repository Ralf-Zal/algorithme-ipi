#Comparaison de 2 offres téléphoniques
#Vous êtes opérateur téléphonique et vous proposez deux offres à vos clients. 
#1 ère offre : coût fixe de 10 euros + coût variable de 0.05 euros par heure consommée
#2 ème offre : coût fixe de 20 euros + coût variable de 0.02 euros par heure consommée
#Demandez à votre client quelle est sa consommation habituelle en heures et proposez lui l’offre la plus avantageuse pour lui.
 
conso = float(input("quel est votre consomation habituel : "))
offer1 = 10 + conso * 0.05
offer2 = 20 + conso * 0.02
if offer1 < offer2 :
    print("la 1ere offre est plus rentable")
else:
    print("la 2eme ofre est plus rentable")