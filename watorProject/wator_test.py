import random, time


"""Création de la grille torique qui simulera la mer (base 8 x 15)"""
grid = [[' ' for _ in range(15)] for _ in range(8)]


"""Je génére une grille avec des poissons et des requins.
 Je pars du principe que environ un tiers de la grille doit être remplie de poissons,
   et qu'il doit y avoir trois fois moins de requins que de poissons """
fish_count = (8 * 15) // 3
shark_count = fish_count // 3

# Placement des poissons
while fish_count > 0:
    x = random.randint(0, 14)
    y = random.randint(0, 7)
    if grid[y][x] == ' ':
        grid[y][x] = 'F'
        fish_count -= 2

# Placement des requins
while shark_count > 0:
    x = random.randint(0, 14)
    y = random.randint(0, 7)
    if grid[y][x] == ' ':
        grid[y][x] = 'S'
        shark_count -= 1

# Déplacements des poissons
def move_fish(x, y):
    # Déplacements possibles pour le poisson, par mélange aléatoire, si espaces libres
    possible_moves = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]

    # Choix d'un déplacement aléatoire parmi les possibilités
    random.shuffle(possible_moves)
    
    for new_x, new_y in possible_moves:
        # Vérification des limites de la grille
        new_x = new_x % 15
        new_y = new_y % 8
        
        # Vérification si la nouvelle case est vide
        if grid[new_y][new_x] == ' ':
        # Déplacement du poisson
            grid[new_y][new_x] = 'F'
            grid[y][x] = ' '
            return
    # Le poisson ne peut pas se déplacer, il reste sur place

# génération énergie du poisson
fish_energy = [[5 for _ in range(15)] for _ in range(8)]

# génération énergie du requin
shark_energy = [[4 for _ in range(15)] for _ in range(8)]

# Déplacements du requin
def move_shark(x, y):
    # Déplacements possibles pour le requin
    possible_moves = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    random.shuffle(possible_moves)

    for new_x, new_y in possible_moves:
        # Vérification des limites de la grille torique
        new_x = new_x % 15
        new_y = new_y % 8

        # Vérification si la nouvelle case contient un poisson
        if grid[new_y][new_x] == 'F':
            # Le requin mange le poisson
            grid[new_y][new_x] = 'S'
            grid[y][x] = ' '
            return
           
       
        # Si aucun poisson n'est trouvé, le requin se déplace sans manger
    if grid[y][x] == 'S':
        grid[y][x] = ' '
        grid[new_y][new_x] = 'S'
        # le requin perd un point d'énergie
        shark_energy[new_y][new_x] -= 1

        # Vérification de l'énergie du requin
        if shark_energy[new_y][new_x] == 0:
            # Le requin meurt s'il n'a plus d'énergie
            grid[new_y][new_x] = ' '
        return


def simulate_turn():
    for y in range(8):
        for x in range(15):
            if grid[y][x] == 'F':
                move_fish(x, y)
            elif grid[y][x] == 'S':
                move_shark(x, y)

    # Logique de reproduction des poissons et des requins
    for y in range(8):
        for x in range(15):
            if grid[y][x] == 'F':
                reproduce_fish(x, y)
            elif grid[y][x] == 'S':
                reproduce_shark(x, y)

                # Vérification de l'énergie des requins
            if grid[y][x] == 'S':
                if shark_energy[y][x] >= 10:
                    shark_energy[y][x] = 10
                elif shark_energy[y][x] <= 0:
                    # Le requin meurt s'il n'a plus d'énergie
                    grid[y][x] = ' '

def reproduce_fish(x, y):
    # Comptage des poissons voisins
    fish_neighbors = 0

    # Vérification des cases voisines pour les poissons
    for i in range(-1, 2):
        for j in range(-1, 2):
            if grid[(y + i) % 8][(x + j) % 15] == 'F':
                fish_neighbors += 1

    # Reproduction du poisson après 1 déplacement
    if fish_neighbors >= 4:
        empty_cells = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if grid[(y + i) % 8][(x + j) % 15] == ' ':
                    empty_cells.append(((x + j) % 15, (y + i) % 8))

def reproduce_shark(x, y):
    # Comptage des poissons voisins
    fish_neighbors = 0

    # Vérification des cases voisines pour les poissons
    for i in range(-1, 2):
        for j in range(-1, 2):
            if grid[(y + i) % 8][(x + j) % 15] == 'F':
                fish_neighbors += 1

    # Reproduction du poisson après 4 déplacements
    if fish_neighbors >= 4:
        empty_cells = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if grid[(y + i) % 8][(x + j) % 15] == ' ':
                    empty_cells.append(((x + j) % 15, (y + i) % 8))                

# Animation avec un exemple de limite de 100 tours
num_turns = 0
while num_turns < 100:  
    print(f"Tour {num_turns}")
    # Affichage de la grille
    for row in grid:
        print(' '.join(row))
    print()

    simulate_turn()
    num_turns += 1

    # Afin de voir correctement l'animation, je met une pause d'une demi-seconde entre chaque tour
    time.sleep(1)

