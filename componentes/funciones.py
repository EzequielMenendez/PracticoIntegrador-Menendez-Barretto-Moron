#Función para filtar por continente
def filtrar_por_continente(paises, continente):
    """
        Recibe una lista de paises y el continente.
        Recorre la lista de los paises y busca si el continente coincide.
        Muestra las coincidencias.
    """
    titulo(f"PAÍSES DEL CONTINENTE: {continente}")
    encontrados = []
    for pais in paises:
        if pais['continente'].lower() == continente.lower():
            encontrados.append(pais)
    
    if len(encontrados) == 0:
        print(f"No se encontraron países en el continente {continente}.")
    else:
        listar_paises(encontrados)
    tecla_para_continuar()

#Función para filtrar por población
def filtrar_por_poblacion(paises, min_pob, max_pob):
    """
        Recibe una lista de paises, el mínimo de población, y el máximo de población
        Recorre la lista de los paises y busca los países entre el mínimo y el máximo de población
        Muestra las coincidencias.
    """
    titulo(f"PAÍSES CON POBLACION ENTRE {min_pob} Y {max_pob}")
    encontrados = []
    for pais in paises:
        if min_pob <= pais['poblacion'] <= max_pob:
            encontrados.append(pais)
    
    if len(encontrados) == 0:
        print(f"No se encontraron países con población entre {min_pob} y {max_pob}.")
    else:
        listar_paises(encontrados)
    tecla_para_continuar()

#Función para filtrar por superficie
def filtrar_por_superficie(paises, min_sup, max_sup):
    """
        Recibe una lista de paises, el mínimo de superficie, y el máximo de superficie
        Recorre la lista de los paises y busca los países entre el mínimo y el máximo de superficie
        Muestra las coincidencias.
    """
    titulo(f"PAÍSES CON UNA SUPERFICIE ENTRE {min_sup} Y {max_sup} KM2")
    encontrados = []
    for pais in paises:
        if min_sup <= pais['superficie'] <= max_sup:
            encontrados.append(pais)
    
    if len(encontrados) == 0:
        print(f"No se encontraron países con una superficie entre {min_sup} y {max_sup}.")
    else:
        listar_paises(encontrados)
    tecla_para_continuar()

#Función para ordenar países
def ordenar_paises(paises, tipo, descendente = False):
    """
        Recibe una lista de paises, el tipo de ordenamiento y si el orden es descendente o no
        Evalua el tipo de ordenamiento y realiza el ordenamiento según el descendente
    """
    titulo(f"ORDENANDO POR {tipo.upper()}...")

    # Copiamos la lista para no modificar la original
    lista_ordenada = paises.copy()
    # key=lambda es una funcion anonima que toma un parametro p (país) y devuelve p['nombre'], se usa en diccionarios.
    lista_ordenada.sort(key=lambda p: p[tipo], reverse=descendente) # Ordena alfabeticamente por según el tipo

    listar_paises(lista_ordenada)
    tecla_para_continuar()

def listar_paises(paises):
    for pais in paises:
        print(f"{pais['nombre']} - {pais['poblacion']} habitantes - {pais['superficie']} km2 - {pais['continente']}")

#Función para continuar al menú
def tecla_para_continuar():
    input("Presione una tecla para continuar... ")

#Función para imprimir una lista
def imprimir_lista(lista):
    separador()
    for elemento in lista:
        print(elemento)

def pedir_entero(mensaje):
    """Pide un numero entero por consola y controla errores."""
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("Error: debe ingresar un numero entero valido. 🔴")


#Imprime un separador
def separador():
    print("===================================================\n")

def titulo(texto):
    separador()
    print(f"{texto}\n")
    separador()