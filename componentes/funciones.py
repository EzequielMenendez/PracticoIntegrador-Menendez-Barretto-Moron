#Función para ver países
def ver_paises(paises):
    """"
        Recibe una lista de paises y los recorre para listarlos
    """
    separador()
    print("\nLISTA DE PAÍSES:\n")
    for pais in paises:
        print(f"{pais['nombre']} - {pais['poblacion']} habitantes - {pais['superficie']} km2 - {pais['continente']}")
    tecla_para_continuar()

#Función para buscar un país
def buscar_pais(paises, nombre_buscado):
    """"
        Recibe una lista de paises y la busqueda del nombre del país.
        Recorre la lista de los paises y busca si el nombre coincide.
        Muestra las coincidencias.
    """
    separador()
    print(f"\nBUSCANDO PAÍSES... '{nombre_buscado}'\n")
    encontrados = []
    for pais in paises:
        if nombre_buscado.lower() in pais['nombre'].lower():
            encontrados.append(pais)
    if len(encontrados) == 0:
        print("No se encontraron países.")
        tecla_para_continuar()
    else:
        ver_paises(encontrados)

#Función para filtar por continente
def filtrar_por_continente(paises, continente):
    """"
        Recibe una lista de paises y el continente.
        Recorre la lista de los paises y busca si el continente coincide.
        Muestra las coincidencias.
    """
    print(f"\nPAÍSES DEL CONTINENTE: {continente}\n")
    encontrados = []
    for pais in paises:
        if pais['continente'].lower() == continente.lower():
            encontrados.append(pais)
    
    if len(encontrados) == 0:
        print(f"No se encontraron países en el continente {continente}.")
        tecla_para_continuar()
    else:
        ver_paises(encontrados)

#Función para filtrar por población
def filtrar_por_poblacion(paises, min_pob, max_pob):
    """"
        Recibe una lista de paises, el mínimo de población, y el máximo de población
        Recorre la lista de los paises y busca los países entre el mínimo y el máximo de población
        Muestra las coincidencias.
    """
    print(f"\nPAÍSES CON POBLACION ENTRE {min_pob} Y {max_pob}\n")
    encontrados = []
    for pais in paises:
        if min_pob <= pais['poblacion'] <= max_pob:
            encontrados.append(pais)
    
    if len(encontrados) == 0:
        print(f"No se encontraron países con población entre {min_pob} y {max_pob}.")
        tecla_para_continuar()
    else:
        ver_paises(encontrados)

#Función para filtrar por superficie
def filtrar_por_superficie(paises, min_sup, max_sup):
    """"
        Recibe una lista de paises, el mínimo de superficie, y el máximo de superficie
        Recorre la lista de los paises y busca los países entre el mínimo y el máximo de superficie
        Muestra las coincidencias.
    """
    print(f"\nPAÍSES CON UNA SUPERFICIE ENTRE {min_sup} Y {max_sup} KM2\n")
    encontrados = []
    for pais in paises:
        if min_sup <= pais['superficie'] <= max_sup:
            encontrados.append(pais)
    
    if len(encontrados) == 0:
        print(f"No se encontraron países con una superficie entre {min_sup} y {max_sup}.")
        tecla_para_continuar()
    else:
        ver_paises(encontrados)

#Función para ordenar países
def ordenar_paises(paises, tipo, descendente = False):
    """"
        Recibe una lista de paises, el tipo de ordenamiento y si el orden es descendente o no
        Evalua el tipo de ordenamiento y realiza el ordenamiento según el descendente
    """
    print(f"\nORDENANDO POR {tipo.upper()}...\n")

    # Copiamos la lista para no modificar la original
    lista_ordenada = paises.copy()
    # key=lambda es una funcion anonima que toma un parametro p (país) y devuelve p['nombre'], se usa en diccionarios.
    lista_ordenada.sort(key=lambda p: p[tipo], reverse=descendente) # Ordena alfabeticamente por según el tipo

    for p in lista_ordenada:
        print(f"{p['nombre']} - {p['poblacion']} habitantes - {p['superficie']} km2 - {p['continente']}")
    tecla_para_continuar()

#Función para mostrar estadisticas
def mostrar_estadisticas(paises):
    """
        Recibe la lista de paises
        Calcula las diferentes estadicticas y muestra los resultados
    """
    separador()
    print("\nESTADÍSTICAS:\n")

    mayor_pob = paises[0]
    menor_pob = paises[0]
    total_pob = 0
    total_sup = 0
    contador_continentes = {}

    for pais in paises:
        # Calcular mayor y menor
        if pais['poblacion'] > mayor_pob['poblacion']:
            mayor_pob = pais
        if pais['poblacion'] < menor_pob['poblacion']:
            menor_pob = pais

        # Sumar para promedios
        total_pob += pais['poblacion']
        total_sup += pais['superficie']

        # Contar por continente
        cont = pais['continente']
        if cont in contador_continentes:
            contador_continentes[cont] += 1
        else:
            contador_continentes[cont] = 1

    promedio_pob = total_pob / len(paises)
    promedio_sup = total_sup / len(paises)

    print(f"País con mayor población: {mayor_pob['nombre']} ({mayor_pob['poblacion']})")
    print(f"País con menor población: {menor_pob['nombre']} ({menor_pob['poblacion']})")
    print(f"Promedio de población: {promedio_pob:.0f}")
    print(f"Promedio de superficie: {promedio_sup:.0f}")
    print("\nCantidad de países por continente:")
    for c, cantidad in contador_continentes.items():
        print(f"{c}: {cantidad}")
    tecla_para_continuar()

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
    print("===================================================")