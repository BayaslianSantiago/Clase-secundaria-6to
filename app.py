import streamlit as st

# Configuración de la página (Ocultamos el panel lateral por defecto)
st.set_page_config(page_title="Repaso de Datos e IA", layout="wide", initial_sidebar_state="collapsed")

# Estructura de las diapositivas
slides = [
    {
        "title": "1. La Materia Prima: El Origen de Todo",
        "content": """
        ### ¿Qué es un dato?
        Un dato es un hecho aislado, cualquier información que podemos registrar, medir o contar (ej: una edad, temperatura, horas de uso de una app).
        
        *Son la base de todo análisis. Sin ellos, no podemos descubrir patrones ni tomar decisiones informadas.*
        """
    },
    {
        "title": "2. El Trabajo Sucio: El Ciclo de Vida del Dato",
        "content": """
        ### Garbage In, Garbage Out
        El proceso analítico no es mágico, requiere trabajo estructural:
        1. **Captura:** Recolección desde fuentes crudas.
        2. **Limpieza:** Tratamiento de nulos y duplicados (¡Representa el **80%** del trabajo de un analista!).
        3. **Exploración:** Identificación de tendencias iniciales.
        4. **Modelado:** Aplicación de algoritmos.
        5. **Historia:** Visualización y comunicación.
        
        > Si alimentamos un sistema con datos basura, las decisiones y resultados serán basura.
        """
    },
    {
        "title": "3. La Escalera del Valor: Los 4 Niveles de Análisis",
        "content": """
        A medida que aumenta la complejidad analítica, el valor estratégico para el negocio crece exponencialmente:
        
        * **Descriptivo (25% Valor):** ¿Qué pasó? *(Enfocado en el pasado, ej: reportes históricos).*
        * **Diagnóstico (45% Valor):** ¿Por qué pasó? *(Buscando causas raíz).*
        * **Predictivo (75% Valor):** ¿Qué va a pasar? *(Modelos estadísticos y Machine Learning).*
        * **Prescriptivo (95% Valor):** ¿Qué hacer? *(Recomendaciones automáticas de acción, como hace Netflix o Instagram).*
        """
    },
    {
        "title": "4. El Cambio de Paradigma: Reglas vs. Patrones",
        "content": """
        ### Programación Tradicional vs. Machine Learning
        
        * **Sistemas basados en reglas (Tradicional):** Diseño manual de reglas estáticas. Escribimos el código, pasamos los datos y obtenemos el resultado.
        * **Técnicas de Machine Learning:** Le damos a la máquina los datos de entrada y las respuestas esperadas (características). El sistema aprende a tomar la decisión y **descubre las reglas** por su cuenta.
        * **Deep Learning:** Diseño automático de características complejas usando capas adicionales (redes neuronales).
        """
    },
    {
        "title": "5. El Entrenamiento: Deep Learning y Práctica",
        "content": """
        ### La importancia del volumen
        Para que los algoritmos de Deep Learning funcionen adecuadamente y logren resolver problemas complejos, requieren un **conjunto de datos grandes**.
        
        *Es exactamente igual que el entrenamiento físico: no alcanza con ir una sola vez al gimnasio o levantar poco peso; el modelo necesita volumen, repetición y datos de alta calidad para no estancarse.*
        
        ---
        **🚀 Actividad Práctica:**
        1. Elegir un tipo de modelo en Teachable Machine.
        2. Diseñar un conjunto de datos de entrenamiento (mínimo dos clases).
        3. Entrenar el modelo y realizar pruebas.
        """
    }
]

# Inicializar el estado de la sesión para el índice de la diapositiva
if 'slide_index' not in st.session_state:
    st.session_state.slide_index = 0

# Funciones de navegación
def next_slide():
    if st.session_state.slide_index < len(slides) - 1:
        st.session_state.slide_index += 1

def prev_slide():
    if st.session_state.slide_index > 0:
        st.session_state.slide_index -= 1

# Ocultar elementos de la interfaz de Streamlit para maximizar el efecto presentación
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    [data-testid="collapsedControl"] {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# Renderizar la diapositiva actual
current_slide = slides[st.session_state.slide_index]

st.title(current_slide["title"])
st.markdown("---")
st.markdown(current_slide["content"])
st.markdown("---")

# Controles de navegación estructurados en columnas
col1, col2, col3 = st.columns([1, 8, 1])

with col1:
    if st.session_state.slide_index > 0:
        st.button("⬅️ Anterior", on_click=prev_slide, use_container_width=True)

with col2:
    # Barra de progreso visual
    progress = (st.session_state.slide_index + 1) / len(slides)
    st.progress(progress)
    st.markdown(f"<div style='text-align: center; color: gray;'>Diapositiva {st.session_state.slide_index + 1} de {len(slides)}</div>", unsafe_allow_html=True)

with col3:
    if st.session_state.slide_index < len(slides) - 1:
        st.button("Siguiente ➡️", on_click=next_slide, use_container_width=True)
        
