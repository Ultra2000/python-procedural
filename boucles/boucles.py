# for x in range(10):
#     print(f"{x} bière")
#La boucle for permet de répéter une instruction un certain nombre de fois.
for x in range(1, 3):
    print(f"{x} bière")

capacite_max = 10
capacite_actu = 3

#La boucle while permet de répéter un instruction(s) jusqu'a ce qu'une certaine condition soit remplie
while capacite_max > capacite_actu:
    capacite_actu += 1

    print(capacite_actu) 


#l'instruction break est utilisée pour interrompre une boucle avant qu'elle ne se termine.

#l'instruction continue est utilisée pour sauter une itération de boucle et passer à littération suivante.