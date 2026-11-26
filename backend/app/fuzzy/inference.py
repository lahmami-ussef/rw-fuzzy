"""Moteur d'inférence de Mamdani : fuzzification, activation, implication, agrégation."""
import numpy as np

from .membership import triangular
from .defuzzification import centroide
from .variables import ENTREES, SORTIE, fuzzifier
from .rules import REGLES

# Grille de 1001 points de 0 à 100 sur laquelle on dessine la sortie
GRILLE = np.linspace(SORTIE["min"], SORTIE["max"], 1001)


class AucuneRegleActivee(Exception):
    """Levée quand toutes les règles ont une force de 0."""


def fuzzifier_joueur(stats):
    """
    stats = {"goals_per_90": 0.5, ...}
    Retourne les degrés d'appartenance de chaque variable.
    """
    resultat = {}

    for nom in ENTREES:                 # 1. Parcourir les 6 variables
        valeur = stats[nom]             # 2. Récupérer la valeur du joueur
        resultat[nom] = fuzzifier(nom, valeur)  # 3. Fuzzifier la valeur

    return resultat

def activer_regles(degres, regles=REGLES):
    """Calcule la force de chaque règle : MIN des degrés de ses conditions."""
    resultats = []
    for r in regles:
        force = min(degres[variable][ensemble] for variable, ensemble in r["si"].items())
        resultats.append({
            "id": r["id"],
            "groupe": r["groupe"],
            "alors": r["alors"],
            "force": float(force),
        })
    return resultats


def agreger(activations):
    """Implication (MIN) puis agrégation (MAX) de toutes les règles activées."""
    agregat = np.zeros_like(GRILLE)
    for act in activations:
        if act["force"] > 0:
            courbe = triangular(GRILLE, *SORTIE["ensembles"][act["alors"]])
            agregat = np.maximum(agregat, np.minimum(act["force"], courbe))
    return agregat


def inferer(stats):
    """Pipeline complet jusqu'à l'agrégation."""
    degres = fuzzifier_joueur(stats)
    activations = activer_regles(degres)

    if not any(a["force"] > 0 for a in activations):
        raise AucuneRegleActivee("Aucune règle ne s'active pour ce profil de joueur.")

    return {
        "degres": degres,
        "activations": activations,
        "agregat": agreger(activations),
    }

def evaluer(stats):
    """Pipeline complet : statistiques -> score sur 100."""
    res = inferer(stats)
    res["score"] = centroide(GRILLE, res["agregat"])
    return res