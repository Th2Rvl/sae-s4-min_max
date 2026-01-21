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
        else: print("La case " + x + " " + y + " n'est pas libre")

    def estCaseVide(self, x, y):
        return True if self.tableauCoup[x][y] == " " else False

    def estComplete(self):
        for i in len(self.tableauCoup):
            if " " in self.tableauCoup[i]:
                return False
        return True