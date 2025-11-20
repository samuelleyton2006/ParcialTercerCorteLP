# Parcial Final — Lenguajes de Programación

---

## 📝 Punto 1: Función Generadora de Gramática de Atributos (SQL/CRUD)

El primer punto consiste en **modelar una función** que genere una **gramática de atributos** diseñada para un lenguaje simple basado en operaciones SQL (CRUD):

- **Create** — Crear registros
- **Read** — Leer/consultar datos
- **Update** — Actualizar registros
- **Delete** — Eliminar datos

### ¿Qué genera la función?

La función implementada en `Funcion.py` imprime:

1. La gramática GIC del lenguaje SQL básico
2. Los atributos de los no terminales
3. Las reglas semánticas asociadas

Esta función se ejecuta desde el menú del programa principal (`Main.py`).

### Archivos relacionados

- `Gramatica.txt` — Contiene la gramática formal
- `AtributosNoTerminales.txt` — Lista de atributos
- `ReglasSemanticas.txt` — Reglas semánticas
- `Funcion.py` — Implementación de la función generadora

---

## 🔢 Punto 2: Gramática para Producto Punto entre Matrices

Se diseñó una **gramática libre de contexto (GIC)** para un lenguaje que permita representar el **producto punto** entre dos matrices.

### Definición de la Gramática

```
<program>    → <matrix> "*" <matrix>
<matrix>     → "[" <rows> "]"
<rows>       → <row> | <row> "," <rows>
<row>        → "[" <nums> "]"
<nums>       → NUM | NUM "," <nums>
NUM          → entero positivo o negativo
```

### Ejemplo de Entrada Válida

```
[[1,2,3],[4,5,6]] * [[7],[8],[9]]
```

Esta expresión representa el producto punto entre:
- Matriz A: 2×3
- Matriz B: 3×1

---

## ⚙️ Punto 3: Implementación en ANTLR4

La gramática del Punto 2 se implementó utilizando **ANTLR4** con Python como lenguaje objetivo.

### Archivo de Gramática

```
ProductoPunto.g4
```

### Generación del Parser

Para generar los analizadores léxico y sintáctico, ejecutar:

```bash
antlr4 -Dlanguage=Python3 ProductoPunto.g4
```

### Archivos Generados

- `ProductoPuntoLexer.py` — Analizador léxico
- `ProductoPuntoParser.py` — Analizador sintáctico
- `ProductoPuntoListener.py` — Listener para recorrido del árbol
- `ProductoPunto.tokens` — Definición de tokens

### Ejecución

El archivo `main.py` ejecuta el proceso completo de parsing:

```bash
python3 main.py
```

El programa:
1. Lee la expresión del usuario
2. Realiza el análisis léxico
3. Construye el árbol sintáctico
4. Valida la corrección de la entrada

---

## 📂 Estructura del Proyecto

```
ProyectoLenguajes/
│
├── Gramatica.txt                   # Gramática SQL (CRUD)
├── AtributosNoTerminales.txt       # Atributos de los no terminales
├── ReglasSemanticas.txt            # Reglas semánticas
│
├── Funcion.py                      # Función generadora (Punto 1)
├── Main.py                         # Menú principal del proyecto
│
├── ProductoPunto.g4                # Gramática ANTLR (Punto 2)
├── ProductoPuntoLexer.py           # Lexer generado
├── ProductoPuntoParser.py          # Parser generado
├── ProductoPuntoListener.py        # Listener generado
├── ProductoPunto.tokens            # Tokens generados
└── main.py                         # Ejecutor del parser (Punto 3)
```

---

## 🛠️ Tecnologías Utilizadas

| Tecnología | Propósito |
|------------|-----------|
| **ANTLR4** (v4.13.x) | Generación de analizadores léxico y sintáctico |
| **Python 3** | Lenguaje objetivo para la implementación |
| **Gramáticas Formales** | Modelado de lenguajes y sintaxis |
| **Gramáticas de Atributos** | Especificación de semántica |

---

## 🚀 Instrucciones de Uso

### Requisitos Previos

- Python 3.x instalado
- ANTLR4 instalado y configurado
- Archivos del proyecto descargados

### Paso 1: Generar el Parser (si no existe)

```bash
antlr4 -Dlanguage=Python3 ProductoPunto.g4
```

### Paso 2: Ejecutar el Programa Principal

```bash
python3 Main.py
```

### Paso 3: Probar el Parser de Matrices

```bash
python3 main.py
```

---

## 📊 Menú del Programa Principal

Al ejecutar `Main.py`, se presenta el siguiente menú:

1. **Imprimir gramática SQL (CRUD)** — Muestra la gramática formal
2. **Imprimir lista de atributos** — Lista todos los atributos de los no terminales
3. **Imprimir reglas semánticas** — Muestra las reglas semánticas definidas
4. **Generar gramática desde función** — Ejecuta la función generadora del Punto 1
5. **Salir** — Termina la ejecución

---


---

## 🏁 Conclusión

Este proyecto combina teoría formal con herramientas prácticas, cumpliendo los tres puntos del trabajo final de Lenguajes de Programación. Demuestra comprensión profunda de gramáticas, análisis sintáctico y construcción de lenguajes mediante ANTLR4 y Python.
