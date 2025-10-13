#RUTA_ARCHIVO = r"C:\Users\ezeme\OneDrive\Desktop\Facultad\Python\PracticoIntegrador-Menendez-Barretto\Paises.csv" #Python ignora los caracteres de escape
RUTA_ARCHIVO = r"C:\Users\Santiago\PracticoIntegrador-Menendez-Barretto\Paises.csv" 
import csv

def leer_archivo():
    try:
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as archivo: # abre el archivo en modo lectura y utf-8 (para evitar problemas con caracteres especiales)
            paises = []
            inicio = True

            for linea in archivo:
                linea = linea.strip()
                if not inicio:  # salta el encabezado
                    nombre, poblacion, superficie, continente = linea.split(",")
                    paises.append({
                        "nombre": nombre, #str | clave
                        "poblacion": int(poblacion), #int | clave
                        "superficie": int(superficie), #int | clave
                        "continente": continente #str | clave
                    })
                inicio = False

            return paises

    except FileNotFoundError:
        print(f"Error: no se encontró el archivo '{RUTA_ARCHIVO}'. Verificá la ruta o el nombre.")
        return []  # devuelve lista vacia para que no se cierre el programa
    except PermissionError:
        print(f"Error: no tenés permisos para leer el archivo '{RUTA_ARCHIVO}'.")
        return []
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return []
    finally:
        try:
            archivo.close()
        except NameError:
            pass

        