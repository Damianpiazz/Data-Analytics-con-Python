# Análisis Exploratorio de Datos (EDA)

## 1. Concepto de EDA
El Análisis Exploratorio de Datos (EDA, por sus siglas en inglés) es un enfoque fundamental en el análisis de datos que permite a los analistas comprender la composición y estructura de un conjunto de datos antes de aplicar modelos complejos.

* **Objetivo:** Identificar patrones, anomalías, relaciones entre variables y estructuras subyacentes mediante un examen visual y estadístico resumido.
* **Importancia:**
    * Facilita la detección temprana de problemas como valores faltantes, irregularidades en la distribución o valores atípicos (*outliers*).
    * Ayuda a formular hipótesis sobre las relaciones entre variables.
    * Es el paso previo indispensable para validar la calidad de los datos y determinar la estrategia de modelado más adecuada.

---

## 2. Técnicas de EDA
El proceso de EDA combina técnicas de resumen estadístico con visualización gráfica para obtener una visión integral del dataset.

### Visualización de Datos
La visualización es el componente central del EDA para interpretar grandes volúmenes de información de manera intuitiva.
* **Bibliotecas clave:** Python utiliza librerías como Matplotlib, Seaborn y Plotly para generar gráficos que facilitan la identificación de tendencias y anomalías.
* **Tipos de gráficos comunes:**
    * **Gráficos de barras:** Ideales para comparar magnitudes entre categorías.
    * **Diagramas de caja (Box Plots):** Cruciales para visualizar distribuciones, dispersión y detectar valores atípicos.
    * **Histogramas:** Útiles para observar la frecuencia y distribución de variables numéricas.

### Resumen Estadístico
El EDA incluye el cálculo de medidas descriptivas para condensar la información:
* **Tendencia central:** Media, mediana y moda para localizar el centro de la distribución.
* **Dispersión:** Desviación estándar y rango para medir cuánto se alejan los datos del valor central.
* **Correlación:** Análisis de la relación entre variables para determinar si el comportamiento de una influye en la otra.

---

## 3. Flujo de Trabajo en EDA
El análisis exploratorio suele seguir una secuencia lógica:
1. **Carga y visualización inicial:** Importación del dataset y revisión de las primeras filas.
2. **Resumen de datos:** Uso de herramientas de Pandas (`df.info()`, `df.describe()`) para obtener una visión general de tipos de datos, conteos y estadísticas básicas.
3. **Identificación de problemas:** Localización de valores nulos, registros duplicados o datos fuera de rango (anómalos).
4. **Visualización diagnóstica:** Creación de gráficos para confirmar las sospechas estadísticas encontradas en la fase de resumen.
5. **Formulación de hipótesis:** Definición de posibles relaciones que serán confirmadas o descartadas en etapas posteriores de modelado.