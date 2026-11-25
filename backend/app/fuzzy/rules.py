"""Base de 20 règles floues IF-THEN (données seulement, aucun calcul ici).

Une règle = des conditions reliées par ET (opérateur MIN) -> un ensemble de sortie.
"""


def regle(id, groupe, si, alors):
    return {"id": id, "groupe": groupe, "si": si, "alors": alors}


G1 = "Efficacité offensive"
G2 = "Dribble et progression"
G3 = "Création d'occasions"
G4 = "Évaluation globale"

REGLES = [
    # --- Groupe 1 : buts et passes décisives ---
    regle("R1", G1, {"goals_per_90": "eleve", "assists_per_90": "eleve"}, "excellent"),
    regle("R2", G1, {"goals_per_90": "eleve", "assists_per_90": "moyen"}, "excellent"),
    regle("R3", G1, {"goals_per_90": "moyen", "assists_per_90": "eleve"}, "excellent"),
    regle("R4", G1, {"goals_per_90": "moyen", "assists_per_90": "moyen"}, "moyen"),
    regle("R5", G1, {"goals_per_90": "faible", "assists_per_90": "faible"}, "faible"),

    # --- Groupe 2 : dribbles et courses progressives ---
    regle("R6", G2, {"dribbling_success": "eleve", "progressive_carries_per_90": "eleve"}, "excellent"),
    regle("R7", G2, {"dribbling_success": "moyen", "progressive_carries_per_90": "moyen"}, "moyen"),
    regle("R8", G2, {"dribbling_success": "faible", "progressive_carries_per_90": "faible"}, "faible"),
    regle("R9", G2, {"dribbling_success": "eleve", "progressive_carries_per_90": "faible"}, "moyen"),
    regle("R10", G2, {"dribbling_success": "faible", "progressive_carries_per_90": "eleve"}, "moyen"),

    # --- Groupe 3 : passes clés et centres ---
    regle("R11", G3, {"key_passes_per_90": "eleve", "crossing_accuracy": "eleve"}, "excellent"),
    regle("R12", G3, {"key_passes_per_90": "moyen", "crossing_accuracy": "moyen"}, "moyen"),
    regle("R13", G3, {"key_passes_per_90": "faible", "crossing_accuracy": "faible"}, "faible"),
    regle("R14", G3, {"key_passes_per_90": "eleve", "crossing_accuracy": "faible"}, "moyen"),
    regle("R15", G3, {"key_passes_per_90": "faible", "crossing_accuracy": "eleve"}, "moyen"),

    # --- Groupe 4 : évaluation globale (3 statistiques combinées) ---
    regle("R16", G4, {"goals_per_90": "eleve", "key_passes_per_90": "eleve", "dribbling_success": "eleve"}, "excellent"),
    regle("R17", G4, {"goals_per_90": "faible", "assists_per_90": "faible", "key_passes_per_90": "faible"}, "faible"),
    regle("R18", G4, {"dribbling_success": "eleve", "key_passes_per_90": "eleve", "progressive_carries_per_90": "eleve"}, "excellent"),
    regle("R19", G4, {"goals_per_90": "moyen", "dribbling_success": "moyen", "key_passes_per_90": "moyen"}, "moyen"),
    regle("R20", G4, {"assists_per_90": "faible", "crossing_accuracy": "faible", "progressive_carries_per_90": "faible"}, "faible"),
]