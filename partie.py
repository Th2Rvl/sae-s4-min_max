import random
import vue
from grille import Grille
from joueur import Joueur, JoueurHumain, IA
from vue import afficherBienvenue, demanderNomJoueur, afficherGrille, demanderCoup, afficherTourJoue, nettoyageConsole, \
    afficherResultat


class Partie:
    def __init__(self):
        # Initialise une nouvelle partie en configurant les joueurs et la grille.
        vue.nettoyageConsole()
        # Le premier joueur est tiré au sort (1 chance sur 2)
        self.joueurHumain = JoueurHumain(demanderNomJoueur(), True if random.randint(0, 1) == 0 else False)
        # L'IA prend le tour opposé
        self.ia = IA(False if self.joueurHumain.aSonTour else True)
        self.grille = Grille()

    def lancerPartie(self):
        # Boucle principale du jeu.
        afficherBienvenue()
        victoire = False
        gagnant = ""

        # La boucle tourne tant que la grille n'est pas pleine et qu'il n'y a pas de gagnant
        while not self.grille.estComplete() and not victoire:
            afficherGrille(self.grille)

            # Identification du joueur dont c'est le tour
            joueur_actuel = self.joueurHumain if self.joueurHumain.aSonTour else self.ia

            # Récupération du coup
            # Si c'est au tour de l'humain
            if self.joueurHumain.aSonTour:
                coup = ""
                while True:
                    coup = demanderCoup(self.joueurHumain.nom)
                    # On vérifie si la case demandée par l'humain est bien libre
                    if self.grille.estCaseVide(int(coup[0]), int(coup[1])):
                        break
                    else:
                        vue.afficherErreur("occupee")
            else:
                # Sinon si c'est au tour de l'IA, on appelle son algorithme
                coup = self.ia.choisirCoup(self.grille)

            # Application du coup sur la grille
            self.grille.modifierGrille(coup[0], coup[1], joueur_actuel.pion)

            # Vérification des conditions de victoire
            if self.grille.verifierGagnant(joueur_actuel.pion):
                victoire = True
                gagnant = joueur_actuel.nom

            afficherTourJoue(joueur_actuel.nom, coup)

            if not victoire:
                # Changement de tour (alternance booléenne)
                self.joueurHumain.aSonTour = not self.joueurHumain.aSonTour
                self.ia.aSonTour = not self.ia.aSonTour
                nettoyageConsole()

        # Fin de la partie : affichage des résultats
        nettoyageConsole()
        afficherGrille(self.grille)
        if victoire:
            afficherResultat(gagnant)
        else:
            afficherResultat("Nul")

        self.rejouer()

    def rejouer(self):
        # Demande au joueur s'il veut rejouer.
        if vue.demanderRejouer():
            vue.nettoyageConsole()
            import appLauncher
            appLauncher.launch()
        else:
            exit()