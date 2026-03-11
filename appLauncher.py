from partie import Partie

def launch():
    """
    Point d'entrée principal du programme.
    Instancie une nouvelle partie et lance la boucle de jeu.
    """
    partie = Partie()
    partie.lancerPartie()

# Exécution initiale du jeu
launch()