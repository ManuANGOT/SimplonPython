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