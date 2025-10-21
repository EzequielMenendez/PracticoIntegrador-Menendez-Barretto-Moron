from componentes.funciones import *

#Función para mostrar estadisticas
def mostrar_estadisticas(paises):
    """
        Recibe la lista de paises
        Calcula las diferentes estadicticas y muestra los resultados
    """
    titulo("ESTADÍSTICAS:")

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