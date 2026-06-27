# Fundamentos de Python: Estructuras de Datos y Comprensiones

## 1. Estructuras de Datos Integradas

Python ofrece diversas estructuras de datos nativas que permiten almacenar, organizar y manipular colecciones de información de manera eficiente. La elección de la estructura adecuada es fundamental para optimizar el rendimiento en el análisis de grandes volúmenes de datos.

### 1.1 Listas
Las listas son colecciones ordenadas y mutables. Son altamente versátiles debido a su capacidad para modificar su contenido en tiempo de ejecución.

* **Mutabilidad:** Sus elementos pueden ser agregados, eliminados o modificados después de la creación.
* **Heterogeneidad:** Permiten almacenar diferentes tipos de datos simultáneamente (enteros, cadenas, flotantes, e incluso otras estructuras).
* **Duplicidad:** Admiten elementos con valores repetidos en diferentes posiciones (índices).

```python
mi_lista = [1, 2, 3, "cuatro", 5.0]
mi_lista.append(6) # Agrega un nuevo elemento al final
print(mi_lista)    # Salida: [1, 2, 3, 'cuatro', 5.0, 6]
```

### 1.2 Tuplas
Las tuplas comparten similitudes con las listas al ser colecciones ordenadas y heterogéneas, pero se distinguen por una característica restrictiva clave: su inmutabilidad.

* **Inmutabilidad:** Una vez definida la tupla, sus elementos no pueden ser alterados, agregados ni eliminados.
* **Casos de Uso:** Ideales para proteger la integridad de datos constantes que no deben sufrir modificaciones durante el flujo del programa (por ejemplo, coordenadas geográficas o configuraciones estáticas).

```python
mi_tupla = (1, 2, 3, "cuatro")
# mi_tupla[0] = 10  # Esta operación generaría un error (TypeError)
print(mi_tupla)     # Salida: (1, 2, 3, 'cuatro')
```

### 1.3 Diccionarios
Los diccionarios estructuran la información mediante asociaciones de pares `clave: valor`. 

* **Estructura Clave-Valor:** Cada valor almacenado es accesible de forma directa e indexada mediante su clave asignada, permitiendo búsquedas rápidas.
* **Unicidad de Claves:** No se permiten claves duplicadas dentro de un mismo diccionario. Si se asigna un valor a una clave existente, el valor anterior se sobrescribe.
* **Mutabilidad:** Es posible agregar, modificar y eliminar pares una vez inicializado el diccionario.

```python
mi_diccionario = {"nombre": "Juan", "edad": 30}
mi_diccionario["profesion"] = "Ingeniero" # Agrega un nuevo par clave-valor
mi_diccionario["edad"] = 31               # Modifica el valor existente
print(mi_diccionario) # Salida: {'nombre': 'Juan', 'edad': 31, 'profesion': 'Ingeniero'}
```

### 1.4 Conjuntos (Sets)
Los conjuntos son colecciones no ordenadas de elementos estrictamente únicos.

* **Unicidad:** No admiten elementos duplicados. Al intentar insertar un duplicado, este es descartado automáticamente.
* **Operaciones Matemáticas:** Optimizados para evaluar membresía y ejecutar operaciones de teoría de conjuntos (uniones, intersecciones y diferencias).

```python
mi_conjunto = {1, 2, 3, 3, 4}
print(mi_conjunto) # Salida: {1, 2, 3, 4} (se elimina el '3' duplicado)

mi_conjunto.add(5) # Agrega un nuevo elemento
print(mi_conjunto) # Salida: {1, 2, 3, 4, 5}
```

---

## 2. Herramientas Avanzadas de Funciones y Colecciones

Para maximizar el rendimiento de las estructuras de datos, Python provee mecanismos sintácticos que favorecen la legibilidad, la concisión y la eficiencia del código.

### 2.1 Funciones Lambda
Las funciones lambda son estructuras anónimas (sin nombre definido mediante `def`) y de formato compacto, diseñadas para ejecutar operaciones lógicas en una única línea.

* **Aplicación:** Son frecuentemente combinadas con funciones de orden superior como `map()` y `filter()` para aplicar transformaciones rápidas sobre iterables.

```python
suma = lambda x, y: x + y
print(suma(5, 3)) # Salida: 8
```

### 2.2 List Comprehension (Comprensión de Listas)
Proporciona una sintaxis elegante y optimizada para generar nuevas listas a partir de colecciones existentes, aplicando transformaciones o filtros condicionales en su construcción.

* **Ventajas:** Reduce drásticamente las líneas de código (reemplazando bucles `for` extensos), incrementa la velocidad de ejecución y mejora la claridad semántica.

```python
numeros = [1, 2, 3, 4, 5]
cuadrados = [x**2 for x in numeros]
print(cuadrados) # Salida: [1, 4, 9, 16, 25]
```

### 2.3 Dict Comprehension (Comprensión de Diccionarios)
Mecanismo homólogo a la comprensión de listas, pero orientado a la construcción dinámica de diccionarios. Permite transformar y mapear datos directamente en pares `clave: valor`.

```python
numeros = [1, 2, 3, 4, 5]
cuadrados_dict = {x: x**2 for x in numeros}
print(cuadrados_dict) # Salida: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```