"""Fonction d'appartenance triangulaire."""
import numpy as np


def triangular(x, a, b, c):
    """Degré d'appartenance de x au triangle Tri(a, b, c).

    Accepte un nombre ou un tableau NumPy.
    Gère les épaulements : a == b (côté gauche vertical)
    ou b == c (côté droit vertical).
    """
    if not (a <= b <= c):
        raise ValueError(f"Paramètres invalides : il faut a <= b <= c, reçu ({a}, {b}, {c})")

    x = np.asarray(x, dtype=float)
    mu = np.zeros_like(x)

    # Côté montant : de a (degré 0) vers b (degré 1)
    if b > a:
        montant = (x >= a) & (x < b)
        mu = np.where(montant, (x - a) / (b - a), mu)

    # Côté descendant : de b (degré 1) vers c (degré 0)
    if c > b:
        descendant = (x > b) & (x <= c)
        mu = np.where(descendant, (c - x) / (c - b), mu)

    # Le sommet vaut toujours 1
    mu = np.where(x == b, 1.0, mu)

    return float(mu) if mu.ndim == 0 else mu