import heapq

class Donnee:
    def __init__(self, id:int, taille:int):
        self.id = 1000 + id
        self.taille = taille
        
    def getID(self) -> int:
        return self.id
    
    def getTaille(self) -> int:
        return self.taille

class Utilisateur:
    def __init__(self, id:int, interets:list, noeudSystemeAccessible:int):
        self.id = 2000 + id
        self.interets = interets
        self.noeudSystemeAccessible = noeudSystemeAccessible

    def getInterets(self) -> list :
        return self.interets
    
    def getID(self) -> int:
        return self.id

class NoeudSysteme:
    def __init__(self, id:int, capaciteMemoire:int, noeudsAccessibles:list):
        self.id = 3000 + id
        self.capaciteMemoire = capaciteMemoire
        self.donneesStockeesLocalement = []
        self.noeudsAccessibles = noeudsAccessibles
        
    def getID(self) -> int:
        return self.id
    
    def isFull(self, lstPoidsAAjouter:list=None) -> bool:
        if lstPoidsAAjouter == None:
            lstPoidsAAjouter = []
            
        tailleDonneesSL = 0
        for donneeSL in self.donneesStockeesLocalement:
            tailleDonneesSL += donneeSL.getTaille()
        for poidsAAjouter in lstPoidsAAjouter:
            tailleDonneesSL += poidsAAjouter
        return  tailleDonneesSL > self.capaciteMemoire

class Arete:
    def __init__(self, n1:NoeudSysteme, n2:NoeudSysteme, poids:int=0):
        self.areteIds = {n1.id, n2.id}
        self.poids = poids

class Graphe:
    def __init__(self, aretes:list, utilisateurs:list, donneesAPlacer:list, noeudsSysteme:list):
        self.aretes = aretes
        self.utilisateurs = utilisateurs
        self.donneesAPlacer = donneesAPlacer
        self.noeudsSysteme = noeudsSysteme

    def getUtilisateurs(self) -> list[Utilisateur]:
        return self.utilisateurs
    
    def getAretes(self) -> list[Arete] :
        return self.aretes
    
    def getDonneesAPlacer(self) -> list[Donnee]:
        return self.donneesAPlacer
    
    def removeDonneesAPlacer(self, d:Donnee) -> None:
        self.donneesAPlacer.remove(d)
        
    def orderDonneesAPlacerByID(self) -> None:
        """
        Trie la liste des données à placer par leur identifiant.
        """
        self.donneesAPlacer.sort(key=lambda donnee: donnee.id)
    
    def getNoeudsSysteme(self) -> list[NoeudSysteme]:
        return self.noeudsSysteme
    
    def addNoeudSystemeDonneeSL(self, noeudSysID:int, donnee:Donnee):
        """
        Ajoute une donnée à la liste des données stockées localement dans un nœud système spécifié.

        Args:
            noeudSysID (int): L'identifiant du nœud système auquel ajouter la donnée.
            donnee (Donnee): La donnée à ajouter à la liste des données stockées localement.

        Raises:
            ValueError: Si le nœud système spécifié n'existe pas dans le graphe.
        """
        # Vérifie si le nœud système spécifié existe dans le graphe
        noeud_trouve = False
        for ns in self.noeudsSysteme:
            if ns.id == noeudSysID:
                ns.donneesStockeesLocalement.append(donnee)
                noeud_trouve = True
                break
        
        # Si le nœud système n'a pas été trouvé, lève une erreur
        if not noeud_trouve:
            raise ValueError("Le nœud système spécifié n'existe pas dans le graphe.")
    
    def dijkstra(self, depart: int, arrivee: int) -> list:
        """
        Calcule le chemin le moins coûteux entre un utilisateur et un nœud système en utilisant l'algorithme de Dijkstra.

        Args:
            depart (int): L'identifiant de l'utilisateur.
            arrivee (int): L'identifiant du nœud système.

        Returns:
            list: Liste des nœuds formant le chemin le moins coûteux.
        """
        distances = {node: float('infinity') for node in range(3000, 4000)}  # Initialisation des distances à l'infini
        distances[depart] = 0
        pq = [(0, depart)]  # Tuple (distance, noeud)

        while pq:
            distance_actuelle, noeud_actuel = heapq.heappop(pq)

            if distance_actuelle > distances[noeud_actuel]:
                continue

            for arete in self.aretes:
                if noeud_actuel in arete.areteIds:
                    voisin = (arete.areteIds - {noeud_actuel}).pop()
                    poids = arete.poids
                    distance = distance_actuelle + poids
                    if distance < distances[voisin]:
                        distances[voisin] = distance
                        heapq.heappush(pq, (distance, voisin))

        chemin = []
        noeud = arrivee
        while noeud != depart:
            chemin.append(noeud)
            for arete in self.aretes:
                if noeud in arete.areteIds and distances[noeud] - arete.poids == distances[(arete.areteIds - {noeud}).pop()]:
                    noeud = (arete.areteIds - {noeud}).pop()
                    break
        chemin.append(depart)
        return chemin[::-1]

    def cout_chemin(self, depart: int, arrivee: int) -> int:
        """
        Calcule le coût d'un chemin dans le graphe.

        Args:
            graphe (Graphe): Le graphe dans lequel le chemin est évalué.
            depart (int): L'identifiant de l'utilisateur.
            arrivee (int): L'identifiant du nœud système.

        Returns:
            int: Le coût total du chemin.
        """
        chemin = self.dijkstra(depart, arrivee)
        cout_total = 0
        for i in range(len(chemin) - 1):
            n1 = chemin[i]
            n2 = chemin[i + 1]
            for arete in self.aretes:
                if n1 in arete.areteIds and n2 in arete.areteIds:
                    cout_total += arete.poids
                    break
        return cout_total

