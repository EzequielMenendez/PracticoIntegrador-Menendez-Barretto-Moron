from componentes.funciones import *
from componentes.validaciones import *

RUTA_ARCHIVO = r"Paises.csv" 

#Función para editar un país
def editar_pais(paises):
    """
        Se le pide al usuario ingresar un país y se busca con exactitud
        En caso de existir se busca la linea donde esta en el csv
        Luego se piden los nuevos datos a modificar y se reemplazan
    """
    titulo("EDITAR PAÍS")
    #Busco el país en la lista
    pais, indice_pais = buscar_pais(paises)
    if not pais:
        tecla_para_continuar()
        return

    try:
        #Abro el archivo y leo todas las líneas
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()

        #Busco el país en el csv
        linea_editar = None
        for i, linea in enumerate(lineas):#enumerate sirve para recorrer una lista y al mismo tiempo obtener el indice
            datos = linea.strip().split(",")
            if len(datos) and datos[0].lower() == pais.lower():
                linea_editar = i
                break

        if not linea_editar:
            print("No se encontró el país en el csv.")
            tecla_para_continuar()
            return

        #Pido al usuario los nuevos datos
        print(f"Se encontró el país {pais}")
        poblacion = pedir_entero("Ingrese la nueva cantidad de población: ")
        superficie = pedir_entero("Ingrese la nueva cantidad de superficie: ")
        continente = pedir_continente("Ingrese el nuevo continente: ")

        #Actualizo la línea encontrada
        lineas[linea_editar] = f"{pais},{poblacion},{superficie},{continente}\n"

        #Reescribo el archivo
        with open(RUTA_ARCHIVO, "w", encoding="utf-8") as archivo:
            archivo.writelines(lineas)

        #Actualizo la lista de paises
        paises[indice_pais] = {
            "nombre": pais,
            "poblacion": poblacion,
            "superficie": superficie,
            "continente": continente
        }

        titulo(f"Los datos del país '{pais}' fueron actualizados correctamente.")

    except FileNotFoundError:
        print(f"Error: no se encontró el archivo '{RUTA_ARCHIVO}'. Verificá la ruta o el nombre.")
    except PermissionError:
        print(f"Error: no tenés permisos para leer el archivo '{RUTA_ARCHIVO}'.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
    tecla_para_continuar()

#Busca un país por coincidencia exacta
def buscar_pais(paises):
    """
        Pide por consola un país a buscar, y lo busca por coincidencia exacta
        Devuelve el nombre del país y su índice
    """
    busqueda = input("Ingrese el nombre del país a editar: ")
    indice_encontrado = None
    pais_encontrado = None

    for i, pais in enumerate(paises):
        if busqueda.lower() == pais['nombre'].lower():
            indice_encontrado = i
            pais_encontrado = pais['nombre']
            break

    if not indice_encontrado:
        print(f"No se encontró el país {busqueda}.")

    return pais_encontrado, indice_encontrado