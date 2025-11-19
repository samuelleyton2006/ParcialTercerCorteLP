grammar ProductoPunto;

// --- REGLA INICIAL ---
program
    : declaracionMatrices operacion EOF
    ;

// --- DECLARACIÓN DE MATRICES ---
declaracionMatrices
    : matrizA matrizB
    ;

matrizA
    : 'matrizA' '=' listaFilas
    ;

matrizB
    : 'matrizB' '=' listaFilas
    ;

// --- MATRICES Y FILAS ---
listaFilas
    : '[' fila (',' fila)* ']'
    ;

fila
    : '[' listaNum ']'
    ;

listaNum
    : NUM (',' NUM)*
    ;

// --- OPERACIÓN ---
operacion
    : 'producto' '(' 'matrizA' ',' 'matrizB' ')'
    ;

// --- TOKENS ---
NUM : [0-9]+ ;

WS : [ \t\r\n]+ -> skip ;