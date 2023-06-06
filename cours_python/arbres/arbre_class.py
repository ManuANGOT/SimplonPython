class Arbre:
    def __init__(self, value):
        self.value = value
        self.children = []

def iterative_ppi(root):
    if not root:
        return

    stack = [root]

    while stack:
        node = stack.pop()
        print(node.value)

        # Ajouter les enfants du nœud courant dans la pile dans l'ordre inverse
        for child in reversed(node.children):
            stack.append(child)

# Création d'une arborescence avec 22 branches
root = Arbre(1)
for i in range(2, 23):
    child = Arbre(i)
    root.children.append(child)

# Appel de la fonction de parcours en profondeur itératif
iterative_ppi(root)
        