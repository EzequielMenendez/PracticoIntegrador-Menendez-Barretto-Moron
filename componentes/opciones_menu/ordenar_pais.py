from componentes.funciones import *

def menu_ordenar(paises):
    if sin_paises(paises):
        return
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
                ordenar_paises(paises, "poblacion")
                break

            case "3": # Ordenar por superficie
                ordenar_paises(paises, "superficie")
                break

            case "0": # Volver al menu principal
                print("Volviendo al menú...")
                break

            case _: # Ejecuta si no se cumplio ninguno de los anteriores 
                print("Acción invalida 🔴")

#Función para ordenar países
def ordenar_paises(paises, tipo):
    """
        Recibe una lista de paises, el tipo de ordenamiento y si el orden es descendente o no
        Evalua el tipo de ordenamiento y realiza el ordenamiento según el descendente
    """
    titulo(f"ORDENANDO POR {tipo.upper()}...")

    descendente = input("Ingrese '1' si quiere un orden descendente o cualquier otra tecla si quiere orden ascendente: ")
    descendente = descendente == "1"

    # Copiamos la lista para no modificar la original
    lista_ordenada = paises.copy()
    # key=lambda es una funcion anonima que toma un parametro p (país) y devuelve p['nombre'], se usa en diccionarios.
    lista_ordenada.sort(key=lambda p: p[tipo], reverse=descendente) # Ordena alfabeticamente por según el tipo

    listar_paises(lista_ordenada)
    tecla_para_continuar()