import { Area, AreaChart, CartesianGrid, ReferenceLine, ResponsiveContainer, Tooltip, XAxis, YAxis } from "recharts";

export default function AggregatedChart({ courbe, score }) {
  return (
    <div className="carte">
      <h2>Courbe agrégée et score</h2>
      <p className="note">La ligne verticale est le centroïde : le score final.</p>
      <div style={{ height: 300 }}>
        <ResponsiveContainer>
          <AreaChart data={courbe}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="x" type="number" domain={[0, 100]} ticks={[0, 20, 40, 60, 80, 100]} />
            <YAxis domain={[0, 1]} />
            <Tooltip formatter={(v) => v.toFixed(2)} labelFormatter={(x) => `Performance : ${x}`} />
            <Area type="monotone" dataKey="y" stroke="#6366f1" fill="#6366f1" fillOpacity={0.35} />
            <ReferenceLine
              x={score}
              stroke="#111827"
              strokeWidth={2}
              label={{ value: score.toFixed(1), position: "top" }}
            />
          </AreaChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
}