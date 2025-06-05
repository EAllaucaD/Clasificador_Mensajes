# 🤖 CLASIFICACIÓN AUTOMATIZADA DE MENSAJES

Esta es una aplicación que usa ia para clasificar automáticamente mensajes escritos en texto en tres categorías:

**🛑 Urgente**, **⚠️ Moderado** y **✅ Normal**.

El usuario escribe un mensaje en una interfaz amigable desarrollada con Streamlit, que se comunica con un backend creado en FastAPI. Este backend utiliza la IA Gemini 1.5 Flash de Google para analizar y clasificar el mensaje, mostrando el resultado de forma visual para facilitar su comprensión. Ideal para priorizar comunicaciones de forma automática y eficiente.

---

## 🧰 TECNOLOGÍAS USADAS

| Herramienta            | Descripción                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| 🐍 **Python**          | Lenguaje de programación base del proyecto.                                |
| ⚡ **FastAPI**          | Framework web para crear el API REST.                                      |
| 🧠 **Gemini AI**        | Modelo de IA de Google para analizar y clasificar el contenido del mensaje.|
| 🌐 **Streamlit**       | Framework para la interfaz gráfica interactiva.                            |
| 🔐 **dotenv**           | Para cargar la API key de forma segura desde el archivo `.env`.            |
| 🔄 **CORS Middleware** | Para permitir la comunicación entre el backend y el frontend.               |
| 🌍 **Postman** | Para probar la API manualmente durante el desarrollo.                  |

---

## 🛠️ INSTALACIÓN Y USO

### 1. 📦 Clonar el repositorio

```bash
git clone https://github.com/EAllaucaD/Clasificador_Mensajes.git
cd Clasificador_Mensajes
```

### 2. 📦 Crear el entorno virtual (recomendado)

```bash
python -m venv venv
source venv/bin/activate
```

### 3. 📚 Instalar las dependencias
```bash
pip install -r requirements.txt
```

### 4. 🔐 Configurar tu archivo .env
En la raíz del proyecto, crea un archivo .env y añade tu API key de Gemini:

```bash
GEMINI_API_KEY=tu_clave_de_api
```

## ▶️EJECUCIÓN DE LA APP

### 1. Ejecutar el backend (FastAPI)

Desde la carpeta del backend, ir hasta el archivo main.py y ejecutar el comando:


```bash
uvicorn main:app --reload

```

### 2. Ejecutar el frontend (Streamlit)

En un nuevo terminal desde la carpeta del frontend, ir hasta el archivo app.py y ejecutar el comando:


```bash
streamlit run app.py
```
Esto abrirá una página en tu navegador como: http://localhost:8501

Con esto podrá usar la app y escribir su mensaje.

## ▶️VISUALIZACIÓN

![image](https://github.com/user-attachments/assets/7e67e195-9e7d-41f6-b135-d9c9d75a203e)

![image](https://github.com/user-attachments/assets/e72d8eff-2c6b-4a10-a284-ac5531af95b8)

