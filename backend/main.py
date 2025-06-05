#Importaciones necesarias
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from google import generativeai as genai
import os
from dotenv import load_dotenv

# Cargar .env desde la raíz del proyecto
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dotenv_path = os.path.join(base_dir, '.env')
load_dotenv(dotenv_path)


#Configuración de Gemini API con la clave secreta

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")


#Instancia de la aplicación FastAPI

app = FastAPI()

#Configuración de CORS para permitir comunicación con el frontend

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

class Message(BaseModel):
    content: str


#Clasificación de los mensajes

@app.post("/clasificar")
def clasificar_mensaje(msg: Message):
    prompt = (
        "Clasifica este mensaje como Urgente, Moderado o Normal, además de un descripción corta del porque. "
        "Solo responde una palabra:\n\n"
        f"Mensaje: {msg.content}"
    )

    try:
        respuesta = model.generate_content(prompt)
        categoria = respuesta.text.strip().capitalize()
        if categoria not in ["Urgente", "Moderado", "Normal"]:
            return {"category": "No identificado"}
        return {"category": categoria}
    except Exception as e:
        return {"category": f"Error: {str(e)}"}
