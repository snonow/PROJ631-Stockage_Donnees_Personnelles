from classes import *
from PlacementDonneeStandard import placer_donnees_dans_graphe
 
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


graphe.dijkstra(2000, 2001)


placer_donnees_dans_graphe(graphe)


print(graphe)