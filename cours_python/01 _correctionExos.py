# Exercice 1 :
input_user = input("Please enter your distance (miles) : ")
try:
    input_user = int(input_user)
    print(f"Your distance is {input_user * 1.6} km")
except ValueError:
    print("I ask for a number ...")

# Exercice 2 :
var1 = "Je dois être en seconde position"
var2 = "Je dois être en première position"

## Ajouter le code de l'exercice ici ##

var1, var2 = var2, var1

print(var1 + " | " + var2) 
# après avoir complété l'exercice, doit afficher :
# Je dois être en première position | Je dois être en seconde position