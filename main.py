class Donnee:
    def __init__(self, id:int, taille:int):
        self.id = 1000 + id
        self.taille = taille

class Utilisateur:
    def __init__(self, id:int, interets:list, noeudSystemeAccessible:int):
        self.id = 2000 + id
        self.interets = interets
        self.noeudSystemeAccessible = noeudSystemeAccessible

class NoeudSysteme:
    def __init__(self, id:int, capaciteMemoire:int, donneesStockeesLocalement:list, noeudsAccessibles:list):
        self.id = 3000 + id
        self.capaciteMemoire = capaciteMemoire
        self.donneesStockeesLocalement = donneesStockeesLocalement
        self.noeudsAccessibles = noeudsAccessibles

class Arete:
    def __init__(self, n1:NoeudSysteme, n2:NoeudSysteme, poids:int=0):
        self.areteIds = {n1.id, n2.id}
        self.poids = poids

class Graphe:
    def __init__(self, areteIds:list):
        self.areteIds = areteIds

# Création des Données
donnees = [Donnee(i, 1) for i in range(9)]

# Création des Noeuds Systèmes
noeuds_systemes = [
    NoeudSysteme(0, 40, [], [3001, 3002, 3003, 3004]),
    NoeudSysteme(1, 50, [1000, 1001, 1002, 1003, 1005], [3000, 3002, 3003, 3004, 2000, 2001, 2002]),
    NoeudSysteme(2, 40, [1004], [3000, 3001, 3003, 3004, 2003]),
    NoeudSysteme(3, 50, [1006], [3000, 3001, 3002, 3004, 2004]),
    NoeudSysteme(4, 40, [1007, 1008], [3000, 3001, 3002, 3003, 2005, 2006])
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

# Ensemble contenant toutes les arêtes
all_arete_ids = [arete.areteIds for arete in aretes]

# Création du graphe
graphe = Graphe(all_arete_ids)
