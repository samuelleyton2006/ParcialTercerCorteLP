# Parcial Tercer Corte Lenguajes de Programación

------------------------------------------------------------------------

## 📘 Descripción General

Este proyecto desarrolla los **tres puntos solicitados oficialmente** en
la tarea final de Lenguajes de Programación.

Cada punto aborda un componente central de la teoría de lenguajes
formales: - Gramáticas libres de contexto - Gramáticas de atributos -
Implementación práctica en ANTLR4 - Procesamiento de lenguajes con
Python

------------------------------------------------------------------------

# ✔️ PUNTO 1 --- Función que genera una Gramática de Atributos para un Lenguaje SQL (CRUD)

El primer punto consiste en **modelar una función** que genere una
**gramática de atributos** diseñada para un lenguaje simple basado en
operaciones SQL (CRUD):

-   Create
-   Read
-   Update
-   Delete

La función implementada imprime:

-   La gramática GIC del lenguaje SQL básico\
-   Los atributos de los no terminales\
-   Las reglas semánticas

Esta función se ejecuta desde el menú del programa principal.

------------------------------------------------------------------------

# ✔️ PUNTO 2 --- Gramática para un Lenguaje que Realiza Producto Punto entre Dos Matrices

Se diseñó una **GIC** para un lenguaje que permita representar el
**producto punto** entre matrices.

### Gramática:

    <program>        → <matrix> "*" <matrix>
    <matrix>         → "[" <rows> "]"
    <rows>           → <row> | <row> "," <rows>
    <row>            → "[" <nums> "]"
    <nums>           → NUM | NUM "," <nums>
    NUM              → entero positivo o negativo

### Ejemplo válido:

    [[1,2,3],[4,5,6]] * [[7],[8],[9]]

------------------------------------------------------------------------

# ✔️ PUNTO 3 --- Implementación en ANTLR4 (Python)

Para implementar esta gramática:

    ProductoPunto.g4

Se generó el parser con:

    antlr4 -Dlanguage=Python3 ProductoPunto.g4

Archivos generados:

-   ProductoPuntoLexer.py\
-   ProductoPuntoParser.py\
-   ProductoPuntoListener.py\
-   ProductoPunto.tokens

El archivo `main.py` ejecuta el proceso de parsing.

------------------------------------------------------------------------

# 📂 Estructura del Proyecto

    ProyectoLenguajes/
    │
    ├── Gramatica.txt
    ├── AtributosNoTerminales.txt
    ├── ReglasSemanticas.txt
    │
    ├── Funcion.py
    ├── Main.py
    │
    ├── ProductoPunto.g4
    ├── ProductoPuntoLexer.py
    ├── ProductoPuntoParser.py
    ├── ProductoPuntoListener.py
    └── ProductoPunto.tokens

------------------------------------------------------------------------

# 🏁 Conclusión

Este proyecto combina teoría formal con herramientas prácticas,
cumpliendo los tres puntos del trabajo final.
