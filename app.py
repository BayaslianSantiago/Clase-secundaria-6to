import streamlit as st

# Configuracion de la pagina con panel expandido por defecto
st.set_page_config(
    page_title="Centro de Recursos: Ciencia de Datos e IA", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# Inyeccion de CSS para forzar un tema oscuro minimalista y consistente
st.markdown("""
    <style>
    /* Fondo principal y color de texto */
    .stApp {
        background-color: #0a0a0a;
        color: #e5e5e5;
    }
    
    /* Barra lateral */
    section[data-testid="stSidebar"] {
        background-color: #111111;
        border-right: 1px solid #222222;
    }
    
    /* Titulos y Encabezados */
    h1, h2, h3, h4 {
        color: #ffffff !important;
        font-weight: 600;
    }
    
    /* Separadores */
    hr {
        border-color: #222222 !important;
    }
    
    /* Estilo para los bloques desplegables (Expanders) */
    div[data-testid="stExpander"] {
        background-color: #141414 !important;
        border: 1px solid #262626 !important;
        border-radius: 4px !important;
    }
    
    /* Modificacion de pestanas (Tabs) para integracion en tema oscuro */
    button[data-baseweb="tab"] {
        color: #888888 !important;
        background-color: transparent !important;
    }
    button[data-baseweb="tab"][aria-selected="true"] {
        color: #ffffff !important;
        border-bottom-color: #ffffff !important;
    }
    
    /* Ocultar elementos nativos de la interfaz de Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# Base de datos de conocimiento estructurada
conocimiento = {
    "Modulo 1: Fundamentos de Datos": {
        "Glosario": [
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
        "Proceso": """
        El flujo de procesamiento profesional de la información se compone de cinco etapas críticas:
        
        1. **Captura:** Recolección de variables desde fuentes crudas.
        2. **Limpieza:** Tratamiento de datos nulos, duplicados o erróneos. Esta fase técnica consume aproximadamente el 80% del tiempo de un proyecto de datos.
        3. **Exploración:** Identificación preliminar de sesgos, distribuciones y correlaciones mediante estadística descriptiva.
        4. **Modelado:** Aplicación de algoritmos matemáticos y métricas de evaluación.
        5. **Historia:** Visualización avanzada y comunicación técnica de los hallazgos.
        
        *Principio rector:* Garbage In, Garbage Out. Si alimentamos un sistema con datos basura, las decisiones y los resultados serán basura.
        """,
        "Codigo_Pandas": """import pandas as pd
import numpy as np

# 1. Simulamos un dataset "sucio" (con valores nulos y registros duplicados)
datos_crudos = {
    'Alumno': ['Juan', 'Ana', 'Pedro', 'Ana', 'Sofia', np.nan],
    'Edad': [17, 18, np.nan, 18, 17, 18],
    'Horas_Celular': [5, 3, 6, 3, np.nan, 4]
}

# Creamos el DataFrame
df = pd.DataFrame(datos_crudos)

# ==========================================
# 2. LIMPIEZA DE DATOS (El "Trabajo Sucio")
# ==========================================

# A. Eliminar filas duplicadas (El registro de 'Ana' está repetido exactamente igual)
df_limpio = df.drop_duplicates()

# B. Tratar valores nulos (NaN - Not a Number)
# Rellenar nombres faltantes con una etiqueta estándar
df_limpio['Alumno'] = df_limpio['Alumno'].fillna('Desconocido')

# Rellenar edades faltantes con el promedio matemático del resto de la clase
promedio_edad = df_limpio['Edad'].mean()
df_limpio['Edad'] = df_limpio['Edad'].fillna(promedio_edad)

# Rellenar horas de celular faltantes con 0
df_limpio['Horas_Celular'] = df_limpio['Horas_Celular'].fillna(0)

# El dataset ahora está listo para la fase de Exploración y Modelado
"""
    },
    "Modulo 2: Analitica Estructurada": {
        "Escalera": [
            {
                "nivel": "Análisis Descriptivo",
                "pregunta": "¿Qué pasó?",
                "detalle": "Enfocado exclusivamente en el examen del pasado mediante el uso de reportes históricos y tabulados estáticos. Representa la base del valor analítico."
            },
            {
                "nivel": "Análisis de Diagnóstico",
                "pregunta": "¿Por qué pasó?",
                "detalle": "Evaluación orientada a descubrir causas raíz, dependencias y correlaciones estadísticas entre las variables del negocio."
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
        "Roles": [
            {
                "rol": "Data Analyst",
                "enfoque": "Interpretación del negocio, generación de tableros y comunicación de métricas históricas.",
                "herramientas": "SQL, Excel, herramientas de Business Intelligence como Power BI o Tableau."
            },
            {
                "rol": "Data Scientist",
                "enfoque": "Diseño de modelos predictivos, experimentación, análisis estadístico avanzado e investigación matemática.",
                "herramientas": "Python, R, entornos Jupyter, frameworks de Machine Learning."
            },
            {
                "rol": "Data Engineer",
                "enfoque": "Desarrollo de infraestructura, arquitectura de almacenamiento masivo y construcción de tuberías ETL.",
                "herramientas": "Spark, entornos Cloud, gestión de bases de datos relacionales y no relacionales."
            }
        ]
    },
    "Modulo 3: Inteligencia Artificial": {
        "Paradigma": """
        El paso de la ingeniería de software tradicional al desarrollo de sistemas inteligentes implica un cambio estructural en la lógica de computación:
        
        * **Sistemas Basados en Reglas (Programación Tradicional):** Los desarrolladores definen manualmente la lógica y las instrucciones condicionales del código. Al ingresar datos de entrada, el sistema ejecuta las reglas preestablecidas y computa una salida.
        * **Machine Learning (Aprendizaje Automático):** Modifica el flujo operativo. Se proveen los datos de entrada junto con las respuestas o etiquetas deseadas. El algoritmo procesa esta información para descubrir de forma autónoma los patrones subyacentes, generando sus propias reglas de decisión.
        """,
        "Deep Learning": """
        ### Redes Neuronales Artificiales Profundas
        Subcampo del Machine Learning especializado en el diseño automático de características complejas a través del uso de múltiples capas ocultas de procesamiento. Es la tecnología detrás del reconocimiento de imágenes y el procesamiento de lenguaje avanzado.
        
        ### El Requerimiento Crítico del Volumen
        A diferencia de los modelos analíticos clásicos, el rendimiento de una red neuronal profunda depende de manera crítica de la disponibilidad de conjuntos de datos masivos. 
        
        Sin un gran volumen de datos de alta calidad para entrenamiento, el modelo es propenso al estancamiento y pierde capacidad de generalización ante nuevos escenarios. El éxito de estos sistemas radica en la iteración constante y el volumen de la información procesada.
        """
    }
}

# Titulo principal de la aplicacion
st.title("Repositorio Teórico: Ciencia de Datos e Inteligencia Artificial")
st.markdown("Material de consulta y referencia conceptual.")
st.markdown("---")

# Seccion de navegacion en barra lateral
st.sidebar.title("Índice de Temas")
modulo_seleccionado = st.sidebar.radio("Seleccionar Unidad:", list(conocimiento.keys()))
st.sidebar.markdown("---")
st.sidebar.caption("Espacio de documentación estática para el análisis diagnóstico.")

# Renderizado logico de contenidos segun seleccion
if modulo_seleccionado == "Modulo 1: Fundamentos de Datos":
    st.header("Módulo 1: Fundamentos de Datos")
    
    # Agregamos una tercera pestaña para el código
    tab1, tab2, tab3 = st.tabs(["Glosario Base", "Ciclo de Vida del Dato", "Práctica en Python"])
    
    with tab1:
        st.markdown("### Conceptos Elementales")
        for item in conocimiento["Modulo 1: Fundamentos de Datos"]["Glosario"]:
            with st.expander(item["termino"]):
                st.write(item["definicion"])
                
    with tab2:
        st.markdown("### El Proceso de la Información")
        st.markdown(conocimiento["Modulo 1: Fundamentos de Datos"]["Proceso"])
        
    with tab3:
        st.markdown("### Ejemplo Real: Limpiando Datos con Pandas")
        st.markdown("Este bloque de código muestra cómo se ejecuta la fase de limpieza en un entorno profesional utilizando la librería `pandas` en Python. El objetivo es tratar los valores nulos (vacíos) y eliminar registros duplicados.")
        st.code(conocimiento["Modulo 1: Fundamentos de Datos"]["Codigo_Pandas"], language='python')

elif modulo_seleccionado == "Modulo 2: Analitica Estructurada":
    st.header("Módulo 2: Analítica Estructurada")
    tab1, tab2 = st.tabs(["Tipos de Análisis", "Ecosistema Profesional"])
    
    with tab1:
        st.markdown("### Evolución del Análisis de Datos")
        for nivel in conocimiento["Modulo 2: Analitica Estructurada"]["Escalera"]:
            st.subheader(nivel["nivel"])
            st.markdown(f"*Interrogante central:* {nivel['pregunta']}")
            st.write(nivel["detalle"])
            st.markdown("---")
            
    with tab2:
        st.markdown("### Perfiles Laborales del Sector")
        for perfil in conocimiento["Modulo 2: Analitica Estructurada"]["Roles"]:
            with st.expander(perfil["rol"]):
                st.markdown(f"**Enfoque principal:** {perfil['enfoque']}")
                st.markdown(f"**Herramientas clave:** `{perfil['herramientas']}`")

elif modulo_seleccionado == "Modulo 3: Inteligencia Artificial":
    st.header("Módulo 3: Inteligencia Artificial")
    tab1, tab2 = st.tabs(["Cambio de Paradigma", "Deep Learning"])
    
    with tab1:
        st.markdown("### Reglas vs. Aprendizaje Autómata")
        st.markdown(conocimiento["Modulo 3: Inteligencia Artificial"]["Paradigma"])
        
    with tab2:
        st.markdown("### Redes Neuronales y Datos Masivos")
        st.markdown(conocimiento["Modulo 3: Inteligencia Artificial"]["Deep Learning"])
        
