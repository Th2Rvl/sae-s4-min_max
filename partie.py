import random

from grille import Grille
from joueur import Joueur, JoueurHumain, IA
from vue import afficherBienvenue, demanderNomJoueur, afficherGrille, demanderCoup, afficherTourJoue, nettoyageConsole, \
    afficherResultat


class Partie:
    def __init__(self):
        self.joueurHumain = JoueurHumain(demanderNomJoueur(), True if random.randint(0,1) == 0 else False)
        self.ia = IA(False if self.joueurHumain.aSonTour else True)
        self.grille = Grille()

    def lancerPartie(self):
        afficherBienvenue()
        victoire = False
        gagnant = ""

        while not self.grille.estComplete() and not victoire:
            # On affiche la grille au début de chaque tour
            afficherGrille(self.grille)

            # Identification du joueur actuel
            joueur_actuel = self.joueurHumain if self.joueurHumain.aSonTour else self.ia

            # Récupération du coup
            if self.joueurHumain.aSonTour:
                coup = ""
                while True :
                    coup = demanderCoup(self.joueurHumain.nom)
                    if self.grille.estCaseVide(int(coup[0]), int(coup[1])):
                        break
            else:
                coup = self.ia.choisirCoup(self.grille)

            # Action sur la grille
            self.grille.modifierGrille(coup[0], coup[1], joueur_actuel.pion)

            # Vérification de la victoire
            if self.grille.verifierGagnant(joueur_actuel.pion):
                victoire = True
                gagnant = joueur_actuel.nom

            # Affichage du tour et nettoyage (optionnel ici pour voir le dernier coup)
            afficherTourJoue(joueur_actuel.nom, coup)

            if not victoire:
                # Changement de tour
                self.joueurHumain.aSonTour = not self.joueurHumain.aSonTour
                self.ia.aSonTour = not self.ia.aSonTour
                nettoyageConsole()

        nettoyageConsole()
        afficherGrille(self.grille)  # Afficher la grille finale
        if victoire:
            afficherResultat(gagnant)
        else:
            afficherResultat("Nul")