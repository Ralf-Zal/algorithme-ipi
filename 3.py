date1 = input("saisir une première date(exemple 10/12/2024) : ")
year1 = int(date1[6:])
month1 = int(date1[3:5])
day1 = int(date1[0:2])
print(day1,month1,year1)
date2 = input("saisir une deuxieme date : ")
year2 = int(date1[6:])
month2 = int(date1[3:5])
day2 = int(date1[0:2])
if year1 > year2:
    print("la premiere date est la plus récente")
elif year1 < year2:
    print("la deuxième date est la plus récente")
else:
    if month1 > month2:
        print("la premiere est date la plus récente")
    elif month1 < month2:
        print("la deuxième date est la plus récente")
    else:
        if day1 > day2:
            print("la premiere date est la plus récente")
        elif day1 < day2:
            print("la deuxième date est la plus récente")
        else:
            print("les deux dates sont identique")
