#RUTA_ARCHIVO = r"C:\Users\ezeme\OneDrive\Desktop\Facultad\Python\PracticoIntegrador-Menendez-Barretto\Paises.csv" #Python ignora los caracteres de escape
RUTA_ARCHIVO = r"C:\Users\Santiago\PracticoIntegrador-Menendez-Barretto\Paises.csv"

def leer_archivo():
    try:
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
            paises = []
            inicio = True

            for linea in archivo:
                linea = linea.strip()
                if not inicio:  # salta el encabezado
                    nombre, poblacion, superficie, continente = linea.split(";")
                    paises.append({
                        "nombre": nombre,
                        "poblacion": int(poblacion),
                        "superficie": int(superficie),
                        "continente": continente
                    })
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


# Prueba
paises = leer_archivo()
for p in paises:
    print(p)