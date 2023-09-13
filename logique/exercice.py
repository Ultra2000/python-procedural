nombre1 = 20
nombre2 = 10



if nombre1 and nombre2 :
    operation = "-"
    match operation:
        case "-":
            resultat = nombre1 - nombre2
            print(f"{nombre1} - {nombre2} = {resultat}")
        case "+":
            resultat = nombre1 + nombre2
            print(f"{nombre1} + {nombre2} = {resultat}")
        case _:
            print("Opérateur non reconnu")
else:
    print("Les nombres ne sont pas valide non valide")