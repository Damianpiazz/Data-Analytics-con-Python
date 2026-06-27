# Fundamentos de Python: Scope, Parámetros y Librerías de Datos

## 1. Alcance de las Variables (Scope)

El scope o alcance de las variables en Python determina la visibilidad y accesibilidad de una variable dentro de las diferentes partes de un programa. 

### Tipos de Scope
* **Scope Local:** Variables definidas dentro de una función, accesibles exclusivamente dentro de la misma.
* **Scope Global:** Variables definidas fuera de cualquier función, accesibles en todo el script.
* **Scope No Local (Enclosing):** Variables en un ámbito superior al de una función anidada.

### Resolución del Scope (Regla LEGB)
Python determina qué variable utilizar siguiendo este orden:
1. **Local**
2. **Enclosing (cerramiento)**
3. **Global**
4. **Built-in (nativas de Python)**

---

## 2. Tipos de Parámetros en Funciones

* **Posicionales:** Se asignan según el orden definido.
* **Por Defecto:** Poseen un valor predefinido si no se proporciona argumento.
* **Indefinidos (`*args`):** Capturan un número variable de argumentos posicionales como tupla.
* **Palabras Clave Indefinidas (`**kwargs`):** Capturan un número variable de argumentos con nombre como diccionario.

---

## 3. Introducción a Librerías de Análisis de Datos

### 3.1 NumPy (Numerical Python)
* **Estructura Principal (ndarray):** Array multidimensional altamente eficiente en memoria y velocidad.
* **Vectorización:** Permite operaciones matemáticas sobre arrays completos simultáneamente.

### 3.2 Pandas (Panel Data)
* **DataFrame:** Estructura bidimensional tabular (filas y columnas).
* **Series:** Estructura unidimensional etiquetada.
* **Uso:** Especializada en filtrado, agrupación, resumen y lectura de múltiples formatos de archivos.