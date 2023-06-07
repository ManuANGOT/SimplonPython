from __future__ import annotations

class Arbre:
    def __init__(self, value):
        self.value = value
        self.children = []

def _str_(self) -> None :
    self.value = Value
    self.children = []

def add_child(self, noeud:Arbre) -> None :
    self.children.append(noeud)

def is_leaf(self) -> bool :
    return True if len(self.children) == 0 else False

def obtenir_profondeur(self) -> int :
    if self.is_leaf():
        return 1
    
    liste_profondeur = [child.obtenir_profondeur() for child in self.children]
    
   # Autre façon de faire :
    # liste_profondeur = []
    # for child in self.children :
     #   liste_profondeur.append(child.profondeur())

def dfs(self) -> list :
    if self.is_leaf():
        return [self.value]
    Liste_resultat = []
    for enfant in self.children:
        Liste_resultat += enfant.dfs()
        Liste_resultat.append(self.value)
        return Liste_resultat


    
