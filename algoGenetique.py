import random
from classes import *

def algorithme_genetique(graphe: Graphe, taille_population: int, iterations: int) -> None:
    """
    Utilise un algorithme génétique pour résoudre le problème de placement de données dans le graphe.

    Args:
        graphe (Graphe): Le graphe dans lequel placer les données.
        taille_population (int): Taille de la population pour l'algorithme génétique.
        iterations (int): Nombre d'itérations de l'algorithme génétique.
    """
    # Initialisation de la population
    population = [genere_solution_aleatoire(graphe) for _ in range(taille_population)]
    
    # Boucle d'itération de l'algorithme génétique
    for _ in range(iterations):
        
        # Évaluation de la fitness de chaque individu dans la population
        fitness_population = [evaluation_fitness(solution, graphe) for solution in population]
        
        # Sélection des meilleurs individus pour la reproduction (roulette)
        meilleurs_individus = selection_meilleur_ratio(population, fitness_population, taille_population // 2)
        
        # Croisement des individus sélectionnés pour former une nouvelle génération
        nouvelle_generation = croisement(meilleurs_individus, taille_population)
        
        # # Mutation de la nouvelle génération
        # nouvelle_generation = mutation(graphe, nouvelle_generation)
        
        # Remplacement de l'ancienne population par la nouvelle génération
        population = nouvelle_generation
    
    # Sélection de la meilleure solution parmi la population finale
    meilleure_solution = max(population, key=lambda solution: evaluation_fitness(solution, graphe))
    
    # Placer les données dans le graphe selon la meilleure solution trouvée
    placer_donnees(graphe, meilleure_solution)

def genere_solution_aleatoire(graphe: Graphe) -> list[int]:
    """
    Génère une solution aléatoire pour le problème de placement de données dans le graphe.

    Args:
        graphe (Graphe): Le graphe dans lequel placer les données.

    Returns:
        list[int]: Une solution aléatoire sous forme d'une liste d'identifiants de nœuds système.
    """
    return [random.choice([noeud.getID() for noeud in graphe.getNoeudsSysteme()]) for _ in range(len(graphe.getDonneesAPlacer()))]

def evaluation_fitness(solution: list[int], graphe: Graphe) -> int:
    """
    Évalue la fitness d'une solution pour le problème de placement de données dans le graphe.

    Args:
        solution (list[int]): Une solution sous forme d'une liste d'identifiants de nœuds système.
        graphe (Graphe): Le graphe dans lequel placer les données.

    Returns:
        int: La fitness de la solution.
    """
    # Créer une copie du graphe pour éviter de modifier l'original
    graphe_copie = graphe.copie()

    # Placer les données selon la solution donnée
    placer_donnees(graphe_copie, solution)

    # Calculer la fitness comme le nombre total d'utilisateurs couverts par la solution
    utilisateurs_couverts = set()
    for donnee in graphe_copie.getDonneesAPlacer():
        utilisateurs_couverts.update(graphe_copie.getUtilisateursInteressesParDonnee(donnee.getID()))
    return len(utilisateurs_couverts)

def selection_meilleur_ratio(population: list[list[int]], fitness_population: list[int], taille_selection: int) -> list[list[int]]:
    """
    Sélectionne l'individu avec le meilleur ratio entre le nombre d'utilisateurs intéressés et le poids.

    Args:
        population (list[list[int]]): La population d'individus.
        fitness_population (list[int]): La liste des fitness correspondant à chaque individu dans la population.
        taille_selection (int): La taille de la sélection.

    Returns:
        list[list[int]]: Les individus sélectionnés pour la reproduction.
    """
    # Associer chaque individu à son indice dans la population
    individus_indices = list(range(len(population)))

    # Trier les individus par rapport au ratio (fitness) décroissant
    individus_tries = sorted(individus_indices, key=lambda x: fitness_population[x], reverse=True)

    # Sélectionner les meilleurs individus en fonction du nombre spécifié
    meilleurs_individus_indices = individus_tries[:taille_selection]

    # Renvoyer les meilleurs individus de la population
    return [population[i] for i in meilleurs_individus_indices]


def croisement(individus: list[list[int]], taille_population: int) -> list[list[int]]:
    """
    Croise les individus sélectionnés pour former une nouvelle génération.

    Args:
        individus (list[list[int]]): Les individus sélectionnés pour la reproduction.
        taille_population (int): La taille de la population.

    Returns:
        list[list[int]]: La nouvelle génération formée par croisement.
    """
    nouvelle_generation = []

    # Croisement des individus sélectionnés pour former une nouvelle génération
    while len(nouvelle_generation) < taille_population:
        parent1, parent2 = random.sample(individus, 2)
        point_croisement = random.randint(1, len(parent1) - 1)
        enfant1 = parent1[:point_croisement] + parent2[point_croisement:]
        enfant2 = parent2[:point_croisement] + parent1[point_croisement:]
        nouvelle_generation.extend([enfant1, enfant2])

    return nouvelle_generation

# def mutation(graphe, population: list[list[int]]) -> list[list[int]]:
#     """
#     Mutate la population donnée en remplaçant aléatoirement certains individus.

#     Args:
#         population (list[list[int]]): La population d'individus.

#     Returns:
#         list[list[int]]: La population mutée.
#     """
#     taux_mutation = 0.1
#     nouvelle_population = []

#     # Mutation des individus de la population
#     for individu in population:
#         if random.random() < taux_mutation:
#             indice_mutation = random.randint(0, len(individu) - 1)
#             nouvel_individu = individu[:]
#             nouvel_individu[indice_mutation] = random.choice([noeud.getID() for noeud in graphe.getNoeudsSysteme()])  # Mutate en sélectionnant un autre nœud aléatoire
#             nouvelle_population.append(nouvel_individu)
#         else:
#             nouvelle_population.append(individu)

#     return nouvelle_population

def placer_donnees(graphe: Graphe, solution: list[int]) -> None:
    """
    Place les données dans le graphe selon la solution donnée.

    Args:
        graphe (Graphe): Le graphe dans lequel placer les données.
        solution (list[int]): Une solution sous forme d'une liste d'identifiants de nœuds système.
    """
    for donnee, noeud_id in zip(graphe.getDonneesAPlacer(), solution):
        noeud = graphe.getNoeudSystemeByID(noeud_id)
        # Vérifier si le poids des données dépasse la capacité mémoire du nœud
        poids_total_donnees = sum(donnee.getTaille() for donnee in noeud.donneesStockeesLocalement)
        if poids_total_donnees + donnee.getTaille() > noeud.capaciteMemoire:
            continue
        # Vérifier si la taille des données dépasse la taille disponible dans le nœud
        if donnee.getTaille() > graphe.getTailleDisponibleNoeud(noeud_id):
            continue
        graphe.addNoeudSystemeDonneeSL(noeud.getID(), donnee)
