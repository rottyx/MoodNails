# 💅 MoodNails

MoodNails es una aplicación que genera ideas de diseño de uñas basadas en tu estado de ánimo usando la API de OpenAI (DALL·E 3).

## 🚀 ¿Cómo funciona?

1. Escribe cómo te sientes (ej. "romántica", "atrevida", "relajada").
2. Haz clic en "Generar diseño".
3. La app generará una imagen realista con un estilo de uñas inspirado en tu mood.

## 🧠 Tecnologías usadas

- ⚡ FastAPI (backend)
- 🎨 HTML/CSS/JavaScript (frontend)
- 🤖 OpenAI API (modelo DALL·E 3)
- 🌿 python-dotenv (para gestionar variables de entorno)

## 📦 Instalación

### 1. Clona el repositorio

```bash
git clone https://github.com/tu-usuario/MoodNails.git
cd MoodNails
```

### 2. Crea tu entorno `.env`

Crea un archivo `.env` basado en `.env.example` con tu clave de API de OpenAI:

```env
OPENAI_API_KEY=sk-xxxxx
```

### 3. Instala dependencias del backend

```bash
cd backend
pip install -r requirements.txt
```

### 4. Lanza el backend

```bash
uvicorn main:app --reload
```

### 5. Lanza el frontend

Abre el archivo `index.html` directamente en tu navegador.

---

## 🔐 Seguridad

- Tu clave API se mantiene segura en el backend.
- Asegúrate de no subir `.env` al repositorio gracias al `.gitignore`.

## 🧪 Prueba rápida

- Introduce un mood (ej: "alegre", "pastel elegante").
- Haz clic en “Generar diseño”.
- Espera unos segundos y aparecerá la imagen.

---

## 🧑‍🎨 Autor

Hecho con 💅 por [rottyx]  
Licencia MIT
