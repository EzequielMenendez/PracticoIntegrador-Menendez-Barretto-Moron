from componentes.lector_archivos import leer_archivo
from componentes.funciones import *


paises = leer_archivo()

def menu():
    print(f"Se cargaron {len(paises)} países correctamente.")
    while True:
        print("===============================================")
        print("GESTIÓN DE PAISES")
        print("MENÚ DE OPCIONES")
        print("1. Ver todos los países.")
        print("2. Buscar un país.")
        print("3. Filtrar países.")
        print("4. Ordenar países.")
        print("5. Mostar estadisticas.")
        print("0. Salir.")

        opcion = input("Ingrese la acción que desea realizar: ")

        if opcion == "1":
            print("===============================================")
            print("Viendo países...")#Aquí va la lógica

            ver_todos(paises)

            tecla_para_continuar()#Este input lo vamos a usar para que no se repita el menu automaticamente
        elif opcion == "2":
            print("===============================================")
            print("Buscando países...")#Aquí va la lógica

            buscar_pais(paises, input("Ingrese el nombre del país a buscar: "))

            tecla_para_continuar()
        elif opcion == "3":
            while True:
                print("===============================================")
                print("Filtar países por:")
                print("1. Continente")
                print("2. Rango de población")
                print("3. Rango de superficie")
                print("0. Volver al menú")

                opcion_filtro = input("Ingrese el filtro a aplicar: ")
                if opcion_filtro == "1":
                    print("Filtrando por continente...")#Aquí va la lógica

                    filtrar_por_continente(paises, input("Ingrese el continente a filtrar: "))

                    tecla_para_continuar()
                    break
                elif opcion_filtro == "2":
                    print("Filtrando por población...")#Aquí va la lógica

                    filtrar_por_poblacion(paises, int(input("Ingrese la población mínima: ")), int(input("Ingrese la población máxima: "))) # despues validar con try except

                    tecla_para_continuar()
                    break
                elif opcion_filtro == "3":
                    print("Filtrando por superficie...")#Aquí va la lógica
                    tecla_para_continuar()
                    break
                elif opcion_filtro == "0":
                    print("Volviendo al menú...")
                    break
                else:
                    print("Acción invalida")
        elif opcion == "4":
            while True:
                print("===============================================")
                print("Ordenar países por:")
                print("1. Nombre")
                print("2. Población")
                print("3. Superficie")
                print("0. Volver al menú")

                opcion_ordenar = input("Ingrese el ordenamiento a aplicar: ")
                if opcion_ordenar == "1":
                    print("Ordenando por nombre...")#Aquí va la lógica

                    ordenar_paises(paises, "nombre")

                    tecla_para_continuar()
                    break
                elif opcion_ordenar == "2":
                    print("Ordenando por población...")#Aquí va la lógica

                    ordenar_paises(paises, "poblacion")

                    tecla_para_continuar()
                    break
                elif opcion_ordenar == "3":
                    print("Ordenando por superficie...")#Aquí va la lógica

                    ordenar_paises(paises, "superficie")

                    tecla_para_continuar()
                    break
                elif opcion_ordenar == "0":
                    print("Volviendo al menú...")
                    break
                else:
                    print("Acción invalida")
        elif opcion == "5":
            print("===============================================")
            print("Mostrando estadisticas...")#Aquí va la lógica

            mostrar_estadisticas(paises)

            tecla_para_continuar()
        elif opcion == "0":
            print("Saliendo...")
            break
        else:
            print("Acción invalida")