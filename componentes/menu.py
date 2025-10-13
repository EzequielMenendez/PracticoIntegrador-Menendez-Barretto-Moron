from componentes.lector_archivos import leer_archivo
from componentes.funciones import *

paises = leer_archivo()

def menu():
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
                while True:
                    imprimir_lista([
                        "Filtar países por:",
                        "1. Continente",
                        "2. Rango de población",
                        "3. Rango de superficie",
                        "0. Volver al menú"
                    ])

                    opcion_filtro = input("Ingrese el filtro a aplicar: ")

                    match opcion_filtro:
                        case "1": # Filtrar por continente
                            while True:
                                imprimir_lista([
                                    "CONTINENTES:",
                                    "1. América",
                                    "2. Europa",
                                    "3. Asia",
                                    "4. África",
                                    "5. Oceanía"
                                ])
                                continentes = {
                                    1: "América",
                                    2: "Europa",
                                    3: "Asia",
                                    4: "África",
                                    5: "Oceanía"
                                }

                                try:
                                    opcion_continente = int(input("Ingrese el continente a filtrar: ")) 
                                    if 1 <= opcion_continente <= 5: # Valir que este dentro del rango 1–5
                                        continente = continentes[opcion_continente]
                                        filtrar_por_continente(paises, continente)
                                        break
                                    else:
                                        print("Opción invalida 🔴")
                                except ValueError:
                                    print("⚠️ Ingrese un número válido.")
                            break

                        case "2": # Filtrar por poblacion
                            min_pob = pedir_entero("Ingrese la población mínima: ")
                            max_pob = pedir_entero("Ingrese la población máxima: ")
                            filtrar_por_poblacion(paises, min_pob, max_pob)
                            break

                        case "3": # Filtrar por superficie
                            min_sup = pedir_entero("Ingrese la superficie mínima: ")
                            max_sup = pedir_entero("Ingrese la superficie máxima: ")
                            filtrar_por_superficie(paises, min_sup, max_sup)
                            break

                        case "0": # Volver al menu principal
                            print("Volviendo al menú...")
                            break

                        case _:
                            print("Acción invalida 🔴")

            case "4": # Submenu de ordenamientos
                while True:
                    imprimir_lista([
                        "Ordenar países por:",
                        "1. Nombre",
                        "2. Población",
                        "3. Superficie",
                        "0. Volver al menú"
                    ])

                    opcion_ordenar = input("Ingrese el ordenamiento a aplicar: ")

                    match opcion_ordenar:
                        case "1": # Ordenar por nombre
                            ordenar_paises(paises, "nombre")
                            break

                        case "2": # Ordenar por poblacion
                            descendente = input("Ingrese 1 si quiere un orden descendente o cualquier otra tecla si quiere orden ascendente: ")
                            descendente = descendente == "1"
                            ordenar_paises(paises, "poblacion", descendente)
                            break

                        case "3": # Ordenar por superficie
                            descendente = input("Ingrese 1 si quiere un orden descendente o cualquier otra tecla si quiere orden ascendente: ")
                            descendente = descendente == "1"
                            ordenar_paises(paises, "superficie", descendente)
                            break

                        case "0": # Volver al menu principal
                            print("Volviendo al menú...")
                            break

                        case _: # Ejecuta si no se cumplio ninguno de los anteriores 
                            print("Acción invalida 🔴")

            case "5": # Mostrar estadisticas
                mostrar_estadisticas(paises)

            case "0": # Salir del programa
                print("Saliendo... 🌐")
                break

            case _: # Ejecuta si no se cumplio ninguno de los anteriores 
                print("Acción invalida 🔴")
