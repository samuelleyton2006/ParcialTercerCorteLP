# Atributos de la Gramática SQL CRUD

## Atributos por No Terminal

| No terminal       | Atributo      | Tipo          | Función |
|------------------|---------------|---------------|---------|
| `<stmt>`         | result^S      | any           | Resultado final de la instrucción |
| `<create_stmt>`  | schema^S      | dict          | Esquema sintetizado de tabla |
| `<insert_stmt>`  | row^S         | list          | Fila lista para insertar |
| `<select_stmt>`  | result^S      | list          | Resultado de consulta |
| `<column_defs>`  | columns^S     | list          | Lista (nombre,tipo) |
| `<column_def>`   | col^S         | tuple         | Una columna con su tipo |
| `<values>`       | vals^S        | list          | Valores para INSERT |
| `<column_list>`  | cols^S        | list/"*"      | Columnas a seleccionar |
| `<where_opt>`    | filt^S        | (col,val)/None | Condición WHERE |

## Atributos Heredados Importantes

| No terminal | Atributo | Tipo | Uso |
|-------------|----------|------|-----|
| `<stmt>` | tablaSimbolos^H | dict | Base de datos |
| `<select_stmt>` | schema^H | dict | Esquema de la tabla |

## Observaciones

- Los atributos sintéticos (S) suben información.
- Los atributos heredados (H) bajan contexto semántico.