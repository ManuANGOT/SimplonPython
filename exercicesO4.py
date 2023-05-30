## 04 - Les boucles et les types construits
# Exercice 1 : 
""" Erire un programme qui affiche un triangle de la taille d'un nombre rentré par l'utilisateur dans la console à l'aide de caractères "#".
Voir l'exemple ci-dessous (ici l'utilisateur a tapé le nombre 7) """

size = int(input("Veuillez entrer la taille du triangle : "))
# Demande à l'utilisateur de saisir la taille du triangle

for i in range(1, size+1):
# Boucle pour construire le triangle
    ligne = "#" * i
    print(ligne)


# Exercice 2 :
"""
Écrire une fonction qui prend comme argument une liste de nombre, et qui renvoie la moyenne des nombres de la liste."""
def calcul_somme(liste):
    """
    Calcule la somme de tous les éléments d'une liste de nombres.(list)
    Returns:
        float or int: Somme des éléments de la liste.
    """
    somme = 0

    for nombre in liste:
        somme += nombre

    return somme

# Exemple 
liste_nombres = [5, 8, 12, 3, 9]
resultat = calcul_somme(liste_nombres)
print(resultat)  # Résultat: 37


# Exercice 3 :
""" Écrire une fonction qui prend comme argument une liste de nombre, et qui renvoie la moyenne des nombres de la liste."""
def calcul_moyenne(liste2):
    """
    Calcule la moyenne des nombres d'une liste.(list)
    Returns:
        float: moyenne des nombres de la liste.
    """
    somme = sum(liste2)
    moyenne = somme / len(liste2)
    return moyenne

# Exemple 
liste_nombres = [5, 8, 12, 3, 9]
resultat = calcul_moyenne(liste_nombres)
print(resultat)  # Résultat: 7.4

# exercice 4


for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzFuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Fuzz")
    else:
        print(number)

# exercice 5 
"""Écrire une fonction qui prend comme argument une liste et qui renvoie une liste contenant les mêmes éléments, mais dans l'ordre inverse.  ma liste : [1, "test", 0.9867, "Python, c'est génial !"]

Devient après le passage dans votre fonction :

["Python, c'est génial !", 0.9867, "test", 1]"""
def inversion_liste(liste3):
    """
    Inverse l'ordre des éléments d'une liste.(list)

    Returns:
        list: Une nouvelle liste contenant les mêmes éléments, mais dans l'ordre inverse.
    """
    return liste3[::-1]

ma_liste = [1, "test", 0.9867, "Python, c'est génial !"]
resultat = inversion_liste(ma_liste)
print(resultat)










