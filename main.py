from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
import os
import openai

load_dotenv()

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PromptRequest(BaseModel):
    prompt: str

# 🔒 Función que reescribe el prompt para evitar bloqueos
def build_safe_prompt(mood: str) -> str:
    mood = mood.lower().strip()

    # Lista de palabras potencialmente problemáticas
    blocked_words = [
        "sangre", "oscuridad", "oscuro", "herida", "violencia", "triste",
        "mujer", "persona", "cara", "piel", "nudillos", "dolor", "sexo", "pecho", "desnudo"
    ]

    # Reemplazar o suavizar palabras
    for word in blocked_words:
        if word in mood:
            mood = mood.replace(word, "poetic")

    return (
        f"High-quality editorial photo of a single feminine hand, shown fully with exactly five well-proportioned fingers. "
        f"The nails display an abstract, artistic, and non-figurative design inspired by the mood: '{mood}'. "
        "The thumb is clearly visible and naturally aligned. "
        "The hand is photographed in a centered close-up, softly lit, against a plain white background. "
        "Skin appears healthy and realistic. No additional elements, text, logos, accessories, or figurative art should appear."
    )

@app.post("/generate")
async def generate_image(data: PromptRequest):
    if not data.prompt or len(data.prompt.strip()) < 5:
        raise HTTPException(status_code=400, detail="El prompt debe ser más descriptivo.")

    prompt = build_safe_prompt(data.prompt)
    print("📝 Prompt generado:\n", prompt)  # 🔍 Mostrar prompt en consola

    try:
        print("🔵 Generando imagen con OpenAI (model: dall-e-3)")
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1
        )
        return {"image_url": response.data[0].url}

    except openai.BadRequestError:
        raise HTTPException(status_code=400, detail="El prompt fue rechazado por la API de OpenAI.")
    except openai.APIError:
        raise HTTPException(status_code=500, detail="Error en la API de OpenAI.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
