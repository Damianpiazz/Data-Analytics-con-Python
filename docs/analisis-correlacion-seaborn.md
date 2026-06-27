# Análisis de Correlación

## 1. Concepto de Correlación
La correlación es una medida estadística que describe la relación entre dos o más variables. Cuando dos variables están correlacionadas, un cambio en una de ellas tiende a estar acompañado por un cambio en la otra. 

* **Importancia:** Permite identificar patrones y tendencias en los datos, ayudando a determinar si el comportamiento de una variable influye o se desplaza en sincronía con otra.

## 2. Medición y Cálculo
En el entorno de Pandas, la matriz de correlación se obtiene mediante el método `.corr()`. Esta matriz cuantifica la fuerza y la dirección de la relación lineal entre todas las variables numéricas de un DataFrame.

* **Interpretación:** Los valores de correlación suelen oscilar entre -1 y 1:
    * **1:** Correlación positiva perfecta (ambas variables aumentan juntas).
    * **0:** No existe relación lineal.
    * **-1:** Correlación negativa perfecta (cuando una aumenta, la otra disminuye).

## 3. Visualización de Correlaciones
Para facilitar la interpretación de grandes matrices de correlación, se utilizan técnicas visuales mediante la librería **Seaborn**:

* **Mapas de calor (Heatmaps):** Representación gráfica donde los valores de correlación se asocian a una escala de colores, permitiendo detectar rápidamente relaciones fuertes (positivas o negativas).
* **Diagramas de dispersión (Scatter Plots):** Representan la relación directa entre dos variables, donde cada punto en el gráfico es una observación, facilitando la identificación visual de la forma y fuerza de la correlación.

## 4. Aplicaciones Técnicas
El análisis de correlación es fundamental para:
1. **Reducción de dimensionalidad:** Identificar variables redundantes que aportan información similar.
2. **Selección de características:** Determinar qué variables tienen una relación más fuerte con el objetivo de estudio, lo cual es crucial para mejorar el rendimiento de modelos de Machine Learning.
3. **Exploración de datos:** Establecer hipótesis iniciales sobre qué variables merecen un estudio más detallado.