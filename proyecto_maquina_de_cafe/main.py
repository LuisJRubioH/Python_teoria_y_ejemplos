from menu import mostrar_menu
from pedidos import pedir_cafe
from historial import ver_historial

def main():

    while True:
        mostrar_menu()
        opcion = input("seleccciona una opción: ")

        if opcion == "1":
            pedir_cafe()   
        if opcion == "2":
            ver_historial()
        elif opcion == "3":
            print("\n Muchas gracias por preferirnos")
            break
        else:
            print("Opción ináluida. Por favor indique una de las opciones sugeridas")

if __name__  == "__main__":
    main()