class Grille:
    def __init__(self):
        self.tableauCoup = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]

    def modifierGrille(self, x, y, pion):
        if self.estCaseVide(x, y):
            self.tableauCoup[x][y] = pion
        else: print("La case " + str(x) + " " + str(y) + " n'est pas libre")

    def estCaseVide(self, x, y):
        return True if self.tableauCoup[x][y] == " " else False

    def estComplete(self):
        for col in self.tableauCoup:
            if " " in col:
                return False
        return True

    def copier(self):
        """Crée une copie de la grille"""
        nouvelle_grille = Grille()
        for i in range(3):
            for j in range(3):
                nouvelle_grille.tableauCoup[i][j] = self.tableauCoup[i][j]
        return nouvelle_grille

    def verifierGagnant(self, pion):
        etat = self.tableauCoup
        lignes_victoire = [
            [etat[0][0], etat[0][1], etat[0][2]],
            [etat[1][0], etat[1][1], etat[1][2]],
            [etat[2][0], etat[2][1], etat[2][2]],
            [etat[0][0], etat[1][0], etat[2][0]],
            [etat[0][1], etat[1][1], etat[2][1]],
            [etat[0][2], etat[1][2], etat[2][2]],
            [etat[0][0], etat[1][1], etat[2][2]],
            [etat[2][0], etat[1][1], etat[0][2]],
        ]
        return [pion, pion, pion] in lignes_victoire

    def obtenirCasesVides(self):
        vides = []
        for x in range(3):
            for y in range(3):
                if self.tableauCoup[x][y] == " ":
                    vides.append([x, y])
        return vides

    def obtenirToutesLignes(self):
        """
        Retourne toutes les lignes (horizontales, verticales, diagonales)
        Pour la fonction d'évaluation de l'IA
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