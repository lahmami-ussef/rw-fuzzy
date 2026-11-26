import { useState } from "react";
import { VARIABLES, EXEMPLES } from "../constants";

function versTexte(valeurs) {
  return Object.fromEntries(Object.entries(valeurs).map(([k, v]) => [k, String(v)]));
}

export default function StatsForm({ onSubmit, chargement }) {
  const [valeurs, setValeurs] = useState(versTexte(EXEMPLES[0].valeurs));
  const [erreurs, setErreurs] = useState({});

  function changer(cle, texte) {
    setValeurs({ ...valeurs, [cle]: texte });
  }

  function soumettre(e) {
    e.preventDefault();
    const nouvellesErreurs = {};
    const stats = {};

    for (const v of VARIABLES) {
      const texte = valeurs[v.key].trim().replace(",", ".");
      const n = Number(texte);
      if (texte === "" || Number.isNaN(n)) {
        nouvellesErreurs[v.key] = "Nombre requis";
      } else if (n < v.min || n > v.max) {
        nouvellesErreurs[v.key] = `Doit être entre ${v.min} et ${v.max}`;
      } else {
        stats[v.key] = n;
      }
    }

    setErreurs(nouvellesErreurs);
    if (Object.keys(nouvellesErreurs).length === 0) onSubmit(stats);
  }

  return (
    <form onSubmit={soumettre} className="carte">
      <h2>Statistiques du joueur</h2>

      <div className="exemples">
        {EXEMPLES.map((ex) => (
          <button
            type="button"
            key={ex.nom}
            className="secondaire"
            onClick={() => {
              setValeurs(versTexte(ex.valeurs));
              setErreurs({});
            }}
          >
            {ex.nom}
          </button>
        ))}
      </div>

      {VARIABLES.map((v) => (
        <label key={v.key} className="champ">
          <span>
            {v.label} <small>({v.min} à {v.max})</small>
          </span>
          <input
            type="text"
            inputMode="decimal"
            value={valeurs[v.key]}
            onChange={(e) => changer(v.key, e.target.value)}
            className={erreurs[v.key] ? "invalide" : ""}
          />
          {erreurs[v.key] && <em className="erreur-champ">{erreurs[v.key]}</em>}
        </label>
      ))}

      <button type="submit" disabled={chargement}>
        {chargement ? "Évaluation..." : "Évaluer le joueur"}
      </button>
    </form>
  );
}