import heapq

class Donnee:
    def __init__(self, id:int, taille:int):
        self.id = id
        self.taille = taille
        self.heuristique = 0
        
    def __str__(self) -> str:
        return  f"Donnee({self.id}, {self.taille})"
        
    def getID(self) -> int:
        return self.id
    
    def getTaille(self) -> int:
        return self.taille
    
    def setHeuristique(self, heuristique:float) -> None :
        self.heuristique = heuristique
        
    def getHeuristique(self) -> None :
        return self.heuristique
        
class Utilisateur:
    def __init__(self, id:int, interets:list, noeudSystemeAccessible:int):
        self.id = id
        self.interets = interets
        self.noeudSystemeAccessible = noeudSystemeAccessible

    def getInterets(self) -> list:
        return self.interets
    
    def getID(self) -> int:
        return self.id
    
    def getNoeudSystemeAccessible(self) -> int:
        return self.noeudSystemeAccessible
    

class NoeudSysteme:
    def __init__(self, id:int, capaciteMemoire:int, noeudsAccessibles:list):
        self.id = id
        self.capaciteMemoire = capaciteMemoire
        self.donneesStockeesLocalement = []
        self.noeudsAccessibles = noeudsAccessibles
        
    def __str__(self) -> str:
        return f"Noeud Système {self.id}: Capacité Mémoire = {self.capaciteMemoire}, Noeuds Accessibles = {self.noeudsAccessibles}"
        
    def getID(self) -> int:
        return self.id
    
    def getCapaciteMemoire(self) -> int :
        return self.capaciteMemoire
    
    def getNoeudsAccessibles(self) -> list :
        return self.noeudsAccessibles
    
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
        self.noeudDepart = n1
        self.noeudArrivee = n2
        self.areteIds = {n1.id, n2.id}
        self.poids = poids

    def ___str__(self) -> str:
        return f"id : {self.areteIds}\tpoids : {self.poids}"
    
    def getAretesIds(self) -> set:
        return self.areteIds
    
    def getNoeudDepart(self) -> int :
        return self.noeudDepart
    
    def getNoeudArrivee(self) -> int :
        return self.noeudArrivee
    
    def getPoids(self) -> int:
        return self.poids
    
