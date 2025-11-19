from antlr4 import *
from ProductoPuntoLexer import ProductoPuntoLexer
from ProductoPuntoParser import ProductoPuntoParser

def main():
    print("=== Lenguaje Producto Punto ===")
    print("Ingrese su programa (sin comillas). Ejemplo:")
    print("matrizA = [[1,2,3],[4,5,6]]")
    print("matrizB = [[7,8],[9,10],[11,12]]")
    print("producto(matrizA, matrizB)")
    print("---------------------------------------")
    print("Pegue su entrada (termine con ENTER y Ctrl+D / Ctrl+Z):")

    data = ""
    try:
        while True:
            line = input()
            data += line + "\n"
    except EOFError:
        pass

    # ANTLR: preparar input
    input_stream = InputStream(data)
    lexer = ProductoPuntoLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = ProductoPuntoParser(tokens)

    tree = parser.program()

    print("\n=== ÁRBOL PARSEADO ===")
    print(tree.toStringTree(recog=parser))

if __name__ == "__main__":
    main()