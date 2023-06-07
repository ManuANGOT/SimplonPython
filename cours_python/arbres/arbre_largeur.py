from __future__ import annotations

class Arbre:
    def __init__(self, value:any) -> None:
        self.value = value
        self.children = []
    
    def __str__(self) -> str:
        return str(self.value)
    
    def add_child(self, noeud:Arbre) -> None:
        self.children.append(noeud)
        
    def is_leaf(self) -> bool:
        return True if len(self.children) == 0 else False
    
    def get_depth(self) -> int:
        if self.is_leaf():
            return 1
        
        liste_profondeur = [child.get_depth() for child in self.children]
        return max(liste_profondeur) + 1
        # Autre façon de faire :
        # liste_profondeur = []
        # for child in self.children:
        #    liste_profondeur.append(child.profondeur())
        
    def dfs(self) -> list:
        if self.is_leaf():
            return [self.value]
        
        liste_resultat = []
        for enfant in self.children:
            liste_resultat += enfant.dfs()
        liste_resultat.append(self.value)
        return liste_resultat
    
    def bfs(self) -> list:
        queue = [self]
        result = []
        while len(queue) != 0:
            elt = queue.pop(0)
            result.append(elt.value)
            for child in elt.children:
                queue.append(child)
        return result