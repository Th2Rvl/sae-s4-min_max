import os


def afficherGrille(grille):
    # Dessine la grille dans la console avec des caractères ASCII.
    lettres = ["A", "B", "C"]
    print("    1   2   3")
    print("  ┌───┬───┬───┐")

    # On gère le fait de recevoir l'objet Grille complet ou juste son tableau
    tableau = grille.tableauCoup if hasattr(grille, "tableauCoup") else grille

    for i, ligne in enumerate(tableau):
        # Formatage du contenu de la ligne (ex: │ X │ O │   │)
        contenu = "│".join([f" {cell} " for cell in ligne])
        print(f"{lettres[i]} │{contenu}│")

        # Séparateurs entre les lignes (sauf pour la dernière)
        if i < len(tableau) - 1:
            print("  ├───┼───┼───┤")

    print("  └───┴───┴───┘")


def afficherBienvenue():
    # Affiche l'entête du jeu.
    print("\n" + "*" * 30)
    print("*     JEU DU TIC-TAC-TOE     *")
    print("*" * 30)
    print("Règles : Alignez 3 symboles pour gagner.")
    print("Format des coups : Lettre + Chiffre (ex: B2)\n")


def afficherTourJoue(nomJoueur, caseJoue):
    # Informe de l'action qui vient d'être réalisée.
    print(f"Le joueur {nomJoueur} a joué en case {caseJoue}.")


def afficherResultat(JoueurGagnant):
    # Affiche le message de fin de partie.
    if JoueurGagnant == "Nul":
        print("MATCH NUL ! Personne ne gagne.")
    else:
        print(f"FÉLICITATIONS ! Le joueur {JoueurGagnant} a gagné !")


def afficherErreur(type_erreur):
    # Centralise les messages d'erreur liés à la saisie de l'utilisateur.
    if type_erreur == "format":
        print("Erreur : Format invalide. Utilisez Lettre + Chiffre (ex: A1).")
    elif type_erreur == "occupee":
        print("Erreur : Cette case est déjà occupée !")
    elif type_erreur == "limites":
        print("Erreur : Cette case n'existe pas (A-C, 1-3).")


def demanderCoup(nomJoueur):
    """
    Demande au joueur où il veut jouer et transforme sa réponse (ex: 'B2')
    en coordonnées de tableau [ligne, colonne].
    Gère également les erreurs de saisie.
    """
    while True:
        try:
            chaine = input(f"Joueur {nomJoueur}, entrez une case (ex: B2) : ").strip().upper()

            # Vérification de la longueur de la saisie
            if len(chaine) != 2:
                afficherErreur("format")
                continue

            ligne = chaine[0]
            colonne_str = chaine[1]

            # Vérification des limites de la grille
            if ligne not in ["A", "B", "C"] or colonne_str not in ["1", "2", "3"]:
                afficherErreur("limites")
                continue

            # Conversion du caractère en index (A=0, B=1, C=2)
            ligne = ord(ligne) - ord("A")
            # Conversion du chiffre (1=0, 2=1, 3=2)
            colonne = int(colonne_str) - 1

            return [ligne, colonne]

        except (ValueError, IndexError):
            afficherErreur("format")


def demanderNomJoueur():
    # Récupère le nom du joueur humain.
    return input("Entrez votre nom : ")


def demanderRejouer():
    # Demande à la fin de la partie si l'utilisateur souhaite faire une autre manche.
    reponse = input("\nVoulez-vous rejouer ? (o/n) : ").lower()
    return reponse == 'o' or reponse == 'oui'


def nettoyageConsole():
    # Efface l'historique de la console pour une interface plus propre.
    os.system('cls' if os.name == 'nt' else 'clear')