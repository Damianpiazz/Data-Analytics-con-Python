# Integración de Datos en Python, NumPy y Pandas

## 1. Concepto de Integración de Datos
La integración de datos es el proceso de combinar información proveniente de distintas fuentes (bases de datos, archivos CSV, APIs) para obtener una visión unificada y coherente. Es fundamental para consolidar datos dispersos en una estructura adecuada para el análisis avanzado.

---

## 2. Operaciones sobre Conjuntos (Set Operations)
El tipo de dato `set` permite realizar operaciones basadas en el álgebra de conjuntos para manipular colecciones de elementos únicos:

* **Unión (`|`):** Combina todos los elementos de dos o más conjuntos.
* **Intersección (`&`):** Extrae únicamente los elementos comunes presentes en todos los conjuntos.
* **Diferencia (`-`):** Extrae los elementos de un conjunto que no pertenecen al otro.
* **Diferencia Simétrica (`^`):** Extrae todos los elementos de ambos conjuntos que no son comunes entre sí.

---

## 3. Integración en NumPy

### Concatenación con `np.concatenate()`
Función principal para unir vectores o matrices de NumPy, respetando las dimensiones de cada objeto.

**Sintaxis:** `np.concatenate((a1, a2, ...), axis=0)`

* **Parámetros:**
    * `axis=0`: Unión por filas (por defecto).
    * `axis=1`: Unión por columnas.
    * `axis=None`: Aplanamiento del resultado a un único vector unidimensional.
    * `out`: Permite guardar el resultado en un objeto existente (debe coincidir en dimensiones).

**Consideraciones Dimensionales:**
Para combinar matrices con vectores, es necesario ajustar las dimensiones (convertir el vector en una matriz). Si se intenta concatenar objetos con distinta dimensionalidad (ej. una matriz de 2D con un vector de 1D) directamente, se producirá un error de tipo `ValueError`.

---

## 4. Integración en Pandas

Pandas proporciona métodos robustos para combinar DataFrames según la estructura requerida:

### 4.1 Concatenación (`pd.concat()`)
Permite apilar DataFrames física y lógicamente.

* **Vertical (`axis=0`):** Apila los DataFrames uno sobre otro. Si las columnas no coinciden exactamente, se generan valores nulos (`NaN`) donde no hay correspondencia.
* **Horizontal (`axis=1`):** Une los DataFrames lado a lado.
* **`ignore_index=True`:** Parámetro opcional para resetear el índice en el DataFrame resultante, evitando conflictos cuando los índices originales no son representativos en la nueva estructura.

### 4.2 Combinación mediante Claves (`merge()`)
Método equivalente a los "joins" de bases de datos SQL, combinando DataFrames basándose en columnas comunes (claves).

* **Tipos de Join:**
    * **Inner Join:** Conserva solo las filas con correspondencia en ambos DataFrames.
    * **Outer Join:** Conserva todas las filas de ambos, rellenando con `NaN` las faltantes.
    * **Left Join:** Conserva todas las filas del DataFrame izquierdo y las coincidentes del derecho.
    * **Right Join:** Conserva todas las filas del DataFrame derecho y las coincidentes del izquierdo.

### 4.3 Combinación por Índices (`join()`)
Similar al `merge()`, pero optimizado para combinar DataFrames utilizando sus índices como claves de unión. Es una forma simplificada de realizar un *left join* por defecto.