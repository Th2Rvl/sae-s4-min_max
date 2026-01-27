import random


class Joueur:
    def __init__(self, nom, aSonTour):
        self.nom = nom
        self.aSonTour = aSonTour
        self.pion = "X" if self.aSonTour else "O"

class JoueurHumain(Joueur):
    def __init__(self, nom, aSonTour):
        super().__init__(nom, aSonTour)


class IA(Joueur):
    def __init__(self, aSonTour):
        super().__init__("IA", aSonTour)

    def choisirCoup(self):
        return [0, 0]
