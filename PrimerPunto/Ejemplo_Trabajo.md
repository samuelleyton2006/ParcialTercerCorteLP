# Ejemplo Completo con Flujo de Atributos

## Instrucción de entrada

```
SELECT nombre, edad FROM Personas WHERE id = 5
```

## Atributos calculados

- `<column_list>.cols^S = ["nombre", "edad"]`
- `<where_opt>.filt^S = ("id", 5)`
- `schema = ["id", "nombre", "edad"]`

## Datos en la tabla

```python
Personas = [
    {"id":1,"nombre":"Carlos","edad":19},
    {"id":5,"nombre":"Samuel","edad":22},
    {"id":7,"nombre":"Maria","edad":30}
]
```

## Evaluación semántica

1. Se filtran filas donde `id == 5`.
2. Se proyectan columnas `nombre` y `edad`.

## Resultado final

```
[ {"nombre":"Samuel", "edad":22} ]
```