# Estadística Descriptiva

## 1. Introducción a la Estadística en Python
La estadística es un campo amplio que permite resumir y analizar datos. Python ofrece diversas librerías especializadas para abordar diferentes facetas de esta disciplina:

* **SciPy (`scipy.stats`):** Proporciona un amplio conjunto de funciones para análisis estadístico básico, incluyendo distribuciones de probabilidad, pruebas de hipótesis (t, ANOVA, chi-cuadrado) e intervalos de confianza.
* **Statsmodels:** Enfocada en análisis estadísticos avanzados, como regresiones (lineales y no lineales) y modelado de series temporales.
* **Pandas:** Fundamental para la manipulación tabular de datos, limpieza, transformación y manejo de series temporales.
* **Seaborn:** Biblioteca de visualización basada en Matplotlib, orientada a representar datos estadísticos, incluyendo correlaciones y distribuciones.

---

## 2. Medidas de Tendencia Central
Las medidas de tendencia central resumen un conjunto de datos mediante un único valor que representa el centro de la distribución.

* **Media:** Promedio aritmético (suma de valores dividida por el total).
    * Fórmula: $Media = \frac{\sum_{i=1}^{n}x_{i}}{n}$
* **Mediana:** Valor central en un conjunto ordenado. Si el número de observaciones es par, es el promedio de los dos centrales.
* **Moda:** Valor que aparece con mayor frecuencia en el conjunto de datos.

---

## 3. Cuartiles y Percentiles
Estas herramientas permiten resumir datasets, identificar valores atípicos (*outliers*) y comprender la variabilidad de la distribución.

* **Cuartiles ($Q_1, Q_2, Q_3$):** Dividen el conjunto de datos en cuatro partes iguales.
    * **$Q_1$ (Primer cuartil):** 25% de los datos por debajo de este punto.
    * **$Q_2$ (Mediana):** 50% de los datos por debajo.
    * **$Q_3$ (Tercer cuartil):** 75% de los datos por debajo.
* **Percentiles:** Dividen los datos en 100 partes iguales. Cada percentil indica el valor bajo el cual se encuentra un porcentaje específico de los datos.

### Rango Intercuartil (IQR)
Diferencia entre el tercer y el primer cuartil ($IQR = Q_3 - Q_1$). Es una medida de dispersión de la mitad central de los datos, efectiva para distribuciones sesgadas o con valores atípicos.

---

## 4. Diagrama de Caja (BoxPlot)
Gráfico que muestra la distribución de datos numéricos.

* **Componentes:**
    * **Caja:** Rango intercuartílico (IQR).
    * **Línea central:** Mediana ($Q_2$).
    * **Bigotes:** Líneas que extienden el rango de variabilidad.
    * **Valores atípicos:** Puntos fuera de los bigotes.
* **Utilidad:** Permite intuir la morfología, simetría y dispersión de los datos.

---

## 5. Medidas de Dispersión
Indican cuán alejados están los valores respecto a la tendencia central.

* **Rango:** Diferencia entre el valor máximo y el mínimo.
* **Varianza:** Promedio de las diferencias al cuadrado entre cada valor y la media.
    * Fórmula: $Varianza = \frac{\sum_{i=1}^{n}(x_i - media)^2}{n}$
* **Desviación Estándar:** Raíz cuadrada de la varianza. Proporciona una medida de dispersión en las mismas unidades que los datos originales.
    * Fórmula: $Desviación Estándar = \sqrt{Varianza}$