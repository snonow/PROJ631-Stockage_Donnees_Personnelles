from classes import *
from PlacementDonnee import *
from Algo_génétique import *
 
# Création des Données
donnees = [Donnee(i, 30) for i in range(1000, 1009)]

# Création des Noeuds Systèmes
noeuds_systemes = [
    NoeudSysteme(3000, 40, [3001, 3002, 3003, 3004]),
    NoeudSysteme(3001, 50, [3000, 3002, 3003, 3004, 2000, 2001, 2002]),
    NoeudSysteme(3002, 40, [3000, 3001, 3003, 3004, 2003]),
    NoeudSysteme(3003, 50, [3000, 3001, 3002, 3004, 2004]),
    NoeudSysteme(3004, 40, [3000, 3001, 3002, 3003, 2005, 2006])
]

# Création des Utilisateurs
utilisateurs = [
    Utilisateur(2000, [1000], 3001),
    Utilisateur(2001, [1001, 1002], 3001),
    Utilisateur(2002, [1003, 1005], 3001),
    Utilisateur(2003, [1004], 3002),
    Utilisateur(2004, [1006], 3003),
    Utilisateur(2005, [1008], 3004),
    Utilisateur(2006, [1007], 3004)
]

# Création des arêtes
aretes = [
    Arete(noeuds_systemes[0], noeuds_systemes[1], 1),
    Arete(noeuds_systemes[0], noeuds_systemes[2], 3),
    Arete(noeuds_systemes[0], noeuds_systemes[3], 3),
    Arete(noeuds_systemes[0], noeuds_systemes[4], 3),
    Arete(noeuds_systemes[1], noeuds_systemes[2], 1),
    Arete(noeuds_systemes[1], noeuds_systemes[3],3),
    Arete(noeuds_systemes[1], noeuds_systemes[4], 3),
    Arete(noeuds_systemes[2], noeuds_systemes[3], 1),
    Arete(noeuds_systemes[2], noeuds_systemes[4], 3),
    Arete(noeuds_systemes[3], noeuds_systemes[4], 1),
    Arete(utilisateurs[0], noeuds_systemes[1], 2),
    Arete(utilisateurs[1], noeuds_systemes[1], 2),
    Arete(utilisateurs[2], noeuds_systemes[1], 2),
    Arete(utilisateurs[3], noeuds_systemes[2], 2),
    Arete(utilisateurs[4], noeuds_systemes[3], 2),
    Arete(utilisateurs[5], noeuds_systemes[4], 2),
    Arete(utilisateurs[6], noeuds_systemes[4], 2)
]

# Création du graphe
graphe = Graphe(aretes, utilisateurs, donnees, noeuds_systemes)

## Placement des données selon plusieurs façon

# naif(graphe)

# glouton(graphe)

# Utilisation de l'algorithme génétique pour résoudre le problème de placement de données
algorithme_genetique(graphe, taille_population=100, iterations=1000)


print(graphe)


