export default function ResultCard({ resultat }) {
  const { score, categorie, points_forts, points_faibles } = resultat;

  return (
    <div className="carte">
      <h2>Résultat</h2>

      <div className="score-bloc">
        <div className="score">{score.toFixed(2)}</div>
        <div className="sur-cent">/ 100</div>
        <span className={`badge ${categorie.toLowerCase()}`}>{categorie}</span>
      </div>

      <div className="deux-colonnes">
        <div>
          <h3>Points forts</h3>
          {points_forts.length === 0 ? (
            <p className="vide">Aucun point fort marqué</p>
          ) : (
            <ul className="liste fort">
              {points_forts.map((p) => (
                <li key={p}>{p}</li>
              ))}
            </ul>
          )}
        </div>
        <div>
          <h3>Points faibles</h3>
          {points_faibles.length === 0 ? (
            <p className="vide">Aucun point faible marqué</p>
          ) : (
            <ul className="liste faible">
              {points_faibles.map((p) => (
                <li key={p}>{p}</li>
              ))}
            </ul>
          )}
        </div>
      </div>

      <p className="note">
        Avec la défuzzification par centroïde, le score reste entre environ 13 et 87.
      </p>
    </div>
  );
}