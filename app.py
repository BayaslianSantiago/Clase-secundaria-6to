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

# Base de datos de conocimiento estructurada
conocimiento = {
    "Modulo 1: Fundamentos de Datos": {
        "Glosario": [
            {
                "termino": "Dato",
                "definicion": "Cualquier informacion que podemos registrar, medir o contar[span_1](start_span)[span_1](end_span). Son la base de todo analisis y se expresan con numeros o palabras[span_2](start_span)[span_2](end_span)."
            },
            {
                "termino": "Analisis de Datos",
                "definicion": "El proceso sistematico de limpiar, transformar y modelar datos para descubrir patrones que apoyen la toma de decisiones estrategicas[span_3](start_span)[span_3](end_span)."
            },
            {
                "termino": "Informacion",
                "definicion": "El resultado de procesar, organizar e interpretar un conjunto de datos dentro de un contexto especifico, dandoles un significado que reduce la incertidumbre[span_4](start_span)[span_4](end_span)."
            }
        ],
        "Proceso": """
        El flujo de procesamiento profesional de la informacion se compone de cinco etapas criticas[span_5](start_span)[span_5](end_span):
        
        1. **Captura:** Recoleccion desde fuentes crudas[span_6](start_span)[span_6](end_span).
        2. **Limpieza:** Tratamiento de nulos y duplicados[span_7](start_span)[span_7](end_span). Esta fase tecnica consume aproximadamente el 80% del trabajo de un analista profesional[span_8](start_span)[span_8](end_span).
        3. **Exploracion:** Identificacion de tendencias iniciales[span_9](start_span)[span_9](end_span).
        4. **Modelado:** Aplicacion de algoritmos y metricas[span_10](start_span)[span_10](end_span).
        5. **Historia:** Visualizacion y comunicacion de resultados[span_11](start_span)[span_11](end_span).
        
        *Principio rector:* Garbage in, Garbage out[span_12](start_span)[span_12](end_span). Sin datos precisos, cualquier analisis llevara a decisiones erroneas[span_13](start_span)[span_13](end_span).
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

# A. Eliminar filas duplicadas (El registro de 'Ana' esta repetido exactamente igual)
df_limpio = df.drop_duplicates()

# B. Tratar valores nulos (NaN - Not a Number)
# Rellenar nombres faltantes con una etiqueta estandar
df_limpio['Alumno'] = df_limpio['Alumno'].fillna('Desconocido')

# Rellenar edades faltantes con el promedio matematico del resto de la clase
promedio_edad = df_limpio['Edad'].mean()
df_limpio['Edad'] = df_limpio['Edad'].fillna(promedio_edad)

# Rellenar horas de celular faltantes con 0
df_limpio['Horas_Celular'] = df_limpio['Horas_Celular'].fillna(0)

# El dataset ahora esta listo para la fase de Exploracion y Modelado
"""
    },
    "Modulo 2: Analitica Estructurada": {
        "Escalera": [
            {
                "nivel": "Analisis Descriptivo",
                "pregunta": "¿Qué paso?",
                "detalle": "Enfocado en el pasado mediante reportes historicos[span_14](start_span)[span_14](end_span)."
            },
            {
                "nivel": "Analisis de Diagnostico",
                "pregunta": "¿Por que paso?",
                "detalle": "Buscando causas raiz y correlaciones[span_15](start_span)[span_15](end_span)."
            },
            {
                "nivel": "Analisis Predictivo",
                "pregunta": "¿Qué pasara?",
                "detalle": "Modelos estadisticos y Machine Learning[span_16](start_span)[span_16](end_span)."
            },
            {
                "nivel": "Analisis Prescriptivo",
                "pregunta": "¿Qué hacer?",
                "detalle": "Recomendaciones automaticas de accion[span_17](start_span)[span_17](end_span)."
            }
        ],
        "Roles": [
            {
                "rol": "Data Analyst",
                "enfoque": "Interpretacion de negocio y visualizacion[span_18](start_span)[span_18](end_span).",
                "herramientas": "SQL, Excel, Power BI[span_19](start_span)[span_19](end_span)."
            },
            {
                "rol": "Data Scientist",
                "enfoque": "Modelos predictivos y experimentacion[span_20](start_span)[span_20](end_span).",
                "herramientas": "Python, R, Machine Learning[span_21](start_span)[span_21](end_span)."
            },
            {
                "rol": "Data Engineer",
                "enfoque": "Infraestructura, tuberias y ETL[span_22](start_span)[span_22](end_span).",
                "herramientas": "Spark, Cloud, Hadoop[span_23](start_span)[span_23](end_span)."
            }
        ]
    },
    "Modulo 3: Inteligencia Artificial": {
        "Glosario_IA": [
            {
                "termino": "Inteligencia Artificial (IA)",
                "definicion": "Concepto global que representa la capacidad de las maquinas de realizar tareas 'inteligentes[span_24](start_span)'[span_24](end_span)."
            },
            {
                "termino": "Machine Learning",
                "definicion": "Subdominio de la IA que proporciona a los sistemas la capacidad de aprender y mejorar automaticamente a partir de la experiencia sin ser explicitamente programados para ellos[span_25](start_span)[span_25](end_span)."
            },
            {
                "termino": "Deep Learning",
                "definicion": "Rama que utiliza redes neuronales, buscando emular el comportamiento de las neuronas de los seres humanos y sus interconexiones[span_26](start_span)[span_26](end_span)."
            }
        ],
        "ML_vs_DL": """
        ### La Diferencia en la Extraccion de Caracteristicas
        El rendimiento de los algoritmos depende en gran medida de la presentacion de los datos[span_27](start_span)[span_27](end_span). La diferencia tecnica central entre ambos paradigmas es:
        
        * **Tecnicas clasicas de Machine Learning:** Requieren un diseno manual de caracteristicas[span_28](start_span)[span_28](end_span). Un humano procesa y selecciona las variables, y el modelo toma una decision a partir de esas caracteristicas[span_29](start_span)[span_29](end_span).
        * **Tecnicas de Deep Learning:** Realizan un diseno automatico de caracteristicas simples en sus capas iniciales, procesando luego capas adicionales con caracteristicas abstractas, para finalmente tomar una decision a partir de las caracteristicas[span_30](start_span)[span_30](end_span).
        """,
        "Volumen": """
        ### El Requerimiento del Volumen de Datos
        Para que los algoritmos de Deep Learning funcionen adecuadamente se requiere un conjunto de datos grandes[span_31](start_span)[span_31](end_span). 
        
        Mientras que los algoritmos de Machine Learning tradicional suelen estancarse en rendimiento al alcanzar un limite de datos procesados, el Deep Learning (como las redes neuronales grandes) continua mejorando su performance a medida que aumenta la cantidad de informacion que recibe[span_32](start_span)[span_32](end_span).
        """
    }
}

