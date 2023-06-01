# Exercice 1

input_user = int(input("Entrez un nombre"))

for i in range(1, input_user + 1):
    print("#" * i)
    
# Exercice 2

def calculer_somme(liste:list) -> float:
    """Fonction qui renvoie la somme des elements de la liste

    Args:
        liste (list): Une liste de nombre

    Returns:
        float: La somme des nombres de la liste
    """
    resultat = 0.
    for nb in liste:
        resultat += nb
    return resultat

# Exercice 3

def calculer_moyenne(liste:list) -> float:
    """Fonction qui renvoie la moyenne des éléments de la liste

    Args:
        liste (list): Une liste de nombres

    Returns:
        float: La moyenne des éléments de la liste
    """
    return calculer_somme(liste) / len(liste)

# Exercice 4

# V1
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("Fizz Fuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Fuzz")
    else:
        print(i)

# V2     
for i in range(1, 101):
    print(i, end=" : ")
    if i % 3 == 0:
        print("Fizz", end=" ")
    if i % 5 == 0:
        print("Fuzz", end="")
    print()
    
# Exercice 5

liste = [1, "test", 0.9867, "Python, c'est génial !"]

def renverser_liste(liste:list) -> list:
    """Fonction qui inverse l'ordre de la liste

    Args:
        liste (list): La liste à renverser

    Returns:
        list: La liste renversée
    """
    liste2 = liste.copy()
    for i in range(0, len(liste)//2):
        liste2[i], liste2[-1 - i] = liste2[-1 - i], liste2[i]
    return liste2

print(renverser_liste(liste))
print(liste)

# Exercice 6

dico = {
    "Python" : "Le meilleur langage de programmation du monde entier d'après Antoine",
    "Pi" : 3.14,
    "ma_liste" : ["Bonjour", "ceci", "est", 1, "liste"]
}

dico["mx5"] = "Voiture sympa"
dico["mx5"] = "Voiture très sympa"

input_user = input("Cherchez vous un mot ?")
if dico.get(input_user) != None:
    print(dico.get(input_user))
else:
    print("Nous ne connaissons pas ce mot")
    
# Exercice 7

from random import randint

liste = []
for _ in range(1000):
    liste.append(randint(1, 100))
print(liste)

liste = [randint(1, 100) for _ in range(1000)]

# Exercice 8

# Methode classique
liste_inf_10 = []
for elt in liste:
    if elt < 10:
        liste_inf_10.append(elt)
print(liste_inf_10)

# Methode par compréhension
liste_inf_10 = [elt for elt in liste if elt < 10]
print(liste_inf_10)
