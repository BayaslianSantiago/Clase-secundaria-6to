import streamlit as st

# Configuración de la página (estilo limpio y amplio)
st.set_page_config(page_title="Repaso de Datos e IA - 6to A", layout="wide", page_icon="📊")

# Diccionario con el contenido estructurado de las "diapositivas"
slides = {
    "1. La Materia Prima": {
        "title": "Datos: El Origen de Todo",
        "content": """
        ### ¿Qué es un dato?
        Un dato es un hecho aislado, cualquier información que podemos registrar, medir o contar (ej: una edad, temperatura, horas de uso de una app).
        
        *Son la base de todo análisis. Sin ellos, no podemos descubrir patrones.*
        """,
        "image_tag": ""
    },
    "2. El Trabajo Sucio": {
        "title": "El Ciclo de Vida del Dato",
        "content": """
        ### Garbage In, Garbage Out
        El proceso analítico no es mágico, requiere trabajo estructural:
        1. **Captura**
        2. **Limpieza** (¡Representa el 80% del trabajo de un analista!)
        3. **Exploración**
        4. **Modelado**
        5. **Historia (Storytelling)**
        
        > Si alimentamos un sistema con datos basura, las decisiones y resultados serán basura.
        """
    },
    "3. La Escalera del Valor": {
        "title": "Los 4 Niveles de Análisis",
        "content": """
        A medida que subimos en la escalera, aumenta la complejidad técnica y el valor para el negocio:
        
        * **Descriptivo:** ¿Qué pasó? *(Ej: Contar cuántos alumnos usan TikTok).*
        * **Diagnóstico:** ¿Por qué pasó? *(Ej: Cruzar uso de redes con horas de sueño).*
        * **Predictivo:** ¿Qué va a pasar? *(Anticipar tendencias usando estadística y Machine Learning).*
        * **Prescriptivo:** ¿Qué deberíamos hacer? *(Sistemas que ejecutan acciones automáticas, como las recomendaciones de Netflix).*
        """,
        "image_tag": "[attachment_0](attachment)"
    },
    "4. El Cambio de Paradigma": {
        "title": "Reglas vs. Patrones (IA)",
        "content": """
        ### Programación Tradicional vs. Machine Learning
        
        * **Programación Tradicional:** Nosotros escribimos las reglas (el código) y le pasamos los datos. La máquina procesa y nos da las respuestas.
        * **Machine Learning:** Nosotros le damos los datos y las respuestas esperadas. La máquina procesa y **descubre las reglas** (patrones).
        """,
        "image_tag": ""
    },
    "5. El Entrenamiento": {
        "title": "Deep Learning y Práctica",
        "content": """
        ### La importancia del volumen en las Redes Neuronales
        Para que los algoritmos de Deep Learning resuelvan problemas complejos (como visión computacional o reconocimiento de voz), necesitan un volumen masivo de datos.
        
        *Es como el entrenamiento físico: no alcanza con ir una sola vez al gimnasio o levantar poco peso; el modelo necesita volumen, repetición y datos de alta calidad para no estancarse y aprender a generalizar.*
        
        ---
        **🚀 Próximo paso práctico:** Teachable Machine (Armar clases, entrenar modelo y probar resultados).
        """
    }
}

# Lógica de navegación en la barra lateral
st.sidebar.title("Navegación")
st.sidebar.markdown("---")
# Usamos un radio button para simular el paso de diapositivas
selection = st.sidebar.radio("Ir a la sección:", list(slides.keys()))

st.sidebar.markdown("---")
st.sidebar.info("💡 **Tip:** Usá las flechas del teclado en este menú para cambiar de tema rápidamente.")

# Renderizar el contenido de la diapositiva seleccionada
slide = slides[selection]
st.title(slide["title"])
st.markdown("---")
st.markdown(slide["content"])

# Mostrar los tags de imágenes para que puedas agregar las tuyas luego si querés
if "image_tag" in slide:
    st.caption(f"*(Acá podrías incluir un gráfico ilustrativo: {slide['image_tag']})*")
