class Grille:
    def __init__(self):
        # Initialisation d'une grille vide 3x3
        # Chaque case contient un espace " " par défaut
        self.tableauCoup = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]

    def modifierGrille(self, x, y, pion):
        # Place un pion (X ou O) aux coordonnées x, y si la case est libre.
        if self.estCaseVide(x, y):
            self.tableauCoup[x][y] = pion
        else:
            print("La case " + str(x) + " " + str(y) + " n'est pas libre")

    def estCaseVide(self, x, y):
        # Vérifie si une case spécifique est vide.
        return True if self.tableauCoup[x][y] == " " else False

    def estComplete(self):
        # Vérifie si la grille est totalement remplie (aucun espace vide).
        for col in self.tableauCoup:
            if " " in col:
                return False
        return True

    def copier(self):
        """
        Crée une copie indépendante de la grille.
        C'est crucial pour l'algorithme Minimax de l'IA afin de simuler
        des coups sans modifier la vraie grille de jeu.
        """
        nouvelle_grille = Grille()
        for i in range(3):
            for j in range(3):
                nouvelle_grille.tableauCoup[i][j] = self.tableauCoup[i][j]
        return nouvelle_grille

    def verifierGagnant(self, pion):
        # Vérifie si le pion donné a aligné 3 symboles (victoire).
        etat = self.tableauCoup
        # Liste de toutes les combinaisons gagnantes (lignes, colonnes, diagonales)
        lignes_victoire = [
            [etat[0][0], etat[0][1], etat[0][2]], # Ligne 1
            [etat[1][0], etat[1][1], etat[1][2]], # Ligne 2
            [etat[2][0], etat[2][1], etat[2][2]], # Ligne 3
            [etat[0][0], etat[1][0], etat[2][0]], # Colonne 1
            [etat[0][1], etat[1][1], etat[2][1]], # Colonne 2
            [etat[0][2], etat[1][2], etat[2][2]], # Colonne 3
            [etat[0][0], etat[1][1], etat[2][2]], # Diagonale descendante
            [etat[2][0], etat[1][1], etat[0][2]], # Diagonale montante
        ]
        # Si une ligne contient 3 fois le même pion, c'est gagné
        return [pion, pion, pion] in lignes_victoire

    def obtenirCasesVides(self):
        # Retourne une liste des coordonnées [x, y] de toutes les cases vides.
        vides = []
        for x in range(3):
            for y in range(3):
                if self.tableauCoup[x][y] == " ":
                    vides.append([x, y])
        return vides

    def obtenirToutesLignes(self):
        """
        Retourne toutes les lignes (horizontales, verticales, diagonales).
        Utilisé principalement pour la fonction d'évaluation heuristique de l'IA.
        """
        etat = self.tableauCoup
        lignes = [
            # Lignes horizontales
            [etat[0][0], etat[0][1], etat[0][2]],
            [etat[1][0], etat[1][1], etat[1][2]],
            [etat[2][0], etat[2][1], etat[2][2]],
            # Colonnes verticales
            [etat[0][0], etat[1][0], etat[2][0]],
            [etat[0][1], etat[1][1], etat[2][1]],
            [etat[0][2], etat[1][2], etat[2][2]],
            # Diagonales
            [etat[0][0], etat[1][1], etat[2][2]],
            [etat[2][0], etat[1][1], etat[0][2]],
        ]
        return lignes