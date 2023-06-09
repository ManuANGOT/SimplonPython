import random

class AlgoGenetic:
    def __init__(self) -> None:
        self.population = []
        self.tableau = [0, 1, 3, 6, 8, 2, 4, 5, 7]

    def generer_chemin_aleatoire(self):
        chemin = list(self.tableau)
        random.shuffle(chemin)
        return chemin
    print(chemin)
    
    # Je crée aléatoirement une popultation de base
    def generer_population_base(self, taille_population):
        population = []
        for _ in range(taille_population):
            chemin = self.generer_chemin_aleatoire()
            population.append(chemin)
        self.population = population
    print("Population de base, est de : " + population)


    # fonction pour évaluer la population
    def evaluer_population(self, population):
        evaluations = []
        for chemin in population:
            # Fonction d'évaluation pour chaque chemin
            evaluation = self.fonction_evaluation(chemin)
            evaluations.append(evaluation)
        return evaluations
        print(evaluations)
    

    # Fonction pour évaluer la validité des chemins    
    def fonction_evaluation(self, chemin):
    # Ajoutez ici votre fonction d'évaluation pour chaque chemin
    # Retourne une valeur qui représente la qualité du chemin
        pass

    def selectionner_parents(self, population, evaluations, proportion_parents):
        nb_parents = int(len(population) * proportion_parents)
        individus_tries = sorted(zip(population, evaluations), key=lambda x: x[1], reverse=True)
        parents = [individu for individu, _ in individus_tries[:nb_parents]]
        return parents

    def croiser_parents(self, parents):
        descendants = []
        nb_descendants = len(self.population) - len(parents)
        for _ in range(nb_descendants):
            parent1, parent2 = random.sample(parents, 2)
            point_crossover = random.randint(1, len(self.tableau) - 2)
            descendant = parent1[:point_crossover] + parent2[point_crossover:]
            descendants.append(descendant)
        return descendants

    def muter_descendants(self, descendants, taux_mutation):
        for i in range(len(descendants)):
            if random.random() < taux_mutation:
                index1, index2 = random.sample(range(len(self.tableau)), 2)
                descendants[i][index1], descendants[i][index2] = descendants[i][index2], descendants[i][index1]
        return descendants

    def fusionner_population(self, population, descendants):
        nouvelle_population = population + descendants
        nouvelle_population.sort(key=lambda x: self.fonction_evaluation(x), reverse=True)
        self.population = nouvelle_population

   
