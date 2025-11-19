def imprimir_gramatica_producto_punto():
    gramatica = """
GRAMÁTICA PARA EL PRODUCTO PUNTO ENTRE MATRICES

<Programa>        → <DeclaraciónMatrices> <Operación>

<DeclaraciónMatrices> → <MatrizA> <MatrizB>

<MatrizA>         → 'matrizA' '=' <ListaFilas>
<MatrizB>         → 'matrizB' '=' <ListaFilas>

<ListaFilas>      → '[' <Fila> {',' <Fila>} ']'
<Fila>            → '[' <ListaNum> ']'
<ListaNum>        → <num> {',' <num>}

<Operación>       → 'producto' '(' 'matrizA' ',' 'matrizB' ')'

Condiciones Semánticas:
1. Las matrices deben ser rectangulares.
2. Si A es de dimensión (m × n), B debe ser (n × p).
3. El resultado es una matriz (m × p).

Ejemplo válido:
matrizA = [[1,2,3],[4,5,6]]
matrizB = [[7,8],[9,10],[11,12]]
producto(matrizA, matrizB)
"""

    print(gramatica)


# Si quieres probar directamente:
if __name__ == "__main__":
    imprimir_gramatica_producto_punto()