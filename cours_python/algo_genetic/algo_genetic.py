from __future__ import annotations
import math
import random



class AlgoGenetic:
    def __init__(self) -> None:
        self.population=[]

    # Tableau de 9 caractères
        self.tableau = [0, 1, 3, 6, 8, 2, 4, 5, 7]

    # Fonction pour générer un chemin aléatoire
    def generer_chemin_aleatoire(self):
        chemin = list(self.tableau)
        random.shuffle(chemin)
        return chemin

    # Génération d'une population de base
    def generer_population_base(self, taille_population):
        population = []
        for _ in range(taille_population):
            chemin = self.generer_chemin_aleatoire()
            population.append(chemin)
        self.population = population
        print(population)

    # Évaluation de la population
    def evaluer_population(self):
        evaluations = []
        for chemin in self.population:
            # Fonction d'évaluation pour chaque chemin
            evaluation = self.fonction_evaluation(chemin)
            evaluations.append(evaluation)
        return evaluations

  