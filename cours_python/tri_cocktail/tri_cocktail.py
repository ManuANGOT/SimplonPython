
def tri_cocktail(tableau):
    """_fonction tri_cocktail 

    Args:
        tableau (tableau): une collection d'éléments de tailles variées
        (chiffres, fichiers...)

    Returns:
       tableau_tri: la liste triée après chaque passage : une fois de gauche à droite, puis une fois de droite à gauche
    """

    # définition des balises de mon tableau
    n = len(tableau)
    start = 0
    end = n - 1
    echange = True

    while echange:
        # Itération de gauche à droite
        echange = False
        for i in range(start, end):
            if tableau[i] > tableau[i + 1]:
                tableau[i], tableau[i + 1] = tableau[i + 1], tableau[i]
                echange = True
        end -= 1
        print (tableau)


        # Itération de droite à gauche
        echange = False
        for i in range(end - 1, start - 1, -1):
            if tableau[i] > tableau[i + 1]:
                tableau[i], tableau[i + 1] = tableau[i + 1], tableau[i]
                echange = True
        start += 1
        print (tableau)
    return tableau
  
# Création d'un tableau d'échantillons pour tester le code et afficher le tri
tableau = [40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 0]


tableau_tri = tri_cocktail(tableau)
print(tableau_tri)

# Ce code est terminé et fonctionne !!!
# Pour démarrer le test, entrer le nom du fichier dans la console