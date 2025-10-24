from componentes.funciones import *
from componentes.validaciones import *
from componentes.lector_archivos import RUTA_ARCHIVO

#Función para agregar un nuevo país
def nuevo_pais(paises):
    """
        Pide por consola los datos: nombre, poblacion, superficie y continente para crear un nuevo país
    """
    titulo("AGREGAR NUEVO PAÍS")
    #Pido y valido los datos de un país
    nombre = pedir_pais("Ingrese el nombre del país: ", paises)
    poblacion = pedir_entero("Ingrese la cantidad de población: ")
    superficie = pedir_entero("Ingrese la cantidad de superficie: ")
    continente = pedir_continente("Ingrese el continente: ")

    try:
        #Abro el archivo y agrego la nueva linea
        with open(RUTA_ARCHIVO, "a", encoding="utf-8") as archivo:
            archivo.write(f"{nombre},{poblacion},{superficie},{continente}\n")
    except FileNotFoundError:
        print(f"Error: no se encontró el archivo '{RUTA_ARCHIVO}'. Verificá la ruta o el nombre.")
        return
    except PermissionError:
        print(f"Error: no tenés permisos para leer el archivo '{RUTA_ARCHIVO}'.")
        return
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return
    
    pais_creado = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }
    #Muestro el país creado y lo añado a la lista de países
    titulo("PAÍS CREADO EXÍTOSAMENTE")
    listar_paises([pais_creado])
    paises.append(pais_creado)
    tecla_para_continuar()