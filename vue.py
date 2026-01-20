def afficherGrille(grille):

    print("┌───┬───┬───┐")

    for i, ligne in enumerate(grille):

        contenu = "│".join([f" {cell} " for cell in ligne])
        print(f"│{contenu}│")

        if i < len(grille) - 1:
            print("├───┼───┼───┤")

    print("└───┴───┴───┘")



# ---- Test ----

ma_grille = [
    ["X", "O", " "],
    [" ", "X", " "],
    ["O", " ", "X"]
]

afficherGrille(ma_grille)