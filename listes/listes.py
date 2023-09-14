#Créons une liste/Tableau 
plateformes_sociaux = ["facebbok", "whatsapp", "instagram", "twitter"]
#Affichons un élément de la liste grâce à son indice. ici nous avons pris l'indice [O]
print(plateformes_sociaux[0])

#Modification de la valeur d'un élément de la liste en choisissant son indice;
plateformes_sociaux[2] = "Linkedin"
print(plateformes_sociaux)

# Ajoutons à la liste plateformes_sociaux, le réseau TikTok grâce à la fonction append();
plateformes_sociaux.append("TikTok")
print(plateformes_sociaux)

#Retirons un élément de notre liste grâce à la fonction remove();
plateformes_sociaux.remove("whatsapp")
print(plateformes_sociaux)

#Affichons la longueur de la liste avec la fonction len();
print(len(plateformes_sociaux))

print(plateformes_sociaux.sort())

plateformes_sociaux.extend("Naruto")
print(plateformes_sociaux)
