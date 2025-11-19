def get_semantic_rules():
    return """
Reglas Semánticas:

1. lista_columnas → columna
    lista_columnas.list = [columna.name]

2. lista_columnas → columna , lista_columnas1
    lista_columnas.list = [columna.name] + lista_columnas1.list

3. tabla → ID
    tabla.name = ID.lexema

4. valor → NUM
    valor.tipo = "int"
    valor.literal = NUM.lexema

5. valor → TEXTO
    valor.tipo = "string"
    valor.literal = TEXTO.lexema

6. condicion → WHERE expresion
    condicion.filtro = expresion.evaluación

7. consulta → SELECT columnas FROM tabla condicion
    consulta.sql = construir_sql(columnas.list, tabla.name, condicion.filtro)
"""