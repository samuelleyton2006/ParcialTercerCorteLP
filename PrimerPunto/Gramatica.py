def get_grammar():
    return """
<consulta> ::= SELECT <columnas> FROM <tabla> <condicion>
<columnas> ::= * | <lista_columnas>
<lista_columnas> ::= <columna> | <columna> , <lista_columnas>
<columna> ::= ID
<tabla> ::= ID
<condicion> ::= WHERE <expresion> | ε
<expresion> ::= <columna> <operador> <valor>
<operador> ::= = | > | < | >= | <=
<valor> ::= NUM | TEXTO
"""