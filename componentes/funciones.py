# Funciones para el programa
from componentes.lector_archivos import leer_archivo
from componentes.funciones import *

def ver_todos(paises):
    print("\nLISTA DE PAÍSES:\n")
    for pais in paises:
        print(f"{pais['nombre']} - {pais['poblacion']} habitantes - {pais['superficie']} km² - {pais['continente']}")

def buscar_pais(paises, nombre_buscado):
    print(f"\nBUSCANDO PAÍS... '{nombre_buscado}'\n")
    encontrados = []
    for pais in paises:
        if nombre_buscado.lower() in pais['nombre'].lower():
            encontrados.append(pais)
    if len(encontrados) == 0:
        print("No se encontró el pais.")
    else:
        for p in encontrados:
            print(f"{p['nombre']} - {p['poblacion']} habitantes - {p['superficie']} km2 - {p['continente']}")

def filtrar_por_continente(paises, continente):
    print(f"\nPAÍSES DEL CONTINENTE: {continente}\n")
    for pais in paises:
        if pais['continente'].lower() == continente.lower():
            print(f"{pais['nombre']} - {pais['poblacion']} habitantes - {pais['superficie']} km²")

def filtrar_por_poblacion(paises, min_pob, max_pob): # filtrar por poblacion
    print(f"\nPAÍSES CON POBLACION ENTRE {min_pob} Y {max_pob}\n")
    for pais in paises:
        if min_pob <= pais['poblacion'] <= max_pob:
            print(f"{pais['nombre']} - {pais['poblacion']} habitantes - {pais['superficie']} km² - {pais['continente']}")

def ordenar_paises(paises, tipo):
    print(f"\nORDENANDO POR {tipo.upper()}...\n")

    # Copiamos la lista para no modificar la original
    lista_ordenada = paises.copy()

    if tipo == "nombre": # key=lambda es una funcion anonima que toma un parametro p (país) y devuelve p['nombre'], se usa en diccionarios.
        lista_ordenada.sort(key=lambda p: p['nombre']) # Ordena alfabeticamente por nombre
    elif tipo == "poblacion":
        lista_ordenada.sort(key=lambda p: p['poblacion']) # Ordena numericamente por poblacion
    elif tipo == "superficie":
        lista_ordenada.sort(key=lambda p: p['superficie']) # Ordena numericamente por superficie

    for p in lista_ordenada:
        print(f"{p['nombre']} - {p['poblacion']} habitantes - {p['superficie']} km² - {p['continente']}")

def mostrar_estadisticas(paises):
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


def tecla_para_continuar():
    input("Presione una tecla para continuar... ")