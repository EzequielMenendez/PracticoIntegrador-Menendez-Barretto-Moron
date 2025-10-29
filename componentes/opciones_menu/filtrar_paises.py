from componentes.funciones import *

#Función que muestra el menú para filtrar países
def menu_filtrar(paises):
    if sin_paises(paises):
        return
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

#Función para filtar por continente
def filtrar_por_continente(paises, continente):
    """
        Recibe una lista de paises y el continente.
        Recorre la lista de los paises y busca si el continente coincide.
        Muestra las coincidencias.
    """
    titulo(f"PAÍSES DEL CONTINENTE: {continente}")
    encontrados = []
    for pais in paises:
        if pais['continente'].lower() == continente.lower():
            encontrados.append(pais)
    
    if len(encontrados) == 0:
        print(f"No se encontraron países en el continente {continente}.")
    else:
        listar_paises(encontrados)
    tecla_para_continuar()

#Función para filtrar por población
def filtrar_por_poblacion(paises, min_pob, max_pob):
    """
        Recibe una lista de paises, el mínimo de población, y el máximo de población
        Recorre la lista de los paises y busca los países entre el mínimo y el máximo de población
        Muestra las coincidencias.
    """
    titulo(f"PAÍSES CON POBLACION ENTRE {min_pob} Y {max_pob}")
    encontrados = []
    for pais in paises:
        if min_pob <= pais['poblacion'] <= max_pob:
            encontrados.append(pais)
    
    if len(encontrados) == 0:
        print(f"No se encontraron países con población entre {min_pob} y {max_pob}.")
    else:
        listar_paises(encontrados)
    tecla_para_continuar()

#Función para filtrar por superficie
def filtrar_por_superficie(paises, min_sup, max_sup):
    """
        Recibe una lista de paises, el mínimo de superficie, y el máximo de superficie
        Recorre la lista de los paises y busca los países entre el mínimo y el máximo de superficie
        Muestra las coincidencias.
    """
    titulo(f"PAÍSES CON UNA SUPERFICIE ENTRE {min_sup} Y {max_sup} KM2")
    encontrados = []
    for pais in paises:
        if min_sup <= pais['superficie'] <= max_sup:
            encontrados.append(pais)
    
    if len(encontrados) == 0:
        print(f"No se encontraron países con una superficie entre {min_sup} y {max_sup}.")
    else:
        listar_paises(encontrados)
    tecla_para_continuar()