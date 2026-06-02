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
    
    /* Estilo de bloques de codigo o texto destacado */
    code {
        color: #ffffff !important;
        background-color: #1a1a1a !important;
        border: 1px solid #2a2a2a !important;
        border-radius: 3px !important;
        padding: 0.2rem 0.4rem !important;
    }
    
    /* Ocultar elementos nativos de la interfaz de Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# Base de datos de conocimiento estructurada sin elementos visuales distractores
conocimiento = {
    "Modulo 1: Fundamentos de Datos": {
        "Glosario": [
            {
                "termino": "Dato",
                "definicion": "Un hecho aislado, una unidad minima de informacion cuantitativa o cualitativa que puede ser registrada, medida o contada sin un contexto previo (ejemplo: un numero de calzado, un registro de temperatura)."
            },
            {
                "termino": "Analisis de Datos",
                "definicion": "El proceso sistematico de examinar, limpiar, transformar y modelar datos con el objetivo de descubrir patrones, tendencias y relaciones que permitan extraer conclusiones utiles."
            },
            {
                "termino": "Informacion",
                "definicion": "El resultado de procesar, organizar e interpretar un conjunto de datos dentro de un contexto especifico, dandoles un significado que reduce la incertidumbre."
            }
        ],
        "Proceso": """
        El flujo de procesamiento profesional de la informacion se compone de cinco etapas criticas:
        
        1. **Captura:** Recoleccion de variables desde fuentes crudas.
        2. **Limpieza:** Tratamiento de datos nulos, duplicados o erroneos. Esta fase tecnica consume aproximadamente el 80% del tiempo de un proyecto de datos.
        3. **Exploracion:** Identificacion preliminar de sesgos, distribuciones y correlaciones mediante estadistica descriptiva.
        4. **Modelado:** Aplicacion de algoritmos matematicos y metricas de evaluacion.
        5. **Historia:** Visualizacion avanzada y comunicacion tecnica de los hallazgos.
        
        *Principio rector:* Garbage In, Garbage Out. Si alimentamos un sistema con datos basura, las decisiones y los resultados seran basura.
        """
    },
    "Modulo 2: Analitica Estructurada": {
        "Escalera": [
            {
                "nivel": "Analisis Descriptivo",
                "pregunta": "¿Qué paso?",
                "detalle": "Enfocado exclusivamente en el examen del pasado mediante el uso de reportes historicos y tabulados estaticos. Representa la base del valor analitico."
            },
            {
                "nivel": "Analisis de Diagnostico",
                "pregunta": "¿Por que paso?",
                "detalle": "Evaluacion orientada a descubrir causas raiz, dependencias y correlaciones estadisticas entre las variables del negocio."
            },
            {
                "nivel": "Analisis Predictivo",
                "pregunta": "¿Qué pasara?",
                "detalle": "Construccion de proyecciones futuras fundamentadas en modelos estadisticos avanzados y algoritmos de Machine Learning."
            },
            {
                "nivel": "Analisis Prescriptivo",
                "pregunta": "¿Qué debemos hacer?",
                "detalle": "Automatizacion de la toma de decisiones complejas, sugiriendo o ejecutando acciones optimas basadas en optimizacion matematica."
            }
        ],
        "Roles": [
            {
                "rol": "Data Analyst",
                "enfoque": "Interpretacion del negocio, generacion de tableros y comunicacion de metricas historicas.",
                "herramientas": "SQL, Excel, herramientas de Business Intelligence como Power BI o Tableau."
            },
            {
                "rol": "Data Scientist",
                "enfoque": "Diseno de modelos predictivos, experimentacion, analisis estadistico avanzado e investigacion matematica.",
                "herramientas": "Python, R, entornos Jupyter, frameworks de Machine Learning."
            },
            {
                "rol": "Data Engineer",
                "enfoque": "Desarrollo de infraestructura, arquitectura de almacenamiento masivo y construccion de tuberias ETL.",
                "herramientas": "Spark, entornos Cloud, gestion de bases de datos relacionales y no relacionales."
            }
        ]
    },
    "Modulo 3: Inteligencia Artificial": {
        "Paradigma": """
        El paso de la ingenieria de software tradicional al desarrollo de sistemas inteligentes implica un cambio estructural en la logica de computacion:
        
        * **Sistemas Basados en Reglas (Programacion Tradicional):** Los desarrolladores definen manualmente la logica y las instrucciones condicionales del codigo. Al ingresar datos de entrada, el sistema ejecuta las reglas preestablecidas y computa una salida.
        * **Machine Learning (Aprendizaje Automatico):** Modifica el flujo operativo. Se proveen los datos de entrada junto con las respuestas o etiquetas deseadas. El algoritmo procesa esta informacion para descubrir de forma autonoma los patrones subyacentes, generando sus propias reglas de decision.
        """,
        "Deep Learning": """
        ### Redes Neuronales Artificiales Profundas
        Subcampo del Machine Learning especializado en el diseno automatico de caracteristicas complejas a traves del uso de multiples capas ocultas de procesamiento. Es la tecnologia detras del reconocimiento de imagenes y el procesamiento de lenguaje avanzado.
        
        ### El Requerimiento Critico del Volumen
        A diferencia de los modelos analiticos clasicos, el rendimiento de una red neuronal profunda depende de manera critica de la disponibilidad de conjuntos de datos masivos. 
        
        Sin un gran volumen de datos de alta calidad para entrenamiento, el modelo es propenso al estancamiento y pierde capacidad de generalizacion ante nuevos escenarios. El exito de estos sistemas radica en la iteracion constante
        
