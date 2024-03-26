class Donnee:
    def __init__(self, attr_id: int, attr_taille: int) -> None:
        """
        Initialise un objet Donnee avec un identifiant unique et une taille.
        
        :param attr_id: Identifiant de la donnée
        :param attr_taille: Taille de la donnée
        """
        self.id = 1000 + attr_id
        self.taille = attr_taille

class NoeudSysteme:
    def __init__(self, attr_id: int, attr_capaciteMemoire: int, attr_donneesStockeesLocalement: set, attr_noeudsAccessibles: set) -> None:
        """
        Initialise un objet NoeudSysteme avec un identifiant unique, une capacité mémoire, un ensemble de données stockées localement et un ensemble de noeuds accessibles.
        
        :param attr_id: Identifiant du noeud système
        :param attr_capaciteMemoire: Capacité mémoire du noeud système
        :param attr_donneesStockeesLocalement: Données stockées localement par le noeud système
        :param attr_noeudsAccessibles: Noeuds accessibles par le noeud système
        """
        self.id = 3000 + attr_id
        self.capaciteMemoire = attr_capaciteMemoire
        self.donneesStockeesLocalement = attr_donneesStockeesLocalement
        self.noeudsAccessibles = attr_noeudsAccessibles
        
class Utilisateur:
    def __init__(self, attr_id: int, attr_interets: set, attr_noeudSystemeAccessible: NoeudSysteme) -> None:
        """
        Initialise un objet Utilisateur avec un identifiant unique, un ensemble d'intérêts et le noeud système accessible.
        
        :param attr_id: Identifiant de l'utilisateur
        :param attr_interets: Ensemble des identifiants des intérêts de l'utilisateur
        :param attr_noeudSystemeAccessible: Noeud système accessible par l'utilisateur
        """
        self.id = 2000 + attr_id
        self.interets = attr_interets
        self.noeudSystemeAccessible = attr_noeudSystemeAccessible
        
class Arete:
    def __init__(self, setNoeud: set, poids: int) -> None:
        """
        Initialise un objet Arete avec un ensemble de noeuds reliés et un poids.
        
        :param setNoeud: Noeuds reliés par l'arête
        :param poids: Poids de l'arête
        """
        self.setNoeud = setNoeud
        self.poids = poids
    
class Graphe:
    def __init__(self, listArete: list) -> None:
        """
        Initialise un objet Graphe avec un ensemble d'arêtes.
        
        :param setArete: Ensemble des arêtes du graphe
        """
        self.listArete = listArete
        
############### TEST ##################

# Création des Données
donnees = [Donnee(i, 1) for i in range(9)]

# Création des Noeuds Systèmes
noeuds_systemes = [
    NoeudSysteme(0, 40, set(), {NoeudSysteme(3001, 0, set(), set()), NoeudSysteme(3002, 0, set(), set()), NoeudSysteme(3003, 0, set(), set()), NoeudSysteme(3004, 0, set(), set())}),
    NoeudSysteme(1, 50, {donnees[0], donnees[1], donnees[2], donnees[3], donnees[5]}, {NoeudSysteme(3000, 0, set(), set()), NoeudSysteme(3002, 0, set(), set()), NoeudSysteme(3003, 0, set(), set()), NoeudSysteme(3004, 0, set(), set()), Utilisateur(2000, set(), 0), Utilisateur(2001, set(), 0), Utilisateur(2002, set(), 0)}),
    NoeudSysteme(2, 40, {donnees[4]}, {NoeudSysteme(3000, 0, set(), set()), NoeudSysteme(3001, 0, set(), set()), NoeudSysteme(3003, 0, set(), set()), NoeudSysteme(3004, 0, set(), set()), Utilisateur(2003, set(), 0)}),
    NoeudSysteme(3, 50, {donnees[6]}, {NoeudSysteme(3000, 0, set(), set()), NoeudSysteme(3001, 0, set(), set()), NoeudSysteme(3002, 0, set(), set()), NoeudSysteme(3004, 0, set(), set()), Utilisateur(2004, set(), 0)}),
    NoeudSysteme(4, 40, {donnees[7], donnees[8]}, {NoeudSysteme(3000, 0, set(), set()), NoeudSysteme(3001, 0, set(), set()), NoeudSysteme(3002, 0, set(), set()), NoeudSysteme(3003, 0, set(), set()), Utilisateur(2005, set(), 0), Utilisateur(2006, set(), 0)})
]

# Création des Utilisateurs
utilisateurs = [
    Utilisateur(0, {donnees[0]}, NoeudSysteme(3001, 0, set(), set())),
    Utilisateur(1, {donnees[1], donnees[2]}, NoeudSysteme(3001, 0, set(), set())),
    Utilisateur(2, {donnees[3], donnees[5]}, NoeudSysteme(3001, 0, set(), set())),
    Utilisateur(3, {donnees[4]}, NoeudSysteme(3002, 0, set(), set())),
    Utilisateur(4, {donnees[6]}, NoeudSysteme(3003, 0, set(), set())),
    Utilisateur(5, {donnees[8]}, NoeudSysteme(3004, 0, set(), set())),
    Utilisateur(6, {donnees[7]}, NoeudSysteme(3004, 0, set(), set()))
]

# Création des arêtes
aretes = [
    Arete({noeuds_systemes[0], noeuds_systemes[1]}, 10),
    Arete({noeuds_systemes[0], noeuds_systemes[2]}, 20),
    Arete({noeuds_systemes[0], noeuds_systemes[3]}, 30),
    Arete({noeuds_systemes[0], noeuds_systemes[4]}, 40),
    Arete({noeuds_systemes[1], noeuds_systemes[2]}, 50),
    Arete({noeuds_systemes[1], noeuds_systemes[3]}, 60),
    Arete({noeuds_systemes[1], noeuds_systemes[4]}, 70),
    Arete({noeuds_systemes[2], noeuds_systemes[3]}, 80),
    Arete({noeuds_systemes[2], noeuds_systemes[4]}, 90),
    Arete({noeuds_systemes[3], noeuds_systemes[4]}, 100)
]

# Création du graphe
graphe = Graphe(arete.setNoeud for arete in aretes)

