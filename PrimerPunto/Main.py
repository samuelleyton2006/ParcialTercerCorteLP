from Gramatica import get_grammar
from AtributosNoTerminales import get_attributes
from ReglasSemanticas import get_semantic_rules
from Funcion import ejecutar_modelado_completo

def menu():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1. Imprimir gramática")
        print("2. Imprimir atributos")
        print("3. Imprimir reglas semánticas")
        print("4. Funcion ")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n=== GRAMÁTICA ===")
            print(get_grammar())

        elif opcion == "2":
            print("\n=== ATRIBUTOS ===")
            print(get_attributes())

        elif opcion == "3":
            print("\n=== REGLAS SEMÁNTICAS ===")
            print(get_semantic_rules())

        elif opcion == "4":
            print(ejecutar_modelado_completo())

        elif opcion == "5":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida, intente nuevamente.")

if __name__ == "__main__":
    menu()