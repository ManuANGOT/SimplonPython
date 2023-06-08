# Distanciel
from __future__ import annotations
import math
import random
from itertools import permutations

# Fonction pour calculer la distance entre deux points
def distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

# Point de départ
base_depart = (0, 0)

# Génération de 3 étapes aléatoires
nombre_etapes = 3
all_points = [(2, 5), (6, 2), (4, 4), (7, 8), (1, 3)]  # Liste de points disponibles
random_etape = random.sample(all_points, nombre_etapes)

# Création de l'arborescence
Road = {
    base_depart: random_etape
}
for step in random_etape:
    Road[step] = random.sample(all_points, nombre_etapes)

# Calcul des distances entre les points
points = [base_depart] + random_etape
num_points = len(points)
distances = [[0] * num_points for _ in range(num_points)]

for i in range(num_points):
    for j in range(num_points):
        if i != j:
            distances[i][j] = distance(points[i], points[j])

# Détermination du chemin optimal pour parcourir tous les points
min_distance = float('inf')
chemin_optimal = None

for chemin in permutations(range(1, num_points)):
    chemin = [0] + list(chemin)
    path_distance = sum(distances[chemin[i]][chemin[i+1]] for i in range(num_points-1))
    if path_distance < min_distance:
        min_distance = path_distance
        chemin_optimal = chemin

chemin_optimal = [points[i] for i in chemin_optimal]

print("Arborescence :")
for point, children in Road.items():
    print(f"{point} -> {children}")

print("\nDistances entre les points :")
for i in range(num_points):
    for j in range(i+1, num_points):
        print(f"Distance entre {points[i]} et {points[j]} : {distances[i][j]}")

print("\nLe chemin optimal à utiliser est :")
print(chemin_optimal)
print("La distance totale sera de : ", min_distance," Kilomètres")