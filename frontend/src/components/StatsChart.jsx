import { Bar, BarChart, CartesianGrid, ResponsiveContainer, Tooltip, XAxis, YAxis } from "recharts";
import { VARIABLES } from "../constants";

export default function StatsChart({ stats }) {
  // Chaque statistique est ramenée en % de son domaine pour pouvoir les comparer
  const data = VARIABLES.map((v) => ({
    name: v.label,
    pourcentage: (stats[v.key] / v.max) * 100,
    valeur: stats[v.key],
  }));

  return (
    <div className="carte">
      <h2>Les 6 statistiques</h2>
      <p className="note">Chaque barre = la valeur en % du maximum de son domaine.</p>
      <div style={{ height: 300 }}>
        <ResponsiveContainer>
          <BarChart data={data} layout="vertical" margin={{ left: 10, right: 20 }}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis type="number" domain={[0, 100]} unit="%" />
            <YAxis type="category" dataKey="name" width={170} tick={{ fontSize: 12 }} />
            <Tooltip
              formatter={(value, name, item) => [
                `${item.payload.valeur} (${value.toFixed(0)} % du domaine)`,
                "Valeur",
              ]}
            />
            <Bar dataKey="pourcentage" fill="#3b82f6" radius={[0, 4, 4, 0]} />
          </BarChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
}