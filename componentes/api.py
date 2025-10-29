from componentes.funciones import *
from urllib.error import HTTPError, URLError # Para manejar errores de API
from http.client import IncompleteRead # Para errores de lectura
import urllib.request
import json

API_URL_BASE = "https://restcountries.com/v3.1"

#Función para listar todos los nombres de países de la api
def listar_nombres_paises_api():
    """
    Consulta la API y muestra una lista de todos los nombres de países
    disponibles para que el usuario sepa qué buscar.
    """
    titulo("LISTA DE PAÍSES DISPONIBLES EN LA API")
    
    url_completa = f"{API_URL_BASE}/all?fields=name"
    print(f"Conectando a {url_completa}...")

    try:
        # Se hace la petición a la API
        with urllib.request.urlopen(url_completa) as respuesta:
            datos_bytes = respuesta.read()
            datos_string = datos_bytes.decode('utf-8')
            datos_api_lista = json.loads(datos_string)

    except HTTPError as e:
        print(f"Error HTTP al consultar la API: {e.code} {e.reason} 🔴")
        tecla_para_continuar()
        return
    except URLError as e:
        print(f"Error de conexión: No se pudo conectar a la API. {e.reason} 🔴")
        tecla_para_continuar()
        return
    except (json.JSONDecodeError, IncompleteRead):
        print("Error: La API devolvió datos corruptos. No se pudo procesar. 🔴")
        tecla_para_continuar()
        return
    except Exception as e:
        print(f"Ocurrió un error inesperado al conectar: {e} 🔴")
        tecla_para_continuar()
        return

    #Se procesa la lista de nombres
    nombres_paises = []
    for pais_api in datos_api_lista:
        nombre = pais_api.get('name', {}).get('common', 'No disponible')
        if nombre != 'No disponible':
            nombres_paises.append(nombre)
            
    # Ordenamos alfabéticamente
    nombres_paises.sort()
    
    print("\nPaíses encontrados:\n")
    for i, nombre in enumerate(nombres_paises):
        print(f"- {nombre}", end=' | ' if (i + 1) % 4 != 0 else '\n') 
        
    print(f"\n\nTotal de países disponibles en la API: {len(nombres_paises)}")

#Función que busca un país en la API
def buscar_país_api(nombre_api):
    """
        Esta función recibe un nombre y lo busca en la API.
        Formatea los datos al formato que se usa en la app.
    """
    url_completa = f"{API_URL_BASE}/name/{nombre_api}?fullText=true&fields=name,population,area,continents"

    try:
        # Hacemos la petición GET a la API
        with urllib.request.urlopen(url_completa) as respuesta:
            datos_bytes = respuesta.read()
            datos_string = datos_bytes.decode('utf-8')
            datos_api_lista = json.loads(datos_string)
            datos_api = datos_api_lista[0]

    except HTTPError as e:
        if e.code == 404:
            print(f"Error: No se encontró el país en la API. 🔴")
        else:
            print(f"Error HTTP al consultar la API: {e.code} {e.reason} 🔴")
        tecla_para_continuar()
        return None
    except URLError as e:
        print(f"Error de conexión: No se pudo conectar. {e.reason} 🔴")
        tecla_para_continuar()
        return None
    except (json.JSONDecodeError, IncompleteRead):
        print("Error: La API devolvió datos corruptos. No se pudo procesar. 🔴")
        tecla_para_continuar()
        return None
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e} 🔴")
        tecla_para_continuar()
        return None
    
    try:
        #Se parsean los datos de la api
        nombre = datos_api.get('name', {}).get('common', 'Nombre no disponible')
        poblacion = int(datos_api.get('population', 0))
        superficie = int(datos_api.get('area', 0))
        continentes = datos_api.get('continents', ['No disponible'])
        continente = continentes[0]

        match continente:
            case "Americas" | "South America" | "North America" | "Caribbean":
                continente = "América"
            case "Africa":
                continente = "África"
            case "Europe":
                continente = "Europa"
            case "Asia":
                continente = "Asia" 
            case "Oceania":
                continente = "Oceanía"
        
        if poblacion == 0 or superficie == 0 or continente not in ("América", "Europa", "Asia", "África", "Oceanía"):
            print(f"Error: Datos de '{nombre}' incompletos en API (Pob: {poblacion}, Sup: {superficie}). No se agregará. 🔴")
            tecla_para_continuar()
            return
        
    except ValueError:
        print(f"Ocurrió un error al procesar los datos de la API: {e} 🔴")
        tecla_para_continuar()
        return None

    return {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }