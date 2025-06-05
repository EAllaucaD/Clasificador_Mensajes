#Importaciones necesarias

import streamlit as st
import requests

# Configuración de la página
st.set_page_config(page_title="Clasificador de Mensajes ", page_icon="🤖", layout="centered")

# Título y descripción
st.title("🧠 Clasificador Automático de Mensajes ")
st.markdown(
    """
    Esta aplicación te permite **clasificar mensajes de texto** en tres categorías:
    - 🛑 **Urgente**  
    - ⚠️ **Moderado**  
    - ✅ **Normal**  
    """
)

st.markdown("---")

# Input de usuario
mensaje = st.text_area("**ESCRIBE TU MENSAJE AQUÍ:**", height=150)


# Función para mostrar resultado con colores y emojis
def mostrar_resultado(categoria: str):
    if categoria == "Urgente":
        st.markdown(f'<h2 style="color:#e03c3c;">🛑 Resultado: {categoria}</h2>', unsafe_allow_html=True)
        st.write("Este mensaje requiere atención inmediata.")
    elif categoria == "Moderado":
        st.markdown(f'<h2 style="color:#f1a600;">⚠️ Resultado: {categoria}</h2>', unsafe_allow_html=True)
        st.write("Este mensaje tiene prioridad media, puedes atenderlo pronto.")
    else:  # Normal
        st.markdown(f'<h2 style="color:#3cb371;">✅ Resultado: {categoria}</h2>', unsafe_allow_html=True)
        st.write("Este mensaje no es urgente y puede esperar.")

# Botón para clasificar
if st.button("🔍 Clasificar mensaje"):
    if not mensaje.strip():
        st.warning("⚠️ Por favor, escribe un mensaje para clasificar.")
    else:
        with st.spinner("🧠 Clasificando tu mensaje..."):
            try:
                response = requests.post("http://localhost:8000/clasificar", json={"content": mensaje})
                if response.status_code == 200:
                    categoria = response.json().get("category", "No definido")
                    mostrar_resultado(categoria)
                else:
                    st.error("Error al comunicarse con el servidor. Intenta de nuevo más tarde.")
            except requests.exceptions.RequestException:
                st.error("No se pudo conectar con el servidor backend. ¿Está corriendo la API?")
