from componentes.validaciones import *

RUTA_ARCHIVO = r"Paises.csv" 

def leer_archivo():
    try:
        # Abre el archivo en modo "a+" para crear si no existe y permitir leer/escribir
        with open(RUTA_ARCHIVO, "a+", encoding="utf-8") as archivo:
            archivo.seek(0) # seek hace que el cursor vuelva al inicio del archivo
            lineas = archivo.readlines()
            
            if not lineas:
                print(f"Advertencia: Archivo '{RUTA_ARCHIVO}' no encontrado o vacío. Escribiendo cabecera.")
                archivo.write("nombre,poblacion,superficie,continente\n")
                return []
            
            paises = []
            contador = 1 # iterar desde la segunda línea para ignorar cabecera.
            for linea in lineas[1:]: 
                pais = validar_linea(linea, contador, paises) # validar y crear objeto pais
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