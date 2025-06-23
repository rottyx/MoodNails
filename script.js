let currentImageUrl = "";
let lastPrompt = "";

async function generate(forcedPrompt = null) {
  const inputField = document.getElementById("promptInput");
  const prompt = forcedPrompt || inputField.value.trim() || lastPrompt;
  const status = document.getElementById("status");
  const error = document.getElementById("error");
  const img = document.getElementById("resultImage");
  const actions = document.getElementById("actions");

  if (!prompt || prompt.length < 3) {
    error.textContent = "❌ Por favor, escribe un estado de ánimo válido.";
    return;
  }

  lastPrompt = prompt;
  inputField.value = forcedPrompt ? "" : prompt;

  status.textContent = "⏳ Generando imagen...";
  error.textContent = "";
  img.src = "";
  actions.style.display = "none";

  try {
    const res = await fetch("http://127.0.0.1:8000/generate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ prompt }),
    });

    const data = await res.json();
    if (!res.ok) throw new Error(data.detail || "Error desconocido");

    currentImageUrl = data.image_url;
    status.textContent = "✅ Imagen generada:";
    img.src = currentImageUrl;
    actions.style.display = "block";
  } catch (err) {
    status.textContent = "";
    error.textContent = "❌ " + err.message;
  }
}

function generateRandom() {
  const randomMoods = [
    "alegre", "misteriosa", "romántica", "verano",
    "salvaje y japonesa", "triste y nocturna", "futurista con tonos grises",
    "relajada con tonos pastel", "divertida", "elegante con dorado",
    "minimalista y nórdica", "inspirada en un atardecer",
    "brillante como neón", "vintage de los 80", "tropical y playera",
    "moderna y elegante", "suave como algodón", "energética y deportiva",
    "serena como un bosque", "lujosa con efecto mármol", "otoñal en tonos tierra",
    "primaveral", "soñadora", "abstracta y creativa"
  ];

  const randomMood = randomMoods[Math.floor(Math.random() * randomMoods.length)];
  lastPrompt = randomMood;
  generate(randomMood);
}
