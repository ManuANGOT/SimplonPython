from __future__ import annotations
from math import sqrt

def get_dist(a:tuple, b:tuple) -> float:
    return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

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
    
    def create_path(self, list_points_of_interest):
        if len(list_points_of_interest) != 0:
            for point in list_points_of_interest:
                self.add_child(Arbre(point))
            for child in self.children:
                child.create_path([elt for elt in list_points_of_interest if elt != child.value])
    

    def get_path_list(self) -> list:
        if self.is_leaf():
            return [[self.value]]
        
        path_list = []
        for child in self.children:
            child_paths = child.get_path_list()
            for path in child_paths:
                path_list.append([self.value] + path)
        return path_list
    
    def get_shortest_path(self, coordonnees:list[tuple]):
        if self.is_leaf():
            return {
                "len" : 0,
                "path" : [self.value]
            }
        
        path_list = [child.get_shortest_path(coordonnees) for child in self.children]
        for path in path_list:
            # on calcul la distance
            path["len"] += get_dist(coordonnees[path["path"][0]], coordonnees[self.value])
            # on ajoute notre point actuel au chemin
            path["path"].insert(0, self.value)
        # on renvoie le meilleur chemin 
        return min(path_list, key=lambda dico:dico["len"])
        
