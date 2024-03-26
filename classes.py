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
    def __init__(self, aretes:list):
        self.aretes = aretes

