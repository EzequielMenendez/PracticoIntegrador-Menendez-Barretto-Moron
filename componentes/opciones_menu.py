from componentes.funciones import *

#Función para ver países
def ver_paises(paises):
    """
        Recibe una lista de paises y los recorre para listarlos
    """
    titulo("LISTA DE PAÍSES:")
    for pais in paises:
        print(f"{pais['nombre']} - {pais['poblacion']} habitantes - {pais['superficie']} km2 - {pais['continente']}")
    tecla_para_continuar()

#Función para buscar un país
def buscar_pais(paises, nombre_buscado):
    """
        Recibe una lista de paises y la busqueda del nombre del país.
        Recorre la lista de los paises y busca si el nombre coincide.
        Muestra las coincidencias.
    """
    titulo(f"BUSCANDO PAÍSES... '{nombre_buscado}'")
    encontrados = []
    for pais in paises:
        if nombre_buscado.lower() in pais['nombre'].lower():
            encontrados.append(pais)
    if len(encontrados) == 0:
        print("No se encontraron países.")
        tecla_para_continuar()
    else:
        listar_paises(encontrados)

#Función que muestra el menú para filtrar países
def menu_filtrar(paises):
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

def menu_ordenar(paises):
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

#Función para mostrar estadisticas
def mostrar_estadisticas(paises):
    """
        Recibe la lista de paises
        Calcula las diferentes estadicticas y muestra los resultados
    """
    titulo("ESTADÍSTICAS:")

    mayor_pob = paises[0]
    menor_pob = paises[0]
    total_pob = 0
    total_sup = 0
    contador_continentes = {}

    for pais in paises:
        # Calcular mayor y menor
        if pais['poblacion'] > mayor_pob['poblacion']:
            mayor_pob = pais
        if pais['poblacion'] < menor_pob['poblacion']:
            menor_pob = pais

        # Sumar para promedios
        total_pob += pais['poblacion']
        total_sup += pais['superficie']

        # Contar por continente
        cont = pais['continente']
        if cont in contador_continentes:
            contador_continentes[cont] += 1
        else:
            contador_continentes[cont] = 1

    promedio_pob = total_pob / len(paises)
    promedio_sup = total_sup / len(paises)

    print(f"País con mayor población: {mayor_pob['nombre']} ({mayor_pob['poblacion']})")
    print(f"País con menor población: {menor_pob['nombre']} ({menor_pob['poblacion']})")
    print(f"Promedio de población: {promedio_pob:.0f}")
    print(f"Promedio de superficie: {promedio_sup:.0f}")
    print("\nCantidad de países por continente:")
    for c, cantidad in contador_continentes.items():
        print(f"{c}: {cantidad}")
    tecla_para_continuar()