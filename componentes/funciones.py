from componentes.validaciones import *

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

#Función para pedir un número entero valido
def pedir_entero(mensaje):
    """Pide un numero entero por consola y controla errores."""
    while True:
        valor = input(mensaje)
        valor = parsear_numero(valor)
        if not valor:
            print("Error: debe ingresar un numero entero valido positivo. 🔴")
        else:
            return valor

#Función para pedir y validar un país
def pedir_pais(mensaje, paises):
    """Pide un string por consola, valida el texto y que el país no este repetido"""
    while True:
        valor = input(mensaje)
        texto_valido = validar_texto(valor)
        if not texto_valido:
            print("Error: No debe ingresar un dato vacio y no puede contener números o caracteres especiales. 🔴")
            continue
        nombre_unico = validar_repetido(valor, paises)
        if not nombre_unico:
            print("Error: El país ingresado ya existe. Ingrese otro país. 🔴")
            continue
        return valor

#Función para pedir y validar un continente
def pedir_continente(mensaje):
    """Recibe un string por consola, valida el texto y que sea un continente existente"""
    continentes = ("América","Europa","Asia","África","Oceanía")
    while True:
        valor = input(mensaje)
        texto_valido = validar_texto(valor)
        if not texto_valido:
            print("Error: No debe ingresar un dato vacio y no puede contener números o caracteres especiales. 🔴")
            continue
        valor = buscar_continente(valor, continentes)
        
        if not valor in continentes:
            print(f"Error: El continente ingresado no es válido. Los continentes existentes son: {', '.join(continentes)}. 🔴")
            continue
        
        return valor

#Imprime un separador
def separador():
    print("===================================================\n")

#Imprime el formato de un título
def titulo(texto):
    separador()
    print(f"{texto}\n")
    separador()

#Función para buscar una línea en el csv
def buscar_linea(lineas, pais):
    """
        Recibe una lista de líneas y el país a buscar
        Recorre las líneas y si el país coincide guarda el número de linea y lo retorna
    """
    #Busca el país en el csv
    for i, linea in enumerate(lineas):#enumerate sirve para recorrer una lista y al mismo tiempo obtener el indice
        datos = linea.strip().split(",")
        if len(datos) and datos[0].lower() == pais.lower():
            return i

#Busca un país por coincidencia exacta
def buscar_pais(paises):
    """
        Pide por consola un país a buscar, y lo busca por coincidencia exacta
        Devuelve el nombre del país y su índice
    """
    busqueda = input("Ingrese el nombre del país a buscar: ")
    indice_encontrado = None
    pais_encontrado = None

    for i, pais in enumerate(paises):
        if busqueda.lower() == pais['nombre'].lower():
            indice_encontrado = i
            pais_encontrado = pais['nombre']
            break

    if not indice_encontrado:
        print(f"No se encontró el país {busqueda}.")

    return pais_encontrado, indice_encontrado