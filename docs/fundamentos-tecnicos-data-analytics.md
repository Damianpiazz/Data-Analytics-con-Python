# Introducción al Análisis de Datos y Fundamentos Tecnológicos

## 1. Conceptos Básicos en Ciencias de Datos y Data Analytics

La ciencia de datos es una disciplina interdisciplinaria que combina las matemáticas, la estadística, la informática y el conocimiento de dominio para extraer conocimiento e insights valiosos a partir de los datos.

### ¿Qué es Data Analytics?
El Análisis de Datos es el proceso sistemático de examinar conjuntos de datos con el objetivo de extraer conclusiones valiosas, identificar tendencias y patrones, y facilitar la toma de decisiones informadas dentro de una organización.

### Definiciones Tecnológicas Clave
* **Big Data:** Conjuntos de datos cuya complejidad y volumen superan la capacidad de procesamiento de las herramientas tradicionales. Se caracteriza por las "3 Vs": volumen, velocidad y variedad.
* **Modelado Predictivo:** Uso de modelos estadísticos y algoritmos de Machine Learning para identificar patrones históricos y predecir resultados futuros.
* **Machine Learning:** Rama de la inteligencia artificial que permite a los sistemas aprender de los datos y mejorar su rendimiento sin ser programados explícitamente (clasificación, regresión, agrupamiento).
* **Inteligencia Artificial (IA):** Simulación de procesos de inteligencia humana mediante algoritmos para la resolución de tareas complejas.
* **Visualización de Datos:** Técnica para convertir datos en representaciones gráficas que faciliten la identificación de patrones.
* **Minería de Datos:** Proceso de descubrimiento de relaciones ocultas en grandes volúmenes de información.

---

## 2. Pirámide de la Jerarquía del Conocimiento

La transformación de los elementos primitivos en valor estratégico sigue esta progresión:



[Image of data information knowledge wisdom pyramid]


1. **Sabiduría:** Capacidad de hacer juicios y tomar decisiones estratégicas basadas en el conocimiento, la experiencia y la reflexión.
2. **Conocimiento:** Comprensión e interpretación de la información para aplicarla en contextos específicos.
3. **Información:** Datos procesados, organizados y dotados de significado.
4. **Datos:** Elementos discontinuos, hechos o cifras aisladas que representan eventos sin un contexto asociado.

---

## 3. Procesos en Ciencias de Datos

El ciclo de vida del análisis de datos es un proceso sistemático y cíclico:



1. **Definición del Problema:** Establecer los objetivos y el marco de trabajo del análisis.
2. **Recolección:** Obtención de datos relevantes de fuentes primarias o secundarias.
3. **Preparación (Limpieza):** Transformación, eliminación de duplicados, manejo de nulos y estandarización de formatos.
4. **Análisis Exploratorio (EDA):** Examen estadístico y visual para identificar tendencias preliminares.
5. **Modelado:** Aplicación de técnicas estadísticas o algoritmos para explicar o predecir fenómenos.
6. **Evaluación:** Medición de la efectividad y precisión del modelo mediante métricas de rendimiento.
7. **Interpretación y Comunicación:** Traducción de hallazgos técnicos en informes y dashboards comprensibles.
8. **Implementación y Seguimiento:** Aplicación de resultados en el entorno real y monitoreo continuo del impacto.

---

## 4. Tecnologías de la Información (TIC)

* **DBMS:** Sistemas de gestión de bases de datos para almacenamiento estructurado (MySQL, PostgreSQL).
* **Visualización:** Herramientas para dashboards interactivos (Tableau, Looker Studio, Power BI).
* **Lenguajes:** Python y R (especializados en procesamiento estadístico).
* **Big Data:** Arquitecturas distribuidas para procesamiento paralelo (Hadoop, Spark).
* **Nube:** Infraestructura escalable para almacenamiento y cómputo (AWS, Google Cloud, Azure).
* **Machine Learning e IA:** Bibliotecas especializadas para modelos predictivos (TensorFlow, Scikit-learn).
* **Business Intelligence (BI):** Integración de datos históricos para reportes estratégicos (IBM Cognos, SAP).

---

## 5. Estructuras de Datos en Python

* **Listas:** Colecciones ordenadas y mutables. Versátiles para almacenar elementos heterogéneos.
* **Tuplas:** Colecciones ordenadas e inmutables. Adecuadas para datos que no deben alterarse.
* **Diccionarios:** Pares clave-valor, mutables y desordenados. Optimizados para búsquedas rápidas.
* **Conjuntos (Sets):** Colecciones desordenadas de elementos únicos. Ideales para operaciones de unión e intersección.

### Herramientas Avanzadas
* **Funciones Lambda:** Funciones anónimas compactas para operaciones lógicas en una sola línea.
* **Comprehensions (List/Dict):** Sintaxis concisa para generar listas o diccionarios transformando colecciones existentes.
* **Scope:** Regla LEGB (Local -> Enclosing -> Global -> Built-in) que determina la visibilidad de las variables.

---

## 6. Librerías Analíticas: NumPy y Pandas

* **NumPy:** Base del cálculo numérico eficiente.
    * Estructura principal: **ndarray** (array multidimensional).
    * Ventaja: Cálculos vectorizados mucho más rápidos que las listas nativas.
* **Pandas:** Biblioteca para manipulación de datos estructurados.
    * **Series:** Estructura unidimensional etiquetada.
    * **DataFrame:** Estructura bidimensional tabular con filas y columnas de tipos mixtos.

---

## 7. Calidad de Datos

La calidad de los datos es la adecuación de un dataset para un propósito específico, basada en: **Precisión, Completitud, Consistencia, Validez y Relevancia**.

### Identificación y Tratamiento
* **Valores Nulos:** Ausencia de información. Estrategias: eliminación, imputación (media/mediana/moda) o modelos predictivos.
* **Duplicados:** Registros repetidos que distorsionan análisis. Estrategia: identificación (`duplicated`) y eliminación (`drop_duplicates`).
* **Técnicas de Limpieza con Pandas:**
    * Resumen: `df.info()`
    * Detección de Nulos: `df.isnull().sum()`
    * Corrección de tipos: `df.astype()`
    * Normalización: `df.str.lower()`, `df.str.replace()`