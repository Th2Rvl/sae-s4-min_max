import random

class Joueur:
    # Classe de base pour un joueur.
    def __init__(self, nom, aSonTour):
        self.nom = nom
        self.aSonTour = aSonTour
        # Le premier joueur a toujours X, le second O
        self.pion = "X" if self.aSonTour else "O"

class JoueurHumain(Joueur):
    # Représente un joueur physique.
    def __init__(self, nom, aSonTour):
        super().__init__(nom, aSonTour)


class IA(Joueur):
    # Représente l'ordinateur, doté d'une intelligence artificielle Minimax.
    def __init__(self, aSonTour):
        super().__init__("IA", aSonTour)
        # Détermine le pion de l'adversaire pour l'évaluation des scores
        self.pion_adversaire = "O" if self.pion == "X" else "X"

    def choisirCoup(self, grille):
        # Point d'entrée de l'IA pour calculer le meilleur coup possible.
        meilleur_score = float('-inf')
        meilleur_coup = None

        # On parcourt tous les coups possibles à ce stade
        coups_possibles = grille.obtenirCasesVides()

        for coup in coups_possibles:
            ligne, col = coup

            # On simule le coup sur une copie de la grille
            grille_copie = grille.copier()
            grille_copie.modifierGrille(ligne, col, self.pion)

            # Évaluation du coup simulé avec l'algorithme Minimax
            # On commence avec est_max=False car c'est au tour de l'adversaire de jouer dans la simulation
            score = self.minimax(grille_copie, 8, False)

            # Si ce coup mène à un meilleur résultat, on le mémorise
            if score > meilleur_score:
                meilleur_score = score
                meilleur_coup = coup

        return meilleur_coup

    def minimax(self, grille, profondeur, est_max):
        # Algorithme Minimax : explore l'arbre des possibilités pour trouver le meilleur coup.
        # Conditions d'arrêt : fin de partie (victoire/défaite)
        if grille.verifierGagnant(self.pion):
            return 100  # L'IA gagne
        if grille.verifierGagnant(self.pion_adversaire):
            return -100  # L'adversaire gagne
        if grille.estComplete():
            return 0  # Match nul

        # Condition d'arrêt : limite de profondeur atteinte
        if profondeur == 0:
            return self.evaluerPosition(grille)

        if est_max:
            # Tour de l'IA (veut maximiser le score)
            meilleur_score = float('-inf')
            for coup in grille.obtenirCasesVides():
                ligne, col = coup
                grille_copie = grille.copier()
                grille_copie.modifierGrille(ligne, col, self.pion)

                score = self.minimax(grille_copie, profondeur - 1, False)
                meilleur_score = max(meilleur_score, score)
            return meilleur_score
        else:
            # Tour de l'adversaire humain (veut minimiser le score de l'IA)
            meilleur_score = float('inf')
            for coup in grille.obtenirCasesVides():
                ligne, col = coup
                grille_copie = grille.copier()
                grille_copie.modifierGrille(ligne, col, self.pion_adversaire)

                score = self.minimax(grille_copie, profondeur - 1, True)
                meilleur_score = min(meilleur_score, score)
            return meilleur_score

    def evaluerPosition(self, grille):
        # Calcule un score global pour l'état actuel de la grille.
        score = 0
        toutes_lignes = grille.obtenirToutesLignes()
        for ligne in toutes_lignes:
            score += self.evaluerLigne(ligne)
        return score

    def evaluerLigne(self, ligne):
        """
        Évalue une ligne, colonne ou diagonale spécifique.
        Attribue des points si l'IA ou l'adversaire est proche de gagner.
        """
        nb_ia = ligne.count(self.pion)
        nb_adv = ligne.count(self.pion_adversaire)
        nb_vide = ligne.count(' ')

        # Ligne bloquée (contient les deux symboles, personne ne peut y gagner)
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

        return 0  # Ligne totalement vide