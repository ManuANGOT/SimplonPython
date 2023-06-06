class Arbre:
    def __init__(self, value):
        self.value = value
        self.children = []

# Le parcours en profondeur par itération (DFS pour Depth-First Search)
def iterative_dfs(root):
    if not root:
        return

    stack = [root]

    while stack:
        node = stack.pop()
        print(node.value)

        # Ajouter les enfants du nœud courant dans la pile
        for child in reversed(node.children):
            stack.append(child)

def create_branch():
    value = int(input("Valeur du nœud racine : "))
    root = Arbre(value)
    stack = [root]

    while stack:
        node = stack.pop()
        child_count = int(input(f"Nombre d'enfants pour le nœud {node.value} : "))

        for i in range(child_count):
            child_value = int(input(f"Valeur de l'enfant {i+1} : "))
            child = Arbre(child_value)
            node.children.append(child)
            stack.append(child)

    return root

# Création de l'arborescence selon la demande de l'utilisateur
root = create_branch()

# Appel de la fonction de parcours en profondeur itératif
iterative_dfs(root)