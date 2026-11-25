"""API FastAPI : évaluation d'un ailier droit par logique floue (Mamdani)."""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from .fuzzy.analysis import categorie, points_forts_faibles
from .fuzzy.inference import GRILLE, AucuneRegleActivee, evaluer
from .schemas import JoueurStats, ResultatEvaluation

app = FastAPI(title="RW Fuzzy Evaluator")

# Autorise le frontend React (Vite : 5173, Create React App : 3000) à appeler l'API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/evaluate", response_model=ResultatEvaluation)
def evaluate(joueur: JoueurStats):
    stats = joueur.model_dump()

    try:
        res = evaluer(stats)
    except AucuneRegleActivee as e:
        raise HTTPException(status_code=422, detail=str(e))

    score = res["score"]
    nom_categorie, degres_cat = categorie(score)
    forts, faibles = points_forts_faibles(res["degres"])

    # 1 point sur 10 de la grille (101 points) : suffisant pour un graphique
    courbe = [
        {"x": float(x), "y": float(y)}
        for x, y in zip(GRILLE[::10], res["agregat"][::10])
    ]

    return {
        "score": round(score, 2),
        "categorie": nom_categorie,
        "degres_categorie": {k: round(v, 3) for k, v in degres_cat.items()},
        "points_forts": forts,
        "points_faibles": faibles,
        "degres": res["degres"],
        "regles_activees": [a for a in res["activations"] if a["force"] > 0],
        "courbe_agregee": courbe,
    }