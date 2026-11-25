"""Modèles Pydantic : ce que l'API accepte et ce qu'elle renvoie."""
from pydantic import BaseModel, Field


class JoueurStats(BaseModel):
    """Entrée : les 6 statistiques. Les bornes = les domaines des variables."""
    goals_per_90: float = Field(ge=0, le=1, allow_inf_nan=False)
    assists_per_90: float = Field(ge=0, le=1, allow_inf_nan=False)
    dribbling_success: float = Field(ge=0, le=100, allow_inf_nan=False)
    key_passes_per_90: float = Field(ge=0, le=5, allow_inf_nan=False)
    crossing_accuracy: float = Field(ge=0, le=100, allow_inf_nan=False)
    progressive_carries_per_90: float = Field(ge=0, le=10, allow_inf_nan=False)


class RegleActivee(BaseModel):
    id: str
    groupe: str
    alors: str
    force: float


class PointCourbe(BaseModel):
    x: float
    y: float


class ResultatEvaluation(BaseModel):
    """Sortie de POST /evaluate."""
    score: float
    categorie: str
    degres_categorie: dict[str, float]
    points_forts: list[str]
    points_faibles: list[str]
    degres: dict[str, dict[str, float]]
    regles_activees: list[RegleActivee]
    courbe_agregee: list[PointCourbe]