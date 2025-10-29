from componentes.funciones import *

#Función para buscar un país
def buscar_paises(paises):
    """
        Recibe una lista de paises y la busqueda del nombre del país.
        Recorre la lista de los paises y busca si el nombre coincide.
        Muestra las coincidencias.
    """
    if sin_paises(paises):
        return
    nombre_buscado = input("Ingrese el nombre del país a buscar: ")
    texto_valido = validar_texto(nombre_buscado)
    if not texto_valido:
        print("Error: No debe ingresar un dato vacio y no puede contener números o caracteres especiales. 🔴")
        return
    titulo(f"BUSCANDO PAÍSES... '{nombre_buscado}'")
    encontrados = []
    for pais in paises:
        if parsear_texto(nombre_buscado) in parsear_texto(pais['nombre']):
            encontrados.append(pais)
    if len(encontrados) == 0:
        print("No se encontraron países.")
        tecla_para_continuar()
    else:
        listar_paises(encontrados)
        tecla_para_continuar()