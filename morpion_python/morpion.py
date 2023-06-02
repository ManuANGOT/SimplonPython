# Création du "plateau de jeu" dans la console
def afficher_plateau(plateau):
    """ fonction qui permet d'afficher la grille
    
    Args : 
    afficher-plateau() : permet d'afficher
    plateau : la grille """
    for ligne in plateau:
        print("|".join(ligne))
        print("-----")


# Pour vérifier la victoire, j'utilise 3 symboles identiques en ligne, en colonne ou en diagonale
def verifier_victoire(plateau, symbole):
    # Vérifier les lignes
    for ligne in plateau:
        if ligne.count(symbole) == 3:
            return True

    # Vérifier les colonnes
    for colonne in range(3):
        if [plateau[i][colonne] for i in range(3)].count(symbole) == 3:
            return True

    # Vérifier les diagonales
    if [plateau[i][i] for i in range(3)].count(symbole) == 3:
        return True
    if [plateau[i][2-i] for i in range(3)].count(symbole) == 3:
        return True

    return False


# Fonction pour démarrer le jeu
def jouer_morpion():
    plateau, joueur = redemarrer_jeu()

    while True:
        # Au démarrage, j'affiche le plateau vide
        afficher_plateau(plateau)

        # Demander au joueur de saisir les coordonnées
        ligne = int(input("Joueur {} - Choisissez la ligne (0, 1, 2) : ".format(joueur)))
        colonne = int(input("Joueur {} - Choisissez la colonne (0, 1, 2) : ".format(joueur)))

        # Vérifier si la case est libre
        if plateau[ligne][colonne] != " ":
            print("Case occupée. Veuillez choisir une autre case.")
            continue

        # Placer le symbole du joueur sur le plateau
        plateau[ligne][colonne] = "X" if joueur == 1 else "O"

        # Vérifier si le joueur a gagné
        if verifier_victoire(plateau, "X"):
            afficher_plateau(plateau)
            print("Joueur 1 a gagné !")
            break
        elif verifier_victoire(plateau, "O"):
            afficher_plateau(plateau)
            print("Joueur 2 a gagné !")
            break

        # Vérifier s'il y a un match nul
        if verifier_match_nul(plateau):
            afficher_plateau(plateau)
            print("Match nul !")
            break

        # Changer de joueur
        joueur = 2 if joueur == 1 else 1

    # Rejouer
    choix = input("Voulez-vous rejouer ? (Oui/Non) : ")
    if choix.lower() == "oui":
        # rappel de la fonction "jouer_morpion()" pour relancer le jeu
        jouer_morpion()


# fonction pour vérifier si match nul
def verifier_match_nul(plateau):
    for ligne in plateau:
        if " " in ligne:
            return False
    return True


# fonction pour redémarrer le jeu
def redemarrer_jeu():
    plateau = [[" " for _ in range(3)] for _ in range(3)]
    joueur = 1
    return plateau, joueur


# Lancer le jeu, appel de la fonction jouer_morpion() pour lancer le jeu/programme
jouer_morpion()