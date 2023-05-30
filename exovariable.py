## 01 DECOUVERTE
# Variables
nomDeMaVariable = "la valeur de ma variable"
nombreUn = 55
nombreDeux = 5

resultat = nombreUn + nombreDeux
print(resultat)
print(nomDeMaVariable)


# Booléen
var1 = True
var2 = False

print("var1 OU var2 = " + str(var1 or var2))
print("var1 ET var2 = " + str(var1 and var2))
print("NON var1 = " + str(not var1))

# Chaîne de caractères
phrase1 = "Bonjour, j'aime beaucoup le Python !"
print(phrase1)

# Concaténation
mot1 = "Bonjour "
mot2 = "Python !"

phrase2 = mot1 + mot2 
print(phrase2)

# décomposition en lettre
print (phrase1[0])
print (phrase1[1])
print (phrase1[2])
print (phrase1[3])
print (phrase1[4])
print (phrase1[5])
print (phrase1[6])
print (phrase1[7])

# Exercice 1 : miles en kilomètres
# Saisie données utilisateur 
miles = float(input("Veuillez entrer une distance en miles : "))
# Conversion (1 mile = 1.60934 kilomètres)
kilometres = miles * 1.60934
# Affichage du résultat
print(f"{miles} miles est équivalent à {kilometres} kilomètres.")


# Exercice 2 : variable
var1 = "Je dois être en seconde position"
var2 = "Je dois être en première position"

print(var1 + " | " + var2)
# Utilisation variable temporaire
temp = var1
var1 = var2
var2 = temp
print(var1 + " | " + var2)

## 02 CONDITIONNELS
# Exo 1 Pair ou impair
userNombre = int(input("Veuillez entrer un nombre : "))

if userNombre % 2 == 0:
    print("Le nombre est pair.")
else:
    print("Le nombre est impair.")

# Exo 2 
# Demande à l'utilisateur d'entrer trois nombres
nombre1 = float(input("Veuillez entrer le premier nombre : "))
nombre2 = float(input("Veuillez entrer le deuxième nombre : "))
nombre3 = float(input("Veuillez entrer le troisième nombre : "))

# Comparaison des nombres pour trouver le plus grand
plus_grand = nombre1 

if nombre2 > plus_grand:
    plus_grand = nombre2

if nombre3 > plus_grand:
    plus_grand = nombre3

# Affichage du plus grand nombre
print("Le plus grand nombre est :", plus_grand)

## 03 LES FONCTIONS
# Exo 1
""" Transformer en fonction, le code suivant :

nb_utilisateur = int(input("Entrez un nombre entier : "))
if nb_utilisateur % 2 == 0:
    print("le nombre est pair")
else:
    print("Le nombre est impair")"""

# Création de la fonction qui vérifie si le nombre est pair ou impair
def verifier_pair_impair(nombre):
    if nombre % 2 == 0:
        print("Le nombre est pair")
    else:
        print("Le nombre est impair")

# Demande à l'utilisateur d'entrer un nombre
userNumber = int(input("Entrez un nombre entier : "))

# Appel de la fonction pour vérifier si le nombre est pair ou impair
verifier_pair_impair(userNumber)

#Exo 2 "Est pair"
newnb = float(input("Veuillez entrer un nombre entier : "))
def est_pair(newnb):
    if newnb % 2 == 0:
        return True
    else:
        return False

# Exemples d'utilisation de la fonction est_pair()
print(est_pair(2))  # Résultat: True
print(est_pair(5))  # Résultat: False

#Exo 3 "Plus petit" Écrire une fonction qui prend pour argument 3 nombres, et renvoie le plus petit des trois
def trouver_plus_petit(a, b, c):
    plus_petit = a  
    # On postule que le premier nombre est le plus petit

    if b < plus_petit:
        plus_petit = b

    if c < plus_petit:
        plus_petit = c

    return plus_petit

# Exemple d'utilisation de la fonction trouver_plus_petit()
print(trouver_plus_petit(500, 1000, 15)) 


# Exo 4 Écrire la docstring de la fonction suivante, et améliorer la qualité du code :
"""def x(a, b):
    if a < 0:
        a = -a
    if b < 0: 
        b = -b
    return a*b"""
def calcul_produit(a, b):
    """
    Calcule le produit de deux nombres a et b.

        a (int or float): Le premier nombre.
        b (int or float): Le deuxième nombre.
    """
    if a < 0:
        a = -a
    if b < 0:
        b = -b
# return : retourne le produit
    return a * b


# Exo 5 Écrire une fonction qui prend en paramètres 3 nombres, et renvoie la moyenne des trois.
def calcul_moyenne(a, b, c):
    """
    Calcule la moyenne de trois nombres.
    Returns:
        float: La moyenne des trois nombres.
    """
    return (a + b + c) / 3

# Exemple d'utilisation de la fonction calcul_moyenne()
resultatMoyenne = calcul_moyenne(4.5, 2.7, 6.8)
print(resultatMoyenne)



