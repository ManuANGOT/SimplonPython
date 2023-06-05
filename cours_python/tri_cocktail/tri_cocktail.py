def tri_cocktail(table):
    """_fonction tri_cocktail 
    Args:
        tableau (table): une collection d'éléments de tailles variées
        (chiffres, fichiers...)

    Returns:
       tableau_tri: la liste triée après chaque passage : une fois de gauche à droite, puis une fois de droite à gauche
    """
    # définition des balises de mon tableau
    complexite = (0, 0, 0)
    x = len(table)
    start = 0
    end = x - 1
    exchange = True

    while exchange:
        complexite = (complexite[0] + 1, complexite[1], complexite[2])
        # Itération de gauche à droite
        exchange = False
        for i in range(start, end):
            if table[i] > table[i + 1]:
                table[i], table[i + 1] = table[i + 1], table[i]
                exchange = True
                complexite = (complexite[0], complexite[1] + 1, complexite[2])
        end -= 1
        # Itération de droite à gauche
        exchange = False
        for i in range(end - 1, start - 1, -1):
            if table[i] > table[i + 1]:
                table[i], table[i + 1] = table[i + 1], table[i]
                exchange = True
            complexite = (complexite[0], complexite[1], complexite[2] + 1)
        start += 1
    print(complexite)
    return table
  
# Création d'un tableau d'échantillons pour tester le code et afficher le tri
import random
table = [i for i in range(10)]

tableau_tri = tri_cocktail(table)
print(tableau_tri)

# Pour démarrer le test, entrer le nom du fichier dans la console, ou cliquer sur "play"