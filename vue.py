import os


def afficherGrille(grille):
    lettres = ["A", "B", "C"]
    print("    1   2   3")
    print("  ┌───┬───┬───┐")

    tableau = grille.tableauCoup if hasattr(grille, "tableauCoup") else grille

    for i, ligne in enumerate(tableau):

        contenu = "│".join([f" {cell} " for cell in ligne])
        print(f"{lettres[i]} │{contenu}│")

        if i < len(tableau) - 1:
            print("  ├───┼───┼───┤")

    print("  └───┴───┴───┘")


def afficherBienvenue():
    print("\n" + "*" * 30)
    print("*     JEU DU TIC-TAC-TOE     *")
    print("*" * 30)
    print("Règles : Alignez 3 symboles pour gagner.")
    print("Format des coups : Lettre + Chiffre (ex: B2)\n")


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
    chaine = input(f"Joueur {nomJoueur}, entrez une case (ex: B2) : ").strip().upper()
    ligne = chaine[0]
    if ligne not in ["A", "B", "C"] or int(chaine[1]) not in range(1, 4):
        afficherErreur("format")
        demanderCoup(nomJoueur)
        return None
    else:
        ligne = ord(ligne) - ord("A")
        colonne = int(chaine[1]) - 1
        return [ligne, colonne]


def demanderNomJoueur():
    return input("Entrez votre nom : ")


def demanderRejouer():
    reponse = input("\nVoulez-vous rejouer ? (o/n) : ").lower()
    return reponse == 'o' or reponse == 'oui'

def nettoyageConsole():
    os.system('cls' if os.name == 'nt' else 'clear')


# ---- Test ----
