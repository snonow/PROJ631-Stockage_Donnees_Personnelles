from classes import *

def quiEstInteresse(donneeID:int, utilisateurs:list):
    """
    Permet de trouver l'utilisateur intéressé 
    par la donné mis en argument
    """
    for u in utilisateurs:
        if donneeID in u.getInterets():
            return u

def PlacementDonnee(userInteresse: Utilisateur, donnee: Donnee, graphe: Graphe) -> int:
    """
    Place la donnée pour l'utilisateur intéressé en trouvant le meilleur noeud système disponible.

    Args:
        userInteresse (Utilisateur): L'utilisateur intéressé par la donnée.
        donnee (Donnee): La donnée à placer.
        graphe (Graphe): Graphe dans lequel on opère.

    Returns:
        int: L'identifiant de l'arête sur laquelle la donnée est placée, -1 si aucune arête n'est trouvée.
    """

    meilleure_noeud = None
    meilleure_poidsTotal = float('inf')

    # Parcourir toutes les arêtes pour trouver la meilleure arête disponible
    lstNoeudSysteme = graphe.getNoeudSystemes()
    for NoeudSysteme in lstNoeudSysteme:
        cout_chemin = graphe.cout_chemin(userInteresse.getID(), NoeudSysteme.getID())
        if (cout_chemin < meilleure_poidsTotal) and (not NoeudSysteme.isFull([donnee.getTaille()])) :
            meilleure_noeud = NoeudSysteme
            meilleure_poidsTotal = cout_chemin
            
    graphe.addNoeudSystemeDonneeSL(meilleure_noeud.getID(), donnee)

    if meilleure_noeud is None:
        print("Impossible de placer la donnée.")

def JeMetCaOu(graphe:Graphe) -> dict:
    """
    Fonction qui répond à la question 2 du projet du projet
    et qui permet de savoir où il faut mettre les données qui
    intèresse certains utilisateurs

    Args:
        donnee (Donnee): La donnée à placer
        graphe (Graphe): Le graphe dans lequel on opère
    """
    graphe.orderDonneesAPlacerByID()
    for donnee in graphe.donnees :
        userInteresse = quiEstInteresse(donnee.getID(), graphe.getUtilisateurs())
        PlacementDonnee(userInteresse, donnee, graphe)