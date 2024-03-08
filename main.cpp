#include <iostream>
#include <list>
#include <set>
using namespace std;

class Donnee {
    public:
        int id; // UNIQUE
        int taille;
        Donnee(int attr_id, int attr_taille) {
            id = 1000 + attr_id; // Ajout de 1000 afin de connaître le type de la données juste en regardant le premier chiffre + garantie unicité des ids
            taille = attr_taille;
        }
};

class Utilisateur {
    public:
        int id; // UNIQUE
        list<int> interets; // Liste des ids des i                                                                                                                                               nterets des utilisateurs
        int noeudSystemeAccessible; // Il est unique
        Utilisateur(int attr_id, list<int> attr_interets, int attr_noeudSystemeAccessible) {
            id = 2000 + attr_id; // Ajout de 2000 afin de connaître le type de la données juste en regardant le premier chiffre + garantie unicité des ids
            interets = attr_interets;
            noeudSystemeAccessible = attr_noeudSystemeAccessible;
        }
};

class NoeudSysteme {
    public:
        int id; // UNIQUE
        int capaciteMemoire;
        list<int> donneesStockeesLocalement;
        list<int> noeudsAccessibles; // les ides des autres Noeuds Systeme et des Noeuds Utilisateurs
        NoeudSysteme(int attr_id, int attr_capaciteMemoire, list<int> attr_donneesStockeesLocalement, list<int> attr_noeudsAccessibles) {
            id = 3000 + attr_id; // Ajout de 3000 afin de connaître le type de la données juste en regardant le premier chiffre + garantie unicité des ids
            capaciteMemoire = attr_capaciteMemoire;
            donneesStockeesLocalement = attr_donneesStockeesLocalement;
            noeudsAccessibles = attr_noeudsAccessibles;
        }
};

class Graphe : public Arrete {
    public:
        set<int> nodesIds;
    Graphe(set<int> attr_nodesIds)
};

class Arrete {
    public:
        set<int> ArreteIds;
        int poids; // Représente le temps d'accès entre les deux noeuds dans le set
    Arrete(set<int> attr_ArreteIds, int attr_poids) {
        ArreteIds = attr_ArreteIds;
        poids = attr_poids;
    }
};

// Implémentation du graphe "Figure 1" dans le sujet

int main() {
    // Création des Données
    Donnee D0(0,1);
    Donnee D1(1,1);
    Donnee D2(2,1);
    Donnee D3(3,1);
    Donnee D4(4,1);
    Donnee D5(5,1);
    Donnee D6(6,1);
    Donnee D7(7,1);
    Donnee D8(8,1);

    // Création des Noeuds Systèmes 
    NoeudSysteme N0(0, 40, {}, {3001, 3002, 3003, 3004});
    NoeudSysteme N1(1, 50, {1000, 1001, 1002, 1003, 1005}, {3000, 3002, 3003, 3004, 2000, 2001, 2002});
    NoeudSysteme N2(2, 40, {1004}, {3000, 3001, 3003, 3004, 2003});
    NoeudSysteme N3(3, 50, {1006}, {3000, 3001, 3002, 3004, 2004});
    NoeudSysteme N4(4, 40, {1007, 1008}, {3000, 3001, 3002, 3003, 2005, 2006});

    // Création des Utilisateurs
    Utilisateur U0(0, {1000}, 3001);
    Utilisateur U1(1, {1001, 1002}, 3001);
    Utilisateur U2(2, {1003, 1005}, 3001);
    Utilisateur U3(3, {1004}, 3002);
    Utilisateur U4(4, {1006}, 3003);
    Utilisateur U5(5, {1008}, 3004);
    Utilisateur U6(6, {1007}, 3004);

    // Création du graphe avec les poids
    Arrete 

    return 0;
};