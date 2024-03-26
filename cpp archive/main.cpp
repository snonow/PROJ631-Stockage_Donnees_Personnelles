#include <iostream>
#include <list>
#include <unordered_set>
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

// class NoeudSysteme {
//     public:
//         int id; // UNIQUE
//         int capaciteMemoire;
//         list<int> donneesStockeesLocalement;
//         list<int> noeudsAccessibles; // les ides des autres Noeuds Systeme et des Noeuds Utilisateurs
//         NoeudSysteme(int attr_id, int attr_capaciteMemoire, list<int> attr_donneesStockeesLocalement, list<int> attr_noeudsAccessibles) {
//             id = 3000 + attr_id; // Ajout de 3000 afin de connaître le type de la données juste en regardant le premier chiffre + garantie unicité des ids
//             capaciteMemoire = attr_capaciteMemoire;
//             donneesStockeesLocalement = {attr_donneesStockeesLocalement};
//             noeudsAccessibles = {attr_noeudsAccessibles};
//         }
// };

// class Arete {
//     public:
//         unordered_set<int> areteIds; // Prend les ids des deux Noeuds Systèmes qu'elle relie
//         int poids; // Représente le temps d'accès entre les deux noeuds dans le set
        
//         Arete(unordered_set<int> attr_areteIds, int attr_poids) {
//             areteIds = attr_areteIds;
//             poids = attr_poids;
//         }

//         Arete(const NoeudSysteme& n1, const NoeudSysteme& n2, int attr_poids) {
//             areteIds = {n1.id, n2.id};
//             poids = attr_poids;
//         }
// };

// class Graphe {
// public:
//     unordered_set< unordered_set<int> > areteIds;
//     Graphe(unordered_set< unordered_set<int> > attr_areteIds) {
//         areteIds = attr_areteIds;
//     }
// };


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
    list<int> N0list1;
    list<int> N0list2 = {3001, 3002, 3003, 3004};
    // NoeudSysteme N0(0, 40, N0list1, N0list2);
    // NoeudSysteme N1(1, 50, list<int>{1000, 1001, 1002, 1003, 1005}, list<int>{3000, 3002, 3003, 3004, 2000, 2001, 2002});
    // NoeudSysteme N2(2, 40, {1004}, {3000, 3001, 3003, 3004, 2003});
    // NoeudSysteme N3(3, 50, {1006}, {3000, 3001, 3002, 3004, 2004});
    // NoeudSysteme N4(4, 40, {1007, 1008}, {3000, 3001, 3002, 3003, 2005, 2006});

    // // Création des Utilisateurs
    // Utilisateur U0(0, {1000}, 3001);
    // Utilisateur U1(1, {1001, 1002}, 3001);
    // Utilisateur U2(2, {1003, 1005}, 3001);
    // Utilisateur U3(3, {1004}, 3002);
    // Utilisateur U4(4, {1006}, 3003);
    // Utilisateur U5(5, {1008}, 3004);
    // Utilisateur U6(6, {1007}, 3004);

    // // Création des arêtes
    // unordered_set<int> areteIds1;
    // areteIds1.insert(N0.id);
    // areteIds1.insert(N1.id);
    // Arete arete1(areteIds1, 10);

    // unordered_set<int> areteIds2;
    // areteIds2.insert(N0.id);
    // areteIds2.insert(N2.id);
    // Arete arete2(areteIds2, 20);

    // unordered_set<int> areteIds3;
    // areteIds3.insert(N0.id);
    // areteIds3.insert(N3.id);
    // Arete arete3(areteIds3, 30);

    // unordered_set<int> areteIds4;
    // areteIds4.insert(N0.id);
    // areteIds4.insert(N4.id);
    // Arete arete4(areteIds4, 40);

    // unordered_set<int> areteIds5;
    // areteIds5.insert(N1.id);
    // areteIds5.insert(N2.id);
    // Arete arete5(areteIds5, 50);

    // unordered_set<int> areteIds6;
    // areteIds6.insert(N1.id);
    // areteIds6.insert(N3.id);
    // Arete arete6(areteIds6, 60);

    // unordered_set<int> areteIds7;
    // areteIds7.insert(N1.id);
    // areteIds7.insert(N4.id);
    // Arete arete7(areteIds7, 70);

    // unordered_set<int> areteIds8;
    // areteIds8.insert(N2.id);
    // areteIds8.insert(N3.id);
    // Arete arete8(areteIds8, 80);

    // unordered_set<int> areteIds9;
    // areteIds9.insert(N2.id);
    // areteIds9.insert(N4.id);
    // Arete arete9(areteIds9, 90);

    // unordered_set<int> areteIds10;
    // areteIds10.insert(N3.id);
    // areteIds10.insert(N4.id);
    // Arete arete10(areteIds10, 100);

    // // Ensemble contenant toutes les arêtes
    // unordered_set< unordered_set<int> > allAreteIds;
    // allAreteIds.insert(arete1.areteIds);
    // allAreteIds.insert(arete2.areteIds);
    // allAreteIds.insert(arete3.areteIds);
    // allAreteIds.insert(arete4.areteIds);
    // allAreteIds.insert(arete5.areteIds);
    // allAreteIds.insert(arete6.areteIds);
    // allAreteIds.insert(arete7.areteIds);
    // allAreteIds.insert(arete8.areteIds);
    // allAreteIds.insert(arete9.areteIds);
    // allAreteIds.insert(arete10.areteIds);

    // // Création du graphe
    // Graphe g(allAreteIds); // Poids arbitraire (1000)

    return 0;
};