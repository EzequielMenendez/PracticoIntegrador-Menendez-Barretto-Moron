from componentes.lector_archivos import leer_archivo
from componentes.funciones import *

paises = leer_archivo()

def menu():
    print(f"Se cargaron {len(paises)} países correctamente.")
    while True:
        separador()
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
        if opcion == "1":
            separador()
            ver_paises(paises)
            tecla_para_continuar()
        elif opcion == "2":
            separador()
            buscar_pais(paises, input("Ingrese el nombre del país a buscar: "))
            tecla_para_continuar()
        elif opcion == "3":
            while True:
                separador()
                imprimir_lista([
                    "Filtar países por:",
                    "1. Continente",
                    "2. Rango de población",
                    "3. Rango de superficie",
                    "0. Volver al menú"
                ])

                opcion_filtro = input("Ingrese el filtro a aplicar: ")
                if opcion_filtro == "1":
                    while True:
                        separador()
                        imprimir_lista([
                            "CONTINENTES:",
                            "1. América",
                            "2. Europa",
                            "3. Asia",
                            "4. África",
                            "5. Oceanía"
                        ])
                        continentes= {1: "América", 2: "Europa", 3: "Asia", 4: "África", 5: "Oceanía"}
                        opcion_continente = int(input("Ingrese el continente a filtrar: "))
                        if opcion_continente >= 1 or opcion_continente <= 5:
                            continente = continentes[opcion_continente]
                            filtrar_por_continente(paises, continente)
                            tecla_para_continuar()
                            break
                        print("Opción invalida")
                    break
                elif opcion_filtro == "2":
                    filtrar_por_poblacion(paises, int(input("Ingrese la población mínima: ")), int(input("Ingrese la población máxima: "))) # despues validar con try except
                    tecla_para_continuar()
                    break
                elif opcion_filtro == "3":
                    filtrar_por_superficie(paises, int(input("Ingrese la superficie mínima: ")), int(input("Ingrese la superficie máxima: ")))
                    tecla_para_continuar()
                    break
                elif opcion_filtro == "0":
                    print("Volviendo al menú...")
                    break
                else:
                    print("Acción invalida")
        elif opcion == "4":
            while True:
                separador()
                imprimir_lista([
                    "Ordenar países por:",
                    "1. Nombre",
                    "2. Población",
                    "3. Superficie",
                    "0. Volver al menú"
                ])

                opcion_ordenar = input("Ingrese el ordenamiento a aplicar: ")
                if opcion_ordenar == "1":
                    ordenar_paises(paises, "nombre")
                    tecla_para_continuar()
                    break
                elif opcion_ordenar == "2":
                    descendente = input("Ingrese 1 si quiere un orden descendente o cualquier otra tecla si quiere orden ascendente: ")
                    descendente = descendente == "1"
                    ordenar_paises(paises, "poblacion", descendente)
                    tecla_para_continuar()
                    break
                elif opcion_ordenar == "3":
                    descendente = input("Ingrese 1 si quiere un orden descendente o cualquier otra tecla si quiere orden ascendente: ")
                    descendente = descendente == "1"
                    ordenar_paises(paises, "superficie", descendente)
                    tecla_para_continuar()
                    break
                elif opcion_ordenar == "0":
                    print("Volviendo al menú...")
                    break
                else:
                    print("Acción invalida")
        elif opcion == "5":
            separador()
            mostrar_estadisticas(paises)
            tecla_para_continuar()
        elif opcion == "0":
            print("Saliendo...")
            break
        else:
            print("Acción invalida")