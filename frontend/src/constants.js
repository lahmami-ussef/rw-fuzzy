// Les 6 variables : les domaines doivent rester identiques à ceux du backend.
export const VARIABLES = [
  { key: "goals_per_90", label: "Buts / 90", court: "Buts", min: 0, max: 1 },
  { key: "assists_per_90", label: "Passes décisives / 90", court: "Passes déc.", min: 0, max: 1 },
  { key: "dribbling_success", label: "Dribbles réussis (%)", court: "Dribbles", min: 0, max: 100 },
  { key: "key_passes_per_90", label: "Passes clés / 90", court: "Passes clés", min: 0, max: 5 },
  { key: "crossing_accuracy", label: "Précision des centres (%)", court: "Centres", min: 0, max: 100 },
  { key: "progressive_carries_per_90", label: "Courses progressives / 90", court: "Courses prog.", min: 0, max: 10 },
];

// Joueurs fictifs pour tester rapidement
export const EXEMPLES = [
  {
    nom: "Joueur test",
    valeurs: {
      goals_per_90: 0.5,
      assists_per_90: 0.3,
      dribbling_success: 72,
      key_passes_per_90: 2.5,
      crossing_accuracy: 60,
      progressive_carries_per_90: 6,
    },
  },
  {
    nom: "Joueur faible",
    valeurs: {
      goals_per_90: 0.05,
      assists_per_90: 0.03,
      dribbling_success: 30,
      key_passes_per_90: 0.5,
      crossing_accuracy: 20,
      progressive_carries_per_90: 1,
    },
  },
  {
    nom: "Joueur élite",
    valeurs: {
      goals_per_90: 0.8,
      assists_per_90: 0.45,
      dribbling_success: 85,
      key_passes_per_90: 4,
      crossing_accuracy: 75,
      progressive_carries_per_90: 8.5,
    },
  },
];