import { useState } from "react";
import "./App.css";
import { evaluerJoueur } from "./api";
import StatsForm from "./components/StatsForm";
import ResultCard from "./components/ResultCard";
import StatsChart from "./components/StatsChart";
import MembershipChart from "./components/MembershipChart";
import AggregatedChart from "./components/AggregatedChart";
import RulesTable from "./components/RulesTable";

export default function App() {
  const [stats, setStats] = useState(null);
  const [resultat, setResultat] = useState(null);
  const [erreur, setErreur] = useState("");
  const [chargement, setChargement] = useState(false);

  async function evaluer(statsSaisies) {
    setChargement(true);
    setErreur("");
    try {
      const res = await evaluerJoueur(statsSaisies);
      setStats(statsSaisies);
      setResultat(res);
    } catch (e) {
      setResultat(null);
      setErreur(e.message);
    } finally {
      setChargement(false);
    }
  }

  return (
    <div className="page">
      <header>
        <h1>Évaluation d'un ailier droit</h1>
        <p>Système d'inférence floue de Mamdani (centroïde)</p>
      </header>

      <div className="grille">
        <div>
          <StatsForm onSubmit={evaluer} chargement={chargement} />
        </div>

        <div className="resultats">
          {erreur && <div className="carte erreur">Erreur : {erreur}</div>}

          {!resultat && !erreur && (
            <div className="carte vide">
              Saisis les statistiques puis clique sur « Évaluer le joueur ».
            </div>
          )}

          {resultat && (
            <>
              <ResultCard resultat={resultat} />
              <StatsChart stats={stats} />
              <MembershipChart degres={resultat.degres} />
              <AggregatedChart courbe={resultat.courbe_agregee} score={resultat.score} />
              <RulesTable regles={resultat.regles_activees} />
            </>
          )}
        </div>
      </div>
    </div>
  );
}