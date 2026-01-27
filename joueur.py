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
        self.pion_adversaire = "O" if self.pion == "X" else "X"

    def choisirCoup(self,grille):
        meilleur_score = float('-inf')
        meilleur_coup = None

        # Parcourir tous les coups possibles
        coups_possibles = grille.obtenirCasesVides()

        for coup in coups_possibles:
            ligne, col = coup

            # Simuler le coup
            grille_copie = grille.copier()
            grille_copie.modifierGrille(ligne, col, self.pion)

            # Évaluation avec Min-Max
            score = self.minimax(grille_copie, 8, False)

            # Garder le meilleur coup
            if score > meilleur_score:
                meilleur_score = score
                meilleur_coup = coup

        return meilleur_coup

    def minimax(self, grille, profondeur, est_max):
        if grille.verifierGagnant(self.pion):
            return 100  # L'IA gagne

        if grille.verifierGagnant(self.pion_adversaire):
            return -100  # L'adversaire gagne

        if grille.estComplete():
            return 0  # Match nul

        if profondeur == 0:
            return self.evaluerPosition(grille)

        if est_max:
            meilleur_score = float('-inf')

            for coup in grille.obtenirCasesVides():
                ligne, col = coup
                grille_copie = grille.copier()
                grille_copie.modifierGrille(ligne, col, self.pion)

                score = self.minimax(grille_copie, profondeur - 1, False)
                meilleur_score = max(meilleur_score, score)

            return meilleur_score

        else:
            meilleur_score = float('inf')

            for coup in grille.obtenirCasesVides():
                ligne, col = coup
                grille_copie = grille.copier()
                grille_copie.modifierGrille(ligne, col, self.pion_adversaire)

                score = self.minimax(grille_copie, profondeur - 1, True)
                meilleur_score = min(meilleur_score, score)

            return meilleur_score

    def evaluerPosition(self, grille):
        score = 0

        # Récupérer toutes les lignes
        toutes_lignes = grille.obtenirToutesLignes()

        for ligne in toutes_lignes:
            score += self.evaluerLigne(ligne)

        return score

    def evaluerLigne(self, ligne):
        """Évalue une ligne, colonne ou diagonale"""
        nb_ia = ligne.count(self.pion)
        nb_adv = ligne.count(self.pion_adversaire)
        nb_vide = ligne.count(' ')

        # Ligne bloquée (contient les deux symboles)
        if nb_ia > 0 and nb_adv > 0:
            return 0

        # Ligne potentiellement gagnante pour l'IA
        if nb_ia == 2 and nb_vide == 1:
            return 10
        if nb_ia == 1 and nb_vide == 2:
            return 1

        # Ligne potentiellement gagnante pour l'adversaire
        if nb_adv == 2 and nb_vide == 1:
            return -10
        if nb_adv == 1 and nb_vide == 2:
            return -1

        return 0  # Ligne vide
