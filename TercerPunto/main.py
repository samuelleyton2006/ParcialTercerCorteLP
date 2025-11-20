from ProductoPuntoLexer import ProductoPuntoLexer
from ProductoPuntoParser import ProductoPuntoParser
from antlr4 import InputStream, CommonTokenStream
import ast

def leer_matrices(archivo):
    with open(archivo, "r") as f:
        lineas = f.read().splitlines()
    if len(lineas) < 2:
        print("Error: Se necesitan dos matrices en el archivo.")
        return None, None
    return lineas[0], lineas[1]

def convertir_a_lista(texto):
    # Convierte string de matriz en lista de Python
    try:
        return ast.literal_eval(texto)
    except:
        print(f"Error: Formato inválido en la matriz: {texto}")
        return None

def producto_punto(mat1, mat2):
    # Verifica dimensiones
    if len(mat1[0]) != len(mat2):
        print("Error: Dimensiones incompatibles para producto punto.")
        return None
    resultado = []
    for fila in mat1:
        nueva_fila = []
        for col in range(len(mat2[0])):
            suma = 0
            for k in range(len(mat2)):
                suma += fila[k] * mat2[k][col]
            nueva_fila.append(suma)
        resultado.append(nueva_fila)
    return resultado

def main():
    archivo = "matrices.txt"
    print(f"[INFO] Leyendo matrices desde '{archivo}'...")
    mat1_text, mat2_text = leer_matrices(archivo)
    
    if not mat1_text or not mat2_text:
        return
    
    print(f"[INFO] Primera matriz: {mat1_text}")
    print(f"[INFO] Segunda matriz: {mat2_text}")
    
    # Concatenamos con el operador '*' como espera la gramática
    entrada = f"{mat1_text} * {mat2_text}"
    print(f"[INFO] Entrada para ANTLR: {entrada}")
    
    # ANTLR Parsing
    input_stream = InputStream(entrada)
    lexer = ProductoPuntoLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ProductoPuntoParser(stream)
    
    print("[INFO] Iniciando parseo...")
    try:
        parser.program()  # 'program' es la regla inicial
        print("[INFO] Parseo completado correctamente.")
    except Exception as e:
        print("[ERROR] La entrada no cumple la gramática.")
        print(e)
        return
    
    # Convertir a listas de Python
    mat1 = convertir_a_lista(mat1_text)
    mat2 = convertir_a_lista(mat2_text)
    if mat1 is None or mat2 is None:
        return
    
    print("[INFO] Calculando producto punto...")
    resultado = producto_punto(mat1, mat2)
    
    if resultado is not None:
        print("[RESULTADO] Producto punto:")
        for fila in resultado:
            print(fila)

if __name__ == "__main__":
    main()