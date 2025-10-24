from componentes.funciones import *
from componentes.validaciones import *
from componentes.lector_archivos import RUTA_ARCHIVO

#Función para eliminar un país
def eliminar_pais(paises):
    """
        Se le pide al usuario ingresar un país y se busca con exactitud
        En caso de existir se busca la linea donde esta en el csv
        Luego se reescribe el csv sin esa linea y se elimina de la lista de paises
    """
    titulo("ELIMINAR PAÍS")
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
        linea_eliminar = buscar_linea(lineas, pais)
        if not linea_eliminar:
            print("No se encontró el país en el csv.")
            tecla_para_continuar()
            return

        #Elimino la linea encontrada
        del lineas[linea_eliminar]

        #Reescribo el archivo
        with open(RUTA_ARCHIVO, "w", encoding="utf-8") as archivo:
            archivo.writelines(lineas)

        #Actualizo la lista de paises
        del paises[indice_pais]

        titulo(f"El país '{pais}' se elimino correctamente.")

    except FileNotFoundError:
        print(f"Error: no se encontró el archivo '{RUTA_ARCHIVO}'. Verificá la ruta o el nombre.")
    except PermissionError:
        print(f"Error: no tenés permisos para leer el archivo '{RUTA_ARCHIVO}'.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
    tecla_para_continuar()