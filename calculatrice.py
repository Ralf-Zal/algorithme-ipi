i = 0
n1 = int(input("choisir un nombre : "))
while i <= 2 :
    calc = input("choisir  la méthode (/ | + | - | * | 'stop')")
    if calc == "/"  or calc == "+" or calc == "-" or "*":
        n2 = int(input("chosir un autre nombre"))
        if calc == "/":
            result = n1 / n2
        elif calc == "+":
            result = n1 + n2
        elif calc == "-":
            result = n1 - n2
        elif calc == "*":
            result = n1 * n2
        elif calc == "stop":
            break
        else:
            break
        print("le calcul vaut : ",result)
        while i <= 2:
            calc = input("choisir  la méthode (/ | + | - | * | 'stop')")
            if calc == "/"  or calc == "+" or calc == "-" or "*":
                n2 = int(input("chosir un autre nombre"))
                if calc == "/":
                    result = result / n2
                elif calc == "+":
                    result = result + n2
                elif calc == "-":
                    result = result - n2
                elif calc == "*":
                    result = result * n2
                elif calc == "stop":
                    break
                else:
                    break
                print("le calcul vaut : ",result)
            
        break
    break
