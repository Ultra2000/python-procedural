#Utilisation des expressions logiques AND, NOT, OR

ensoilelle = True

en_semaine = True

if ensoilelle and en_semaine:
    print("Nous allons au boulot les gars")
elif ensoilelle and not en_semaine:
    print("Nous allons à la plage")
else:
    print("Bah finalement nous restons à la maison")