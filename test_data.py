from classes import *
from PlacementDonnee import placer_donnees_dans_graphe
 
# Création des Données
donnees = [Donnee(i, 30) for i in range(9)]

# Création des Noeuds Systèmes
noeuds_systemes = [
    NoeudSysteme(0, 40, [3001, 3002, 3003, 3004]),
    NoeudSysteme(1, 50, [3000, 3002, 3003, 3004, 2000, 2001, 2002]),
    NoeudSysteme(2, 40, [3000, 3001, 3003, 3004, 2003]),
    NoeudSysteme(3, 50, [3000, 3001, 3002, 3004, 2004]),
    NoeudSysteme(4, 40, [3000, 3001, 3002, 3003, 2005, 2006])
]

# Création des Utilisateurs
utilisateurs = [
    Utilisateur(0, [1000], 3001),
    Utilisateur(1, [1001, 1002], 3001),
    Utilisateur(2, [1003, 1005], 3001),
    Utilisateur(3, [1004], 3002),
    Utilisateur(4, [1006], 3003),
    Utilisateur(5, [1008], 3004),
    Utilisateur(6, [1007], 3004)
]

# Création des arêtes
aretes = [
    Arete(noeuds_systemes[0], noeuds_systemes[1], 10),
    Arete(noeuds_systemes[0], noeuds_systemes[2], 20),
    Arete(noeuds_systemes[0], noeuds_systemes[3], 30),
    Arete(noeuds_systemes[0], noeuds_systemes[4], 40),
    Arete(noeuds_systemes[1], noeuds_systemes[2], 50),
    Arete(noeuds_systemes[1], noeuds_systemes[3], 60),
    Arete(noeuds_systemes[1], noeuds_systemes[4], 70),
    Arete(noeuds_systemes[2], noeuds_systemes[3], 80),
    Arete(noeuds_systemes[2], noeuds_systemes[4], 90),
    Arete(noeuds_systemes[3], noeuds_systemes[4], 100)
]

# Création du graphe
graphe = Graphe(aretes, utilisateurs, donnees, noeuds_systemes)

placer_donnees_dans_graphe(graphe)