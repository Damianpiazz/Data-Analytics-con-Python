# Calidad de Datos en Análisis de Datos

## 1. Concepto de Calidad de Datos

La calidad de los datos es la medida en la que un conjunto de datos resulta apto para un propósito específico. No implica únicamente precisión, sino que abarca múltiples dimensiones necesarias para que el análisis sea robusto.

### Atributos Clave de la Calidad
* **Precisión:** Los datos deben reflejar la realidad con exactitud. Registros incorrectos conducen a análisis de resultados erróneos.
* **Completitud:** Indica si los datos están presentes o si faltan registros (valores nulos). La falta de información impide análisis completos.
* **Consistencia:** Los datos deben ser coherentes entre distintas fuentes y registros. Inconsistencias (ej. diferentes formatos de dirección) dificultan la integración de datos.
* **Validez:** Los datos deben ajustarse a criterios o restricciones predefinidas, como el formato de fechas o rangos numéricos permitidos.
* **Relevancia:** Los datos recopilados deben ser útiles y necesarios para responder a las preguntas de negocio planteadas.

La baja calidad de los datos impacta directamente en las decisiones empresariales, pudiendo resultar en pérdidas de recursos, sobreproducción o estrategias de marketing mal fundamentadas.

---

## 2. Identificación y Tratamiento de Valores Nulos y Duplicados

La limpieza de datos es un paso crítico para asegurar que los modelos estadísticos y algoritmos de machine learning operen correctamente.

### 2.1 Valores Nulos
Representan la ausencia de información, provocada frecuentemente por errores de recolección o problemas en formularios.

**Estrategias de tratamiento:**
* **Eliminación:** Se suprimen filas o columnas con nulos si estos son mínimos y no alteran la significancia del análisis.
* **Imputación:** Se rellenan los valores nulos con estadísticos como la media, mediana o moda, o mediante algoritmos predictivos más complejos.
* **Predicción:** Modelado de los valores faltantes basándose en otras variables existentes en el dataset.

### 2.2 Valores Duplicados
Ocurren cuando un registro aparece más de una vez, a menudo por errores en la entrada de datos o problemas al combinar múltiples fuentes. Los duplicados distorsionan el análisis al inflar conteos.

**Proceso de tratamiento:**
1. **Identificación:** Localización de registros repetidos.
2. **Eliminación:** Supresión de las ocurrencias adicionales, manteniendo únicamente la primera instancia detectada.

---

## 3. Evaluación de Calidad con Python (Pandas)

Para evaluar y limpiar datasets utilizando la biblioteca Pandas, se recomiendan los siguientes métodos fundamentales:

* `df.info()`: Proporciona un resumen general del DataFrame, incluyendo el conteo de valores no nulos y los tipos de datos en cada columna.
* `df.isnull().sum()`: Calcula el número total de valores nulos presentes en cada columna, permitiendo localizar rápidamente dónde falta información.
* `df.duplicated()`: Identifica los registros repetidos en el DataFrame.

La correcta aplicación de estas técnicas permite transformar datos crudos en conjuntos de alta calidad, fundamentales para generar conclusiones confiables y estrategias empresariales efectivas.