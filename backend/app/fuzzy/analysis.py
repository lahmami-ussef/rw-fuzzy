"""Interprétation du résultat : catégorie, points forts et points faibles."""
from .membership import triangular
from .variables import ENTREES, SORTIE

NOMS_CATEGORIES = {"faible": "Faible", "moyen": "Moyen", "excellent": "Excellent"}


def categorie(score):
    """Catégorie = ensemble de sortie qui a le plus fort degré au score obtenu."""
    degres = {nom: triangular(score, *params) for nom, params in SORTIE["ensembles"].items()}
    meilleur = max(degres, key=degres.get)
    return NOMS_CATEGORIES[meilleur], degres


def points_forts_faibles(degres):
    """degres = résultat de fuzzifier_joueur.

    Pour chaque statistique, on regarde l'ensemble dominant (le plus fort degré) :
    - "eleve" dominant  -> point fort
    - "faible" dominant -> point faible
    - "moyen" dominant  -> neutre
    """
    ordre = ["moyen", "eleve", "faible"]  # en cas d'égalité, "moyen" gagne (neutre)
    forts, faibles = [], []
    for nom, d in degres.items():
        dominant = max(ordre, key=lambda e: d[e])
        label = ENTREES[nom]["label"]
        if dominant == "eleve":
            forts.append(label)
        elif dominant == "faible":
            faibles.append(label)
    return forts, faibles