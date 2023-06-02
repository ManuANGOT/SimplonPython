# Exercice 1 :

def est_pair(nb:int) -> None:
    """Fonction qui affiche dans le terminal si le nombre est pair

    Args:
        nb (int): Le nombre à tester
    """
    if nb % 2 == 0:
        print("le nombre est pair")
    else:
        print("Le nombre est impair")

nb_utilisateur = int(input("Entrez un nombre entier : "))
est_pair(nb_utilisateur)


# Exercice 2 :

def est_pair(nb:int) -> bool:
    """Fonction qui vérifie si un nombre est pair

    Args:
        nb (int): Le nombre à tester

    Returns:
        bool: True si le nombre est pair, False sinon
    """
    if nb % 2 == 0:
        return True
    else:
        return False
    
# exercice 3

def renvoyer_minimum(nb1:int, nb2:int, nb3:int) -> int:
    """Fonction qui renvoie le plus petit de ses paramètres

    Args:
        nb1 (int): Un premier nombre à tester
        nb2 (int): Un deuxième nombre à tester
        nb3 (int): Un troisième nombre à tester

    Returns:
        int: Le plus petit des trois paramètres
    """
    if nb1 <= nb2 and nb1 <= nb3:
        return nb1
    elif nb2 <= nb1 and nb2 <= nb3:
        return nb2
    else:
        return nb3

# exercice 4 :

def produit_des_valeurs_absolues(nombre1:int, nombre2:int) -> int:
    """Fonction qui renvoie le produit des valeurs absolues de ses arguments

    Args:
        nombre1 (int): Un nombre
        nombre2 (int): Un deuxième nombre

    Returns:
        int: Le produit des valeurs absolues de nombre1 et nombre2
    """
    if nombre1 < 0:
        nombre1 = -nombre1
    if nombre2 < 0:
        nombre2 = -nombre2
    return nombre1 * nombre2

# Exercice 5

def calculer_moyenne(nb1:float, nb2:float, nb3:float) -> float:
    """Fonction qui calcule la moyenne des 3 arguments

    Args:
        nb1 (float): Un premier nombre
        nb2 (float): Un deucième nombre
        nb3 (float): Un troisième nombre

    Returns:
        float: La moyenne des trois nombres
    """
    return (nb1 + nb2 + nb3) / 3