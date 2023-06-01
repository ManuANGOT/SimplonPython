# Exercice 1 :

user_input = int(input("Please enter a number : "))

if user_input % 2 == 0:
    print("Your number is even")
else:
    print("Your number is odd")
    
# Exercice 2

nb1 = int(input("Entrez un nombre : "))
nb2 = int(input("Entrez un deuxième nombre : "))
nb3 = int(input("Entrez un troisième nombre : "))

if nb1 >= nb2 and nb1 >= nb3:
    print(nb1)
elif nb2 >= nb1 and nb2 >= nb3:
    print(nb2)
else:
    print(nb3)