"""Défuzzification par la méthode du centroïde."""
import numpy as np


def centroide(grille, agregat):
    """Centre de gravité de la courbe agrégée.

    grille  : les valeurs x (0 à 100)
    agregat : la hauteur de la courbe en chaque x
    """
    surface = np.sum(agregat)
    if surface == 0:
        raise ValueError("Surface nulle : impossible de calculer le centroïde.")
    return float(np.sum(grille * agregat) / surface)