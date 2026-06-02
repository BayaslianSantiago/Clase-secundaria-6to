import streamlit as st

# Configuracion de la pagina
st.set_page_config(page_title="Glosario de Datos e IA", layout="centered")

# Inyeccion de CSS para forzar un tema oscuro minimalista y ocultar botones/menus
st.markdown("""
    <style>
    .stApp {
        background-color: #0a0a0a;
        color: #e5e5e5;
    }
    h1, h2, h3 {
        color: #ffffff !important;
        font-weight: 600;
        margin-top: 2rem;
    }
    hr {
        border-color: #222222 !important;
    }
    code {
        color: #ffffff !important;
        background-color: #1a1a1a !important;
        border: 1px solid #2a2a2a !important;
        border-radius: 3px !important;
        padding: 0.2rem 0.4rem !important;
    }
    /* Ocultar elementos nativos de la interfaz para que parezca un documento estatico */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    [data-testid="stSidebar"] {display: none;}
    </style>
    """, unsafe_allow_html=True)

# Encabezado
st.title("Glosario: Ciencia de Datos e Inteligencia Artificial")
st.markdown("Documentación estática de lectura continua para la clase.")
st.markdown("---")

# Módulo 1
st.header("1. Fundamentos de Datos")
st.markdown("""
**Dato:** Cualquier información que podemos registrar, medir o contar. Son hechos concretos expresados en números o palabras sin contexto previo.

**Información:** Es el resultado de procesar y organizar un conjunto de datos dentro de un contexto, dándoles un significado que reduce la incertidumbre.

**Análisis de Datos:** El proceso de limpiar, transformar y estudiar datos para descubrir patrones y tomar decisiones informadas.

**Ciclo de Vida del Dato:**
1. **Captura:** Recolección de datos crudos.
2. **Limpieza:** Tratamiento de errores, nulos y duplicados (Consume el 80% del tiempo de trabajo).
3. **Exploración:** Búsqueda de tendencias y estadística inicial.
4. **Modelado:** Aplicación de algoritmos.
5. **Historia:** Comunicación visual de los resultados.
""")

# Módulo 2: Pandas
st.header("2. Práctica: Limpieza de Datos")
st.markdown("""
El trabajo de limpieza garantiza que los sistemas no aprendan de información errónea (el principio de *Garbage In, Garbage Out*). 
A continuación, se muestra cómo se realiza la limpieza de datos nulos y duplicados utilizando código Python con la librería Pandas:
""")

codigo_pandas = """import pandas as pd
import numpy as np

# 1. Datos crudos con errores (nulos y un registro duplicado)
datos = {
    'Alumno': ['Juan', 'Ana', 'Pedro', 'Ana', 'Sofia', np.nan],
    'Edad': [17, 18, np.nan, 18, 17, 18],
    'Horas_Celular': [5, 3, 6, 3, np.nan, 4]
}
df = pd.DataFrame(datos)

# 2. Limpieza de duplicados (se elimina la segunda 'Ana')
df_limpio = df.drop_duplicates()

# 3. Tratamiento de valores nulos (vacios)
# Rellenar nombres faltantes con la etiqueta 'Desconocido'
df_limpio['Alumno'] = df_limpio['Alumno'].fillna('Desconocido')

# Rellenar edades vacias con el promedio matematico del curso
promedio = df_limpio['Edad'].mean()
df_limpio['Edad'] = df_limpio['Edad'].fillna(promedio)

# Rellenar horas de celular vacias con 0
df_limpio['Horas_Celular'] = df_limpio['Horas_Celular'].fillna(0)
"""
st.code(codigo_pandas, language='python')

# Módulo 3
st.header("3. La Escalera Analítica y los Roles")
st.markdown("""
**Los 4 Niveles de Análisis:**
* **Descriptivo:** ¿Qué pasó? (Reportes históricos y conteos).
* **Diagnóstico:** ¿Por qué pasó? (Causas raíz y cruce de variables).
* **Predictivo:** ¿Qué pasará? (Modelos estadísticos sobre tendencias futuras).
* **Prescriptivo:** ¿Qué hacer? (Automatización de decisiones complejas).

**Roles del Ecosistema:**
* **Data Analyst:** Analiza el negocio, limpia datos y crea visualizaciones (SQL, Power BI).
* **Data Scientist:** Diseña modelos predictivos y experimentación matemática (Python, Machine Learning).
* **Data Engineer:** Construye la arquitectura, servidores y automatiza el flujo de datos (Spark, Cloud).
""")

# Módulo 4
st.header("4. Inteligencia Artificial y Aprendizaje Automático")
st.markdown("""
**Inteligencia Artificial (IA):** Concepto global que representa la capacidad de los sistemas informáticos para realizar tareas que normalmente requieren inteligencia humana.

**Programación Tradicional vs. Machine Learning:**
* **Tradicional:** Un programador escribe reglas estrictas en el código. Se ingresan los datos, la máquina sigue las reglas y entrega un resultado.
* **Machine Learning:** Se ingresan los datos y las respuestas esperadas. La máquina procesa la información y **descubre las reglas** por su cuenta.

**Machine Learning vs. Deep Learning:**
* **Machine Learning Clásico:** Requiere un diseño manual de características. Un humano debe procesar y seleccionar las variables importantes antes de que el modelo pueda tomar decisiones.
* **Deep Learning (Redes Neuronales):** Realiza un diseño automático de características. El modelo usa múltiples capas de procesamiento para entender información compleja sin intervención humana estructurada, ideal para reconocer imágenes o procesar lenguaje.

**El Factor del Volumen en el Deep Learning:**
Mientras que los algoritmos clásicos se estancan si se les da demasiada información, las Redes Neuronales Profundas (Deep Learning) **necesitan** un volumen masivo de datos para no estancarse. A mayor cantidad de datos de alta calidad en el entrenamiento, mayor capacidad del modelo para generalizar y tomar decisiones correctas en escenarios nuevos.
""")
