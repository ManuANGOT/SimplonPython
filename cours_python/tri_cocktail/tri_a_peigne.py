import math
def tri_a_peigne(tableau):
    """_fonction tri_a_peigne 

    Args:
        tableau (tableau): une collection d'éléments de tailles variées
        (chiffres, fichiers...)

    Returns:
       
    """

    # définition des balises de mon tableau
    intervalle = len(tableau)
    end = intervalle - 1
    echange = True

    while (echange == True) or (intervalle>1):      
        echange = False
        intervalle = math.floor(intervalle / 1.3)
        if intervalle<1 : intervalle=1
        for i in range(0, len(tableau) - intervalle):
            if tableau[i] > tableau[i + intervalle]:
                tableau[i], tableau[i + 1] = tableau[i + 1], tableau[i]
                echange = True
                tableau[i], tableau[i + intervalle] = \
                tableau[i + intervalle],tableau[i]
            
            print(tableau)
           
    return tableau
  
# Création d'un tableau d'échantillons pour tester le code et afficher le tri
tableau = [40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 0]

tableau_tri = tri_a_peigne(tableau)
print(tableau_tri)

# Ce code n'est pas terminé !!!
