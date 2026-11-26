import { Bar, BarChart, CartesianGrid, Legend, ResponsiveContainer, Tooltip, XAxis, YAxis } from "recharts";
import { VARIABLES } from "../constants";

export default function MembershipChart({ degres }) {
  const data = VARIABLES.map((v) => ({
    name: v.court,
    Faible: degres[v.key].faible,
    Moyen: degres[v.key].moyen,
    Élevé: degres[v.key].eleve,
  }));

  return (
    <div className="carte">
      <h2>Degrés d'appartenance</h2>
      <p className="note">Pour chaque statistique : à quel degré (0 à 1) elle est faible, moyenne ou élevée.</p>
      <div style={{ height: 320 }}>
        <ResponsiveContainer>
          <BarChart data={data}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="name" interval={0} tick={{ fontSize: 11 }} />
            <YAxis domain={[0, 1]} />
            <Tooltip formatter={(v) => v.toFixed(2)} />
            <Legend />
            <Bar dataKey="Faible" fill="#ef4444" />
            <Bar dataKey="Moyen" fill="#f59e0b" />
            <Bar dataKey="Élevé" fill="#22c55e" />
          </BarChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
}