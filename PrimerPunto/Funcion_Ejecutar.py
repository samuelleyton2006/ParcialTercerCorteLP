# Función de evaluación basada en gramática de atributos
# Simula la ejecución semántica del lenguaje SQL simplificado

def filtrar(datos, condicion):
    if condicion is None:
        return datos
    col, val = condicion
    return [fila for fila in datos if fila[col] == val]

def proyectar(datos, columnas):
    if columnas == "*":
        return datos
    return [{col: fila[col] for col in columnas} for fila in datos]

def ejecutar(operacion, tablaSimbolos, atributos=None):
    """
    operacion: AST ya analizado y con atributos semánticos
    tablaSimbolos: dict con todas las tablas
    """
    
    tipo = operacion["tipo"]

    # CREATE TABLE
    if tipo == "CREATE":
        nombre = operacion["nombre"]
        columnas = operacion["columnas"]
        tablaSimbolos[nombre] = {
            "schema": columnas,
            "datos": []
        }
        return f"Tabla {nombre} creada."

    # INSERT
    if tipo == "INSERT":
        nombre = operacion["nombre"]
        valores = operacion["valores"]
        tablaSimbolos[nombre]["datos"].append(valores)
        return "Fila insertada."

    # SELECT
    if tipo == "SELECT":
        nombre = operacion["nombre"]
        columnas = operacion["columnas"]
        where = operacion["where"]

        datos = tablaSimbolos[nombre]["datos"]
        filtrados = filtrar(datos, where)
        proyectados = proyectar(filtrados, columnas)

        return proyectados

    # UPDATE
    if tipo == "UPDATE":
        nombre = operacion["nombre"]
        colObjetivo = operacion["col"]
        nuevoValor = operacion["valor"]
        where = operacion["where"]

        datos = tablaSimbolos[nombre]["datos"]

        for fila in datos:
            if where is None or fila[where[0]] == where[1]:
                fila[colObjetivo] = nuevoValor

        return "Filas actualizadas."

    # DELETE
    if tipo == "DELETE":
        nombre = operacion["nombre"]
        where = operacion["where"]

        datos = tablaSimbolos[nombre]["datos"]

        tablaSimbolos[nombre]["datos"] = [
            fila for fila in datos
            if not (where and fila[where[0]] == where[1])
        ]

        return "Filas eliminadas."