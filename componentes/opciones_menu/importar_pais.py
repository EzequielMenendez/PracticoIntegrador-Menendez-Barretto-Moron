from componentes.funciones import titulo, tecla_para_continuar
from componentes.validaciones import validar_repetido
from componentes.api import *
from componentes.lector_archivos import RUTA_ARCHIVO

API_URL_BASE = "https://restcountries.com/v3.1"

#Función para importar un país desde la api
def importar_pais_api(paises):
    """
    Pide al usuario el nombre de un país, lo busca en la API 
    y, si lo encuentra y no está repetido, lo agrega al CSV y a la lista en memoria.
    """

    listar_nombres_paises_api()
    titulo("IMPORTAR PAÍS DESDE API")

    nombre = pedir_pais("Ingrese el nombre del país a importar: ", paises)
    nombre_api = nombre.replace(" ", "%20")
    
    #Se busca el país en la api
    pais = buscar_país_api(nombre_api)
    if not pais:
        return

    try:
        #Se agrega el país en el csv y en la lista
        with open(RUTA_ARCHIVO, "a", encoding="utf-8") as archivo:
            linea_csv = f"{pais['nombre']},{pais['poblacion']},{pais['superficie']},{pais['continente']}\n"
            archivo.write(linea_csv)

        paises.append(pais)

        titulo(f"PAÍS IMPORTADO Y AGREGADO EXITOSAMENTE")
        listar_paises([pais])
    except FileExistsError or FileNotFoundError:
        print("No se encontro el archivo csv.")
        return
    except Exception as e:
        print(f"Ocurrió un error al almacenar el país: {e} 🔴")
        return
    
    tecla_para_continuar()