# Titulo principal de la aplicacion
st.title("Repositorio Teórico: Ciencia de Datos e Inteligencia Artificial")
st.markdown("Material de consulta y referencia conceptual.")
st.markdown("---")

# Seccion de navegacion en barra lateral
st.sidebar.title("Indice de Temas")
modulo_seleccionado = st.sidebar.radio("Seleccionar Unidad:", list(conocimiento.keys()))
st.sidebar.markdown("---")
st.sidebar.caption("Espacio de documentacion estatica para el analisis diagnostico.")

# Renderizado logico de contenidos segun seleccion
if modulo_seleccionado == "Modulo 1: Fundamentos de Datos":
    st.header("Modulo 1: Fundamentos de Datos")
    
    tab1, tab2, tab3 = st.tabs(["Glosario Base", "Ciclo de Vida del Dato", "Practica en Python"])
    
    with tab1:
        st.markdown("### Conceptos Elementales")
        for item in conocimiento["Modulo 1: Fundamentos de Datos"]["Glosario"]:
            with st.expander(item["termino"]):
                st.write(item["definicion"])
                
    with tab2:
        st.markdown("### El Proceso de la Informacion")
        st.markdown(conocimiento["Modulo 1: Fundamentos de Datos"]["Proceso"])
        
    with tab3:
        st.markdown("### Ejemplo Real: Limpiando Datos con Pandas")
        st.markdown("Este bloque de codigo muestra como se ejecuta la fase de limpieza en un entorno profesional utilizando la libreria `pandas` en Python. El objetivo es tratar los valores nulos (vacios) y eliminar registros duplicados.")
        st.code(conocimiento["Modulo 1: Fundamentos de Datos"]["Codigo_Pandas"], language='python')

elif modulo_seleccionado == "Modulo 2: Analitica Estructurada":
    st.header("Modulo 2: Analitica Estructurada")
    tab1, tab2 = st.tabs(["Tipos de Analisis", "Ecosistema Profesional"])
    
    with tab1:
        st.markdown("### Evolucion del Analisis de Datos")
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
    st.header("Modulo 3: Inteligencia Artificial")
    tab1, tab2, tab3 = st.tabs(["Conceptos Elementales", "ML vs. Deep Learning", "El Factor del Volumen"])
    
    with tab1:
        st.markdown("### Glosario de Inteligencia Artificial")
        for item in conocimiento["Modulo 3: Inteligencia Artificial"]["Glosario_IA"]:
            with st.expander(item["termino"]):
                st.write(item["definicion"])
                
    with tab2:
        st.markdown("### Diferencias Estructurales")
        st.markdown(conocimiento["Modulo 3: Inteligencia Artificial"]["ML_vs_DL"])
        
    with tab3:
        st.markdown("### Rendimiento y Datos")
        st.markdown(conocimiento["Modulo 3: Inteligencia Artificial"]["Volumen"])
        
