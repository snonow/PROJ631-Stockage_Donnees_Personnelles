from classes import *

def placer_donnee_pour_n_utilisateur_interesse(donnee: Donnee, utilisateurs: list[Utilisateur], graphe: Graphe) -> int:
    """
    Place la donnée pour l'utilisateur intéressé en trouvant 
    le meilleur nœud système disponible.

    Args:
        donnee (Donnee): La donnée à placer.
        utilisateurs (list[Utilisateur]): Utilisateurs intéressés par la donnée.
        graphe (Graphe): Graphe dans lequel on opère.

    Returns:
        int: L'identifiant de l'arête sur laquelle la donnée est placée, -1 si aucune arête n'est trouvée.
    """

    meilleure_noeud = None
    meilleure_poids_total = float('inf')

    # Parcourir tous les nœuds système pour trouver le meilleur nœud disponible
    for noeud in graphe.getNoeudsSysteme():
        # Vérifier si le nœud a suffisamment de capacité pour stocker la donnée
        if not noeud.isFull([donnee.getTaille()]):
            # Calculer le coût total entre le nœud et chaque utilisateur intéressé par cette donnée et l'additionner
            cout_chemin_total = sum(graphe.cout_chemin(utilisateur.getID(), noeud.getID()) for utilisateur in utilisateurs)
            if cout_chemin_total < meilleure_poids_total:
                meilleure_noeud = noeud
                meilleure_poids_total = cout_chemin_total
            
    if meilleure_noeud is not None:
        graphe.addNoeudSystemeDonneeSL(meilleure_noeud.getID(), donnee)
        print(meilleure_noeud.getID(), donnee)
    else:
        print("Impossible de placer la donnée.")

def naif(graphe: Graphe) -> None:
    """
    Place toutes les données dans le graphe en les associant aux nœuds système appropriés.

    Args:
        graphe (Graphe): Le graphe dans lequel placer les données.
    """
    graphe.orderDonneesAPlacerByID()
    for donnee in graphe.getDonneesAPlacer():
        utilisateurs_interesses = [utilisateur for utilisateur in graphe.getUtilisateurs() if donnee.getID() in utilisateur.getInterets()]
        placer_donnee_pour_n_utilisateur_interesse(donnee, utilisateurs_interesses, graphe)

def glouton(graphe: Graphe) -> None:
    '''
    Définition selon un triage glouton en amont des données les plus importants à placer.
    
    Args:
        graphe (Graphe): Le graphe dans lequel placer les données.
    '''
    graphe.orderDonneesAPlacerByHeuristiqueGlouton()
    for donnee in graphe.getDonneesAPlacer():
        utilisateurs_interesses = [utilisateur for utilisateur in graphe.getUtilisateurs() if donnee.getID() in utilisateur.getInterets()]
        placer_donnee_pour_n_utilisateur_interesse(donnee, utilisateurs_interesses, graphe)