class Graphe:
    def __init__(self, aretes:list[Arete], utilisateurs:list[Utilisateur], donneesAPlacer:list[Donnee], noeudsSysteme:list[NoeudSysteme]):
        self.aretes = aretes
        self.utilisateurs = utilisateurs
        self.donneesAPlacer = donneesAPlacer
        self.noeudsSysteme = noeudsSysteme
        self.voisins = self.calculer_voisins()
        
    def __str__(self) -> str:
        res = ''
        for noeud in self.noeudsSysteme:
            res += str(noeud.id) + ' ' + str(noeud.capaciteMemoire) + ' Données : { '
            for donnee in noeud.donneesStockeesLocalement:
                res += str(donnee) + ' '
            res += '}\n'
        return res
        
        
    def calculer_voisins(self) -> dict:
        """
        Calcule les voisins pour chaque nœud dans le graphe, y compris les utilisateurs.

        Returns:
            dict: Un dictionnaire où les clés sont les identifiants des nœuds et les valeurs sont les ensembles de voisins.
        """
        voisins = {}

        # Ajouter les utilisateurs comme clés avec leur unique voisin
        for utilisateur in self.utilisateurs:
            voisins[utilisateur.id] = {utilisateur.noeudSystemeAccessible}

        # Ajouter les voisins des nœuds système
        for arete in self.aretes:
            n1, n2 = arete.areteIds
            voisins.setdefault(n1, set()).add(n2)
            voisins.setdefault(n2, set()).add(n1)

            # Vérifier si les nœuds sont également des utilisateurs pour garantir la bidirectionnalité
            if n1 in self.utilisateurs:
                voisins[n2].add(n1)
            if n2 in self.utilisateurs:
                voisins[n1].add(n2)

        return voisins

    def getUtilisateurs(self) -> list[Utilisateur]:
        return self.utilisateurs
    
    def getAretes(self) -> list[Arete] :
        return self.aretes
    
    def getDonneesAPlacer(self) -> list[Donnee]:
        return self.donneesAPlacer
    
    def removeDonneesAPlacer(self, d:Donnee) -> None:
        self.donneesAPlacer.remove(d)
        
    def copie(self):
        """
        Crée une copie profonde du graphe.

        Returns:
            Graphe: Une copie profonde du graphe.
        """
        # Copie des listes d'objets en utilisant des listes par compréhension
        aretes_copie = [Arete(arete.getNoeudDepart(), arete.getNoeudArrivee(), arete.getPoids()) for arete in self.aretes]
        utilisateurs_copie = [Utilisateur(utilisateur.getID(), utilisateur.getInterets(), utilisateur.getNoeudSystemeAccessible()) for utilisateur in self.utilisateurs]
        donneesAPlacer_copie = [Donnee(donnee.getID(), donnee.getTaille()) for donnee in self.donneesAPlacer]
        noeudsSysteme_copie = [NoeudSysteme(noeud.getID(), noeud.getCapaciteMemoire(), noeud.getNoeudsAccessibles()) for noeud in self.noeudsSysteme]

        # Retourne un nouveau graphe avec les listes copiées
        return Graphe(aretes_copie, utilisateurs_copie, donneesAPlacer_copie, noeudsSysteme_copie)
        
    def orderDonneesAPlacerByID(self) -> None:
        """
        Trie la liste des données à placer par leur identifiant.
        """
        self.donneesAPlacer.sort(key=lambda donnee: donnee.id)
    
    def orderDonneesAPlacerByHeuristiqueGlouton(self) -> None:
        """
        Trie la liste des selon leurs ratio décroissant entre nb d'utilisateurs 
        intéressé et leurs poids.
        """
        for donnee in self.donneesAPlacer:
            utilisateurs_interesses = [utilisateur for utilisateur in self.utilisateurs if donnee.getID() in utilisateur.getInterets()]
            n = len(utilisateurs_interesses)
            donnee.setHeuristique(n/donnee.getTaille())
        self.donneesAPlacer.sort(key=lambda donnee: donnee.getHeuristique(), reverse=True)
    
    def getNoeudsSysteme(self) -> list[NoeudSysteme]:
        return self.noeudsSysteme
    
    def getNoeudSystemeByID(self, id_noeud) -> NoeudSysteme:
        for noeud in self.noeudsSysteme:
            if noeud.getID() == id_noeud:
                return noeud
            
    def getTailleDisponibleNoeud(self, id_noeud) -> int:
        noeud = self.getNoeudSystemeByID(id_noeud)
        return noeud.getCapaciteMemoire()
        
    def getUtilisateursInteressesParDonnee(self, id: int):
        return [utilisateur for utilisateur in self.getUtilisateurs() if id in utilisateur.getInterets()]
        
    
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
        Calcule le chemin le moins coûteux entre un utilisateur et un nœud 
        système en utilisant l'algorithme de Dijkstra.

        Args:
            depart (int): L'identifiant de l'utilisateur.
            arrivee (int): L'identifiant du nœud système.

        Returns:
            list: Liste des nœuds formant le chemin le moins coûteux.
        """
        distances = {node: float('infinity') for node in self.voisins.keys()}  # Initialisation des distances à l'infini
        distances[depart] = 0
        pq = [(0, depart)]  # Tuple (distance, noeud)

        while pq:
            distance_actuelle, noeud_actuel = heapq.heappop(pq)

            if distance_actuelle > distances[noeud_actuel]:
                continue

            # Utilisation des voisins précalculés
            for voisin in self.voisins[noeud_actuel]:
                poids = self.get_poids_arete(noeud_actuel, voisin)
                distance = distance_actuelle + poids
                if distance < distances[voisin]:
                    distances[voisin] = distance
                    heapq.heappush(pq, (distance, voisin))
                    

        chemin = []
        noeud = arrivee
        while noeud != depart:
            chemin.append(noeud)
            noeud = min(self.voisins[noeud], key=lambda x: distances[x])
        chemin.append(depart)
        return chemin[::-1]


    def get_poids_arete(self, n1: int, n2: int) -> int:
        """
        Récupère le poids de l'arête entre deux nœuds.

        Args:
            n1 (int): L'identifiant du premier nœud.
            n2 (int): L'identifiant du deuxième nœud.

        Returns:
            int: Le poids de l'arête entre les deux nœuds.
        """
        for arete in self.aretes:
            if n1 in arete.areteIds and n2 in arete.areteIds:
                return arete.poids
        return float('infinity')

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

