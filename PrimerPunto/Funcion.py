def ejecutar_modelado_completo():
    """
    Esta función modela una gramática de atributos completa
    para un mini lenguaje SQL CRUD. Genera dinámicamente:

    - Gramática
    - Atributos por símbolo
    - Reglas semánticas

    Y retorna todo como un texto formateado.
    """

    # =============================
    # 1. GRAMÁTICA
    # =============================
    gramatica = """
<sentencia> ::= <create> | <read> | <update> | <delete>

<create> ::= CREATE TABLE ID '(' <columnas> ')'
<columnas> ::= <columna> | <columna> ',' <columnas>
<columna> ::= ID <tipo>

<tipo> ::= INT | TEXT

<read> ::= SELECT <lista_sel> FROM ID <cond>
<lista_sel> ::= * | <id_lista>
<id_lista> ::= ID | ID ',' <id_lista>

<update> ::= UPDATE ID SET <asignaciones> <cond>
<asignaciones> ::= <asig> | <asig> ',' <asignaciones>
<asig> ::= ID '=' <valor>

<delete> ::= DELETE FROM ID <cond>

<cond> ::= WHERE ID <op> <valor> | ε
<op> ::= '=' | '>' | '<'
<valor> ::= NUM | TEXTO
"""

    # =============================
    # 2. ATRIBUTOS
    # =============================
    atributos = """
Atributos:

sentencia:
 - tipo
 - resultado

create:
 - tabla.name
 - columnas.lista

read:
 - campos
 - tabla.name
 - filtro

update:
 - tabla.name
 - asignaciones
 - filtro

delete:
 - tabla.name
 - filtro

columna:
 - name
 - tipo

valor:
 - tipo
 - literal
"""

    # =============================
    # 3. REGLAS SEMÁNTICAS
    # =============================
    reglas = """
Reglas Semánticas:

1. columna → ID tipo
    columna.name = ID.lexema
    columna.tipo = tipo.lexema

2. columnas → columna
    columnas.lista = [columna]

3. columnas → columna , columnas1
    columnas.lista = [columna] + columnas1.lista

4. read → SELECT lista_sel FROM ID cond
    read.campos = lista_sel.lista
    read.tabla.name = ID.lexema
    read.filtro = cond.filtro

5. update → UPDATE ID SET asignaciones cond
    update.tabla.name = ID.lexema
    update.asignaciones = asignaciones.lista
    update.filtro = cond.filtro

6. delete → DELETE FROM ID cond
    delete.tabla.name = ID.lexema
    delete.filtro = cond.filtro

7. cond → WHERE ID op valor
    cond.filtro = (ID.lexema, op.lexema, valor.literal)
"""

    # ENSAMBLAR TODO
    resultado = "\n=== MODELO DE GRAMÁTICA DE ATRIBUTOS PARA SQL CRUD ===\n\n"
    resultado += "--------------- GRAMÁTICA ---------------\n"
    resultado += gramatica + "\n"
    resultado += "--------------- ATRIBUTOS ---------------\n"
    resultado += atributos + "\n"
    resultado += "----------- REGLAS SEMÁNTICAS -----------\n"
    resultado += reglas + "\n"

    return resultado