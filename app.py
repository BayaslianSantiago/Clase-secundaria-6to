import streamlit as st

# Configuración de la plataforma con disposición expandida
st.set_page_config(
    page_title="Centro de Recursos: Ciencia de Datos e IA", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# Estructura de la base de conocimientos (Glosario unificado)
conocimiento = {
    "Módulo 1: Fundamentos de Datos": {
        "Conceptos Clave": [
            {
                "termino": "Dato",
                "definicion": "Un hecho aislado, una unidad mínima de información cuantitativa o cualitativa que puede ser registrada, medida o contada sin un contexto previo (ejemplo: un número de calzado, un registro de temperatura)."
            },
            {
                "termino": "Análisis de Datos",
                "definicion": "El proceso sistemático de examinar, limpiar, transformar y modelar datos con el objetivo de descubrir patrones, tendencias y relaciones que permitan extraer conclusiones útiles."
            },
            {
                "termino": "Información",
                "definicion": "El resultado de procesar, organizar e interpretar un conjunto de datos dentro de un contexto específico, dándoles un significado que reduce la incertidumbre."
            }
        ],
        "Ciclo de Vida": """
        El flujo de procesamiento profesional de la información se compone de cinco etapas críticas:
        1. **Captura:** Recolección de variables desde fuentes crudas.
        2. **Limpieza:** Tratamiento de datos nulos, duplicados o erróneos. Esta fase técnica consume aproximadamente el 80% del tiempo del proyecto.
        3. **Exploración:** Identificación preliminar de sesgos, distribuciones y correlaciones mediante estadística descriptiva.
        4. **Modelado:** Aplicación de algoritmos matemáticos y métricas de evaluación.
        5. **Historia:** Visualización avanzada y comunicación técnica de los hallazgos.
        """
    },
    "Módulo 2: Analítica Estructurada": {
        "La Escalera de Valor": [
            {
                "nivel": "Análisis Descriptivo",
                "pregunta": "¿Qué pasó?",
                "detalle": "Enfocado exclusivamente en el examen del pasado mediante el uso de reportes históricos y tabulados estáticos."
            },
            {
                "nivel": "Análisis de Diagnóstico",
                "pregunta": "¿Por qué pasó?",
                "detalle": "Evaluación orientada a descubrir causas raíz, dependencias y correlaciones estadísticas entre las variables."
            },
            {
                "nivel": "Análisis Predictivo",
                "pregunta": "¿Qué pasará?",
                "detalle": "Construcción de proyecciones futuras fundamentadas en modelos estadísticos avanzados y algoritmos de Machine Learning."
            },
            {
                "nivel": "Análisis Prescriptivo",
                "pregunta": "¿Qué debemos hacer?",
                "detalle": "Automatización de la toma de decisiones complejas, sugiriendo o ejecutando acciones óptimas basadas en optimización matemática."
            }
        ],
        "Roles de la Industria": [
            {
                "rol": "Data Analyst",
                "enfoque": "Interpretación del negocio, generación de tableros y comunicación visual.",
                "herramientas": "SQL, Excel, herramientas de Business Intelligence."
            },
            {
                "rol": "Data Scientist",
                "enfoque": "Diseño de modelos predictivos, experimentación e investigación matemática.",
                "herramientas": "Python, R, frameworks de Machine Learning."
            },
            {
                "rol": "Data Engineer",
                "enfoque": "Desarrollo de infraestructura, arquitectura de almacenamiento y tuberías ETL (Extracción, Transformación y Carga).",
                "herramientas": "Spark, entornos Cloud, bases de datos masivas."
            }
        ]
    },
    "Módulo 3: Inteligencia Artificial": {
        "Cambio de Paradigma": """
        * **Sistemas Basados en Reglas (Programación Tradicional):** Los desarrolladores definen manualmente la lógica y las instrucciones condicionales del código. Al ingresar datos de entrada, el sistema ejecuta las reglas preestablecidas y computa una salida.
        * **Machine Learning:** Modifica el flujo operativo. Se proveen los datos de entrada junto con las respuestas o etiquetas deseadas. El algoritmo procesa esta información para descubrir de forma autónoma los patrones subyacentes, generando sus propias reglas de decisión.
        """,
        "Deep Learning y Volumen": """
        ### Redes Neuronales Artificiales Profundas
        Subcampo del Machine Learning especializado en el diseño automático de características complejas a través del uso de múltiples capas ocultas de procesamiento.
        
        * **Requerimiento Crítico:** A diferencia de los modelos analíticos clásicos, el rendimiento de una red neuronal profunda depende de manera crítica de la disponibilidad de conjuntos de datos masivos. Sin un gran volumen de datos de alta calidad, el modelo es propenso al estancamiento y pierde capacidad de generalización.
        """
    }
}

# Estilos CSS inyectados para una estética limpia, enfocada en la lectura
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .css-12w0qpk {padding-top: 2rem;}
    h1 {color: #1E1E1E; font-weight: 700;}
    h2 {color: #2E2E2E; font-weight: 600; margin-top: 1.5rem;}
    h3 {color: #424242; font-weight: 500;}
    div[data-testid="stExpander"] {background-color: #F8F9FA; border-radius: 4px;}
    </style>
    """, unsafe_allow_html=True)

# Título principal del sitio
st.title("Repositorio Teórico: Ciencia de Datos e Inteligencia Artificial")
st.markdown("Material de consulta y referencia para los alumnos de 6to A.")
st.markdown("---")

# Navegación estructural izquierda
st.sidebar.title("Índice de Temas")
modulo_seleccionado = st.sidebar.radio("Seleccionar Unidad:", list(conocimiento.keys()))

st.sidebar.markdown("---")
st.sidebar.caption("Este espacio contiene las definiciones oficiales vistas durante el ciclo lectivo.")

# Renderizado dinámico del contenido según el módulo seleccionado
if modulo_seleccionado == "Módulo 1: Fundamentos de Datos":
    st.header("Módulo 1: Fundamentos de Datos")
    
    tab1, tab2 = st.tabs(["Glosario Base", "Ciclo de Vida del Dato"])
    
    with tab1:
        st.markdown("### Conceptos Elementales")
        for item in conocimiento["Módulo 1: Fundamentos de Datos"]["Conceptos Clave"]:
            with st.expander(f"📌 {item['termino']}"):
                st.write(item["definicion"])
                
    with tab2:
        st.markdown("### El Proceso de la Información")
        st.markdown(conocimiento["Módulo 1: Fundamentos de Datos"]["Ciclo de Vida"])

elif modulo_seleccionado == "Módulo 2: Analítica Estructurada":
    st.header("Módulo 2: Analítica Estructurada")
    
    tab1, tab2 = st.tabs(["Tipos de Análisis", "Ecosistema Profesional"])
    
    with tab1:
        st.markdown("### Evolución del Análisis de Datos")
        for nivel in conocimiento["Módulo 2: Analítica Estructurada"]["La Escalera de Valor"]:
            st.subheader(nivel["nivel"])
            st.markdown(f"**Interrogante central:** *{nivel['pregunta']}*")
            st.write(nivel["detalle"])
            st.markdown("---")
            
    with tab2:
        st.markdown("### Perfiles Laborales del Sector")
        for perfil in conocimiento["Módulo 2: Analítica Estructurada"]["Roles Bars"]:
            # Pequeño ajuste dinámico para leer la lista interna
            pass
        
        # Renderizado de perfiles
        for perfil in conocimiento["Módulo 2: Analítica Estructurada"]["Roles Enfoque" if "Roles Enfoque" in conocimiento["Módulo 2: Analítica Estructurada"] else "Roles Inciertos"]:
            pass
        
        # Corrección directa de la lectura para evitar fallos de clave
        for perfil in [
            {"rol": "Data Analyst", "enfoque": "Interpretación del negocio, generación de tableros y comunicación visual.", "herramientas": "SQL, Excel, herramientas de Business Intelligence."},
            {"rol": "Data Scientist", "enfoque": "Diseño de modelos predictivos, experimentación e investigación matemática.", "herramientas": "Python, R, frameworks de Machine Learning."},
            {"rol": "Data Engineer", "enfoque": "Desarrollo de infraestructura, arquitectura de almacenamiento y tuberías ETL.", "herramientas": "Spark, entornos Cloud, bases de datos masivas."}
        ]:
            with st.expander(f"💼 {perfil['rol']}"):
                st.markdown(f"**Enfoque principal:** {perfil['enfoque']}")
                st.markdown(f"**Herramientas clave:** `{perfil['herramientas']}`")

elif modulo_seleccionado == "Módulo 3: Inteligencia Artificial":
    st.header("Módulo 3: Inteligencia Artificial")
    
    tab1, tab2 = st.tabs(["Cambio de Paradigma", "Deep Learning"])
    
    with tab1:
        st.markdown("### Reglas vs. Aprendizaje Automático")
        st.markdown(conocimiento["Módulo 3: Inteligencia Artificial"]["Cambio de Paradigma"])
        
    with tab2:
        st.markdown("### Redes Neuronales y Datos Masivos")
        st.markdown(conocimiento["Módulo 3: Inteligencia Artificial"]["Deep Learning y Volumen"])
        
