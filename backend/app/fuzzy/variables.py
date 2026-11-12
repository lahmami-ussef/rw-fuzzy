"""Définition des variables floues : 6 entrées et 1 sortie.

Chaque ensemble est un triangle (a, b, c), voir membership.py.
Les ensembles "eleve" sont des épaulements droits (sommet = maximum du domaine).
"""
from .membership import triangular

ENTREES = {
    "goals_per_90": {
        "label": "Buts / 90",
        "min": 0, "max": 1,
        "ensembles": {
            "faible": (0, 0, 0.30),
            "moyen": (0.10, 0.40, 0.70),
            "eleve": (0.40, 1, 1),
        },
    },
    "assists_per_90": {
        "label": "Passes décisives / 90",
        "min": 0, "max": 1,
        "ensembles": {
            "faible": (0, 0, 0.15),
            "moyen": (0.05, 0.20, 0.40),
            "eleve": (0.25, 1, 1),
        },
    },
    "dribbling_success": {
        "label": "Dribbles réussis (%)",
        "min": 0, "max": 100,
        "ensembles": {
            "faible": (0, 0, 50),
            "moyen": (35, 55, 75),
            "eleve": (60, 100, 100),
        },
    },
    "key_passes_per_90": {
        "label": "Passes clés / 90",
        "min": 0, "max": 5,
        "ensembles": {
            "faible": (0, 0, 1.2),
            "moyen": (0.5, 1.8, 3),
            "eleve": (2, 5, 5),
        },
    },
    "crossing_accuracy": {
        "label": "Précision des centres (%)",
        "min": 0, "max": 100,
        "ensembles": {
            "faible": (0, 0, 35),
            "moyen": (20, 45, 70),
            "eleve": (55, 100, 100),
        },
    },
    "progressive_carries_per_90": {
        "label": "Courses progressives / 90",
        "min": 0, "max": 10,
        "ensembles": {
            "faible": (0, 0, 3),
            "moyen": (1.5, 4.5, 7),
            "eleve": (5, 10, 10),
        },
    },
}

SORTIE = {
    "nom": "performance_rw",
    "min": 0, "max": 100,
    "ensembles": {
        "faible": (0, 0, 40),
        "moyen": (20, 50, 80),
        "excellent": (60, 100, 100),
    },
}


def fuzzifier(nom, x):
    """Renvoie les degrés d'appartenance de x pour une variable d'entrée.

    Exemple : fuzzifier("dribbling_success", 72)
    -> {"faible": 0.0, "moyen": 0.15, "eleve": 0.30}
    """
    ensembles = ENTREES[nom]["ensembles"]
    return {ens: triangular(x, *params) for ens, params in ensembles.items()}