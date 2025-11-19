# Reglas Semánticas del ETDS

## CREATE TABLE

```
<create_stmt> → "CREATE" "TABLE" id "(" <column_defs> ")"
SEM:
  SymbolTable[id.lex] ← <column_defs>.columns^S
  <create_stmt>.schema^S ← SymbolTable[id.lex]
```

```
<column_defs> → <column_def> <column_defs_tail>
SEM:
  <column_defs>.columns^S ← [<column_def>.col^S] + <column_defs_tail>.columns^S
```

## INSERT

```
<insert_stmt> → "INSERT" "INTO" id "VALUES" "(" <values> ")"
SEM:
  schema ← SymbolTable[id.lex]
  verificar tamaños(schema) == tamaños(<values>.vals^S)
  <insert_stmt>.row^S ← <values>.vals^S
```

## SELECT

```
<select_stmt> → "SELECT" <column_list> "FROM" id <where_opt>
SEM:
  schema ← SymbolTable[id.lex]
  columnas ← (<column_list>.cols^S == "*") ? schema : <column_list>.cols^S
  validar columnas ∈ schema
  resultado ← filtrar(tabla, <where_opt>.filt^S)
  resultado ← proyectar(resultado, columnas)
  <select_stmt>.result^S ← resultado
```

## UPDATE

```
<update_stmt> → "UPDATE" id "SET" id "=" value <where_opt>
SEM:
  validar columna
  actualizar filas con condición
```

## DELETE

```
<delete_stmt> → "DELETE" "FROM" id <where_opt>
SEM:
  eliminar filas con la condición
```