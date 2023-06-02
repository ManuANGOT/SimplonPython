def tri_cocktail(tableau):
    
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

        # Itération de droite à gauche
        echange = False
        for i in range(end - 1, start - 1, -1):
            if tableau[i] > tableau[i + 1]:
                tableau[i], tableau[i + 1] = tableau[i + 1], tableau[i]
                echange = True
        start += 1

    return tableau
  
tableau = [40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 0]
tableau_tri = tri_cocktail(tableau)

print("tableau non trié :" + (tableau))
print("tableau après le tri-cocktail : " +(tableau_tri))