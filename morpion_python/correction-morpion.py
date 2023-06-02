"""Besoin de fonctions pour :
- créer une grille
- afficher la grille
- vérifier si le coup est valide
- jouer un coup
- changer de joueur
- vérifier si grille est gagnante
- vérifier si grille est pleine""" 

def afficher_grille(grille:dict) -> None:
    """Fonction qui affiche la grille

    Args:
        grille (dict): Un dictionnaire qui représente une grille
    """
    print(" \t|\t0\t|\t1\t|\t2\t|")
    print("---------------------------------------------------------")
    for cle in grille:
        print(f"{cle}\t|\t{grille[cle][0]}\t|\t{grille[cle][1]}\t|\t{grille[cle][2]}\t|")
        print("---------------------------------------------------------")

def est_coup_valide(grille:dict, coup:str) -> bool:
    """Fonction qui vérifie si un coup est valide

    Args:
        grille (dict): La grille à vérifier
        coup (str): Le coup à vérifier (de la forme "A1")

    Returns:
        bool: True si le coup est dans la grille et la case est vide, False sinon
    """
    if len(coup) == 2 and coup[0].upper() in ["A", "B", "C"] and coup[1] in ["0", "1", "2"]:
        # Le coup est dans la grille
        if grille[coup[0]][int(coup[1])] == " ":
            # La case est libre
            return True
    return False
        
def jouer_coup(grille:dict, coup:str, joueur:str) -> None:
    """Fonction qui permet de jouer un coup

    Args:
        grille (dict): Un plateau de jeu
        coup (str): Un coup valide de la forme "A1" (/!\ Pas de vérification sur le coup)
        joueur (str): "O" ou "X"
    """
    grille[coup[0]][int(coup[1])] = joueur
    
def est_pleine(grille:dict) -> bool:
    """Fonction qui vérifie si la grille est pleine

    Args:
        grille (dict): Un plateau de jeu

    Returns:
        bool: True si la grille est plein, False sinon
    """
    for cle in grille:
        for elt in grille[cle]:
            if elt == " ":
                return False
    return True

def est_gagnante(grille:dict) -> bool:
    """Fonction qui vérifie si la grille est gagnante

    Args:
        grille (dict): Un plateau de jeu

    Returns:
        bool: True si la grille est gagnante, False sinon
    """
    # On vérifie les lignes
    for cle in grille:
        if grille[cle][0] != " " and grille[cle][0] == grille[cle][1] == grille[cle][2]:
            return True
    # On vérifie les colonnes
    for i in range(3):
        if grille["A"][i] != " " and grille["A"][i] == grille["B"][i] == grille["C"][i]:
            return True
    # On vérifie les diagonales
    if grille["A"][0] != " " and grille["A"][0] == grille["B"][1] == grille["C"][2]:
        return True
    if grille["A"][2] != " " and grille["A"][2] == grille["B"][1] == grille["C"][0]:
        return True
    
    return False
    
        

grille = {
    "A" : [" ", " ", " "],
    "B" : [" ", " ", " "],
    "C" : [" ", " ", " "],
}

fin = False
joueur = "X"

while not fin:
    afficher_grille(grille)
    coup = input(f"Entrez votre coup (De la forme A1) (Joueur {joueur})")
    
    # On vérifie si le coup est valide, et on redemande au joueur son coup s'il ne l'est pas
    while not est_coup_valide(grille, coup):
        coup = input(f"Entrez Un coup valide cette fois ! (Joueur {joueur})")
    
    # On sait que une fois arrivé ici que le coup est valide
    jouer_coup(grille, coup, joueur)
    
    if est_gagnante(grille):
        afficher_grille(grille)
        print(f"Victoire du joueur {joueur}")
        fin = True
    elif est_pleine(grille):
        afficher_grille(grille)
        print("Egalité !")
        fin = True
    else:
        joueur = "O" if joueur == "X" else "X"
   
    
    
    

