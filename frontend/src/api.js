const API_URL = "http://127.0.0.1:8000";

export async function evaluerJoueur(stats) {
  let reponse;
  try {
    reponse = await fetch(`${API_URL}/evaluate`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(stats),
    });
  } catch {
    throw new Error("Impossible de joindre le serveur. Le backend est-il lancé ?");
  }

  if (!reponse.ok) {
    const erreur = await reponse.json().catch(() => null);
    let message = "Erreur du serveur";
    if (erreur && typeof erreur.detail === "string") {
      message = erreur.detail;
    } else if (erreur && Array.isArray(erreur.detail)) {
      message = erreur.detail
        .map((e) => `${e.loc.slice(1).join(".")} : ${e.msg}`)
        .join(" | ");
    }
    throw new Error(message);
  }

  return reponse.json();
}