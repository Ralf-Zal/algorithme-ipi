candidat = int(input("saisir le nombre de voit que possède l'élève"))
if candidat < 5:
    print("candidat éliminé")
elif candidat >= 5 and candidat < 50: 
    print("qualifié second tour")
else:
    print("élus")
