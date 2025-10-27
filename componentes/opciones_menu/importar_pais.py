# Importamos las librerías NATIVAS de Python
import urllib.request
import json
from urllib.error import HTTPError, URLError # Para manejar errores de API
from http.client import IncompleteRead # Para errores de lectura

# Importamos las funciones de tu proyecto
from componentes.funciones import titulo, tecla_para_continuar
from componentes.validaciones import validar_repetido
from componentes.lector_archivos import RUTA_ARCHIVO

# --- URLs de la API ---
API_URL_BASE = "https://restcountries.com/v3.1"


# --- FUNCIÓN 1: Importar un país específico ---

def importar_pais_api(paises):

    listar_nombres_paises_api()
    """
    Pide al usuario el nombre de un país, lo busca en la API 
    y, si lo encuentra y no está repetido, lo agrega al CSV y a la lista en memoria.
    """
    titulo("IMPORTAR PAÍS DESDE API (NATIVO)")
    nombre_original = input("Ingrese el nombre del país a importar (en inglés, ej: Japan): ")
    if not nombre_original.strip():
        print("Error: El nombre no puede estar vacío. 🔴")
        tecla_para_continuar()
        return
    nombre_buscado = nombre_original.replace(" ", "%20")

    # 1. Validar que el país no exista ya en tu CSV
    if not validar_repetido(nombre_original, paises):
        print(f"Error: '{nombre_original}' ya existe en tu lista de países. 🔴")
        tecla_para_continuar()
        return

    # 2. Llamar a la API con urllib
    print(f"Buscando '{nombre_original}' en la API de restcountries...")
    
    # URL optimizada: pide solo los 4 campos necesarios
    url_completa = f"{API_URL_BASE}/name/{nombre_buscado}?fullText=true&fields=name,population,area,continents"

    try:
        # Hacemos la petición GET a la API
        with urllib.request.urlopen(url_completa) as respuesta:
            datos_bytes = respuesta.read()
            datos_string = datos_bytes.decode('utf-8')
            datos_api_lista = json.loads(datos_string)
            datos_api = datos_api_lista[0] # Tomamos el primer resultado

    # --- Manejo de Errores (la parte compleja de urllib) ---
    except HTTPError as e:
        if e.code == 404:
            print(f"Error: No se encontró el país '{nombre_original}' en la API. 🔴")
        else:
            print(f"Error HTTP al consultar la API: {e.code} {e.reason} 🔴")
        tecla_para_continuar()
        return
    except URLError as e:
        print(f"Error de conexión: No se pudo conectar. ¿Tenés internet? 🌐 ({e.reason})")
        tecla_para_continuar()
        return
    except (json.JSONDecodeError, IncompleteRead):
        print("Error: La API devolvió datos corruptos. No se pudo procesar. 🔴")
        tecla_para_continuar()
        return
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e} 🔴")
        tecla_para_continuar()
        return

    # 3. Procesar la respuesta
    try:
        # 4. Mapear los datos de la API a tu estructura simple
        nombre = datos_api.get('name', {}).get('common', 'Nombre no disponible')
        poblacion = int(datos_api.get('population', 0))
        superficie = int(datos_api.get('area', 0))
        continentes = datos_api.get('continents', ['No disponible'])
        continente = continentes[0]

        # Estandarizamos continentes con tu match
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
            # Si no es ninguno, se filtrará en la validación de abajo

        # Validar que los datos importados sean coherentes
        if poblacion == 0 or superficie == 0 or continente not in ("América", "Europa", "Asia", "África", "Oceanía"):
            print(f"Error: Datos de '{nombre}' incompletos en API (Pob: {poblacion}, Sup: {superficie}). No se agregará. 🔴")
            tecla_para_continuar()
            return
            
        # 5. Guardar en el CSV
        with open(RUTA_ARCHIVO, "a", encoding="utf-8") as archivo:
            linea_csv = f"{nombre},{poblacion},{superficie},{continente}\n"
            archivo.write(linea_csv)

        # 6. Crear el diccionario y agregarlo a la lista en memoria
        pais_creado = {
            "nombre": nombre,
            "poblacion": poblacion,
            "superficie": superficie,
            "continente": continente
        }
        paises.append(pais_creado)

        titulo(f"PAÍS IMPORTADO Y AGREGADO EXITOSAMENTE")
        print(f"{nombre} - {poblacion} hab. - {superficie} km2 - {continente}")
        
    except Exception as e:
        print(f"Ocurrió un error al procesar los datos de la API: {e} 🔴")
    
    tecla_para_continuar()


# --- FUNCIÓN 2: Listar todos los nombres de la API ---

def listar_nombres_paises_api():
    """
    Consulta la API y muestra una lista de todos los nombres de países
    disponibles para que el usuario sepa qué buscar.
    """
    titulo("LISTA DE PAÍSES DISPONIBLES EN LA API")
    
    # URL optimizada: pide solo el campo 'name'
    url_completa = f"{API_URL_BASE}/all?fields=name"
    print(f"Conectando a {url_completa}...")

    try:
        # 1. Hacer la llamada a la API
        with urllib.request.urlopen(url_completa) as respuesta:
            datos_bytes = respuesta.read()
            datos_string = datos_bytes.decode('utf-8')
            datos_api_lista = json.loads(datos_string)

    # --- Manejo de Errores ---
    except HTTPError as e:
        print(f"Error HTTP al consultar la API: {e.code} {e.reason} 🔴")
        tecla_para_continuar()
        return
    except URLError as e:
        print(f"Error de conexión: No se pudo conectar. ¿Tenés internet? 🌐 ({e.reason})")
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

    # --- 2. Procesar la lista de nombres ---
    nombres_paises = []
    for pais_api in datos_api_lista:
        nombre = pais_api.get('name', {}).get('common', 'No disponible')
        if nombre != 'No disponible':
            nombres_paises.append(nombre)
            
    # Ordenamos alfabéticamente
    nombres_paises.sort()
    
    print("\nPaíses encontrados (ordenados alfabéticamente):\n")
    for i, nombre in enumerate(nombres_paises):
        # Usamos end=' | ' para mostrar varios por línea y que no sea una lista eterna
        print(f"- {nombre}", end=' | ' if (i + 1) % 4 != 0 else '\n') 
        
    print(f"\n\nTotal de países disponibles en la API: {len(nombres_paises)}")
