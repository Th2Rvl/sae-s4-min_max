import random

from grille import Grille
from joueur import Joueur, JoueurHumain, IA



class Partie:
    def __init__(self):
        self.joueurHumain = JoueurHumain("Joueur1", True if random.randint(0,1) == 0 else False)
        self.ia = IA(False if self.joueurHumain.aSonTour else True)
        self.grille = Grille()

    def lancerPartie(self):
        while not self.grille.estComplete():
