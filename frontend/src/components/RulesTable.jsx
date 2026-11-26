export default function RulesTable({ regles }) {
  const triees = [...regles].sort((a, b) => b.force - a.force);

  return (
    <div className="carte">
      <h2>Règles activées ({regles.length})</h2>
      <table>
        <thead>
          <tr>
            <th>Règle</th>
            <th>Groupe</th>
            <th>Conclusion</th>
            <th>Force</th>
          </tr>
        </thead>
        <tbody>
          {triees.map((r) => (
            <tr key={r.id}>
              <td>{r.id}</td>
              <td>{r.groupe}</td>
              <td>{r.alors}</td>
              <td>
                <div className="barre-fond">
                  <div className="barre" style={{ width: `${r.force * 100}%` }} />
                </div>
                {r.force.toFixed(3)}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}