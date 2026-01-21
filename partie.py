import random

from grille import Grille
from joueur import Joueur, JoueurHumain, IA
from vue import afficherBienvenue, demanderNomJoueur, afficherGrille, demanderCoup


class Partie:
    def __init__(self):
        self.joueurHumain = JoueurHumain(demanderNomJoueur(), True if random.randint(0,1) == 0 else False)
        self.ia = IA(False if self.joueurHumain.aSonTour else True)
        self.grille = Grille()

    def lancerPartie(self):
        afficherBienvenue()
        while not self.grille.estComplete():
            afficherGrille(self.grille)

            coup = ""
            if self.joueurHumain.aSonTour:
                coup = demanderCoup(self.joueurHumain.nom)
            else: coup = self.ia.choisirCoup()
            self.grille.modifierGrille(coup[0], coup[1], self.joueurHumain.pion)