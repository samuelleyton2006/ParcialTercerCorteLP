# Proyecto Final — Lenguajes de Programación

**Autor:** Samuel Esteban Leyton  
**Fecha:** 2025

---

## 📌 Descripción General

Este proyecto desarrolla cuatro puntos fundamentales relacionados con gramáticas formales, gramáticas de atributos y su implementación práctica utilizando ANTLR4 con Python como lenguaje objetivo.

### Componentes del Proyecto

1. Función que genera una gramática de atributos para un lenguaje tipo SQL (CRUD)
2. Gramática para un lenguaje capaz de resolver el producto punto entre matrices
3. Implementación de la gramática del punto 2 en ANTLR4 (lenguaje objetivo: Python)
4. Programa en Python con menú que imprime gramática, atributos, reglas semánticas y genera automáticamente la gramática de atributos

---

## 📋 Punto 1: Generación de Gramática de Atributos (CRUD SQL)

Se diseñó una función en Python (`Funcion.py`) que genera dinámicamente una **gramática de atributos** enfocada en operaciones CRUD (Create, Read, Update y Delete) similares a SQL.

La función imprime en consola:
- Gramática BNF
- Lista de atributos sintetizados y heredados
- Reglas semánticas asociadas

**Archivos:**
- `Funcion.py` — contiene la función generadora
- `Main.py` — permite ejecutarla desde el menú (opción 4)

---

## 🔢 Punto 2: Gramática del Producto Punto entre Matrices

Se diseñó una gramática sencilla para describir un lenguaje capaz de realizar el **producto punto entre dos matrices** dadas por el usuario.

### Gramática Propuesta

```
Expresion → Matriz "*" Matriz

Matriz → "[" FilaLista "]"
FilaLista → Fila | Fila "," FilaLista
Fila → "[" NumeroLista "]"
NumeroLista → NUM | NUM "," NumeroLista

NUM → entero positivo o negativo
```

### Ejemplo de Entrada

```
[[1,2,3],[4,5,6]] * [[7],[8],[9]]
```

---

## ⚙️ Punto 3: Implementación en ANTLR4

Se creó el archivo `ProductoPunto.g4` y se generaron los analizadores léxicos y sintácticos.

### Generación del Parser

```bash
antlr4 -Dlanguage=Python3 ProductoPunto.g4
```

Esto produce:
- `ProductoPuntoLexer.py`
- `ProductoPuntoParser.py`
- `ProductoPuntoListener.py`
- `ProductoPunto.tokens`

### Ejecución

El archivo `main.py`:
- Lee la expresión del usuario
- Pasa la entrada al lexer
- Usa el parser para validar la sintaxis
- Muestra si la expresión es válida

```bash
python3 main.py
```

---

## 🖥️ Punto 4: Programa con Menú Interactivo

El archivo `Main.py` despliega un menú con las siguientes opciones:

1. Imprimir gramática SQL (CRUD)
2. Imprimir lista de atributos
3. Imprimir reglas semánticas
4. Generar gramática SQL desde la función (Punto 1)
5. Salir

Los textos se cargan desde:
- `Gramatica.txt`
- `AtributosNoTerminales.txt`
- `ReglasSemanticas.txt`

La opción 4 ejecuta la función generadora del archivo `Funcion.py`.

---

## 📂 Estructura del Proyecto

```
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
```

---

## 🛠️ Tecnologías Utilizadas

- **ANTLR4** (versión 4.13.x)
- **Python 3**
- Gramáticas libres de contexto
- Gramáticas de atributos
- Análisis léxico y parsing

---

## 🚀 Cómo Ejecutar el Proyecto

### 1. Generar el Parser (si no existe)

```bash
antlr4 -Dlanguage=Python3 ProductoPunto.g4
```

### 2. Ejecutar el Programa Principal

```bash
python3 Main.py
```

---

## ✅ Conclusión

Este proyecto demuestra el uso real de gramáticas formales, gramáticas de atributos, construcción de lenguajes y análisis sintáctico mediante ANTLR. Además, integra conceptos de teoría de lenguajes con programación práctica.
