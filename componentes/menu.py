from componentes.opciones_menu import *
from componentes.lector_archivos import leer_archivo

paises = leer_archivo()

def menu():
    if len(paises) == 0:
        print("No se encontraron paiíes cargados en el archivo.")
    print(f"Se cargaron {len(paises)} países correctamente.")
    while True: # Mostrar el menu principal
        imprimir_lista([
            "GESTIÓN DE PAISES",
            "MENÚ DE OPCIONES",
            "1. Ver todos los países.",
            "2. Buscar un país.",
            "3. Filtrar países.",
            "4. Ordenar países.",
            "5. Mostar estadisticas.",
            "0. Salir."
        ])

        opcion = input("Ingrese la acción que desea realizar: ")

        # Estructura de control principal del menu
        match opcion:
            case "1": # Ver todos los paises
                ver_paises(paises)
            case "2": # Buscar un pais
                buscar_pais(paises, input("Ingrese el nombre del país a buscar: "))
            case "3": # Submenu de filtros
                menu_filtrar(paises)
            case "4": # Submenu de ordenamientos
                menu_ordenar(paises)
            case "5": # Mostrar estadisticas
                mostrar_estadisticas(paises)
            case "0": # Salir del programa
                print("Saliendo... 🌐")
                break

            case _: # Ejecuta si no se cumplio ninguno de los anteriores 
                print("Acción invalida 🔴")
