from componentes.validaciones import *

RUTA_ARCHIVO = r"Paises.csv" 

def leer_archivo():
    try:
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as archivo: # abre el archivo en modo lectura y utf-8 (para evitar problemas con caracteres especiales)
            paises = []
            contador = 1
            for linea in archivo:
                pais = validar_linea(linea, contador)
                if pais:
                    paises.append(pais)
                contador += 1
            
            return paises

    except FileNotFoundError:
        print(f"Error: no se encontró el archivo '{RUTA_ARCHIVO}'. Verificá la ruta o el nombre.")
        return []
    except PermissionError:
        print(f"Error: no tenés permisos para leer el archivo '{RUTA_ARCHIVO}'.")
        return []
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return []