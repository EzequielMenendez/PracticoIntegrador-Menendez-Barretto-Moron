from componentes.funciones import *

#Función para buscar un país
def buscar_pais(paises, nombre_buscado):
    """
        Recibe una lista de paises y la busqueda del nombre del país.
        Recorre la lista de los paises y busca si el nombre coincide.
        Muestra las coincidencias.
    """
    titulo(f"BUSCANDO PAÍSES... '{nombre_buscado}'")
    encontrados = []
    for pais in paises:
        if nombre_buscado.lower() in pais['nombre'].lower():
            encontrados.append(pais)
    if len(encontrados) == 0:
        print("No se encontraron países.")
        tecla_para_continuar()
    else:
        listar_paises(encontrados)