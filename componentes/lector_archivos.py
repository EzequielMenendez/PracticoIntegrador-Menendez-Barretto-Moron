RUTA_ARCHIVO = r"C:\Users\ezeme\OneDrive\Desktop\Facultad\Python\PracticoIntegrador-Menendez-Barretto\Paises.csv" #Python ignora los caracteres de escape
#RUTA_ARCHIVO = r"C:\Users\Santiago\PracticoIntegrador-Menendez-Barretto\Paises.csv"

def leer_archivo():
    try:
        # Abrimos el archivo en modo lectura
        archivo = open(RUTA_ARCHIVO, "r", encoding="utf-8")
        
        print("Contenido del archivo:\n")

        paises = []

        inicio = True
        # Recorremos línea por línea
        for linea in archivo:
            linea = linea.strip()
            if inicio == False:
                nombre, poblacion, superficie, continente = linea.split(";")
                paises.append({"nombre": nombre, "poblacion": poblacion, "superficie": superficie, "continente": continente})

            inicio = False

        return paises

    except FileNotFoundError:
        print(f"Error: no se encontró el archivo '{RUTA_ARCHIVO}'. Verificá la ruta o el nombre.")
    except PermissionError:
        print(f"Error: no tenés permisos para leer el archivo '{RUTA_ARCHIVO}'.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
    finally:
        try:
            archivo.close()
        except NameError:
            pass