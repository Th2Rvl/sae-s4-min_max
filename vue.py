def afficherGrille(grille):
    lettres = ["A", "B", "C"]
    print("    1   2   3")
    print("  ┌───┬───┬───┐")

    for i, ligne in enumerate(grille):

        contenu = "│".join([f" {cell} " for cell in ligne])
        print(f"{lettres[i]} │{contenu}│")

        if i < len(grille) - 1:
            print("  ├───┼───┼───┤")

    print("  └───┴───┴───┘")


def afficherTourJoue(nomJoueur, caseJoue):
    print(f"Le joueur {nomJoueur} a joué en case {caseJoue}.")


def afficherResultat(JoueurGagnant):
    if JoueurGagnant == "Nul":
        print("MATCH NUL ! Personne ne gagne.")
    else:
        print(f"FÉLICITATIONS ! Le joueur {JoueurGagnant} a gagné !")


def afficherErreur(type_erreur):
    if type_erreur == "format":
        print("Erreur : Format invalide. Utilisez Lettre + Chiffre (ex: A1).")
    elif type_erreur == "occupee":
        print("Erreur : Cette case est déjà occupée !")
    elif type_erreur == "limites":
        print("Erreur : Cette case n'existe pas (A-C, 1-3).")


def demanderCoup(nomJoueur):
    return input(f"Joueur {nomJoueur}, entrez une case (ex: B2) : ").strip().upper()


def demanderNomJoueur():
    return input("Entrez votre nom : ")


# ---- Test ----

ma_grille = [
    ["X", "O", " "],
    [" ", "X", " "],
    ["O", " ", "X"]
]

afficherGrille(ma_grille)

print(demanderNomJoueur())