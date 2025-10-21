from componentes.funciones import *

#Función para ver países
def ver_paises(paises):
    """
        Recibe una lista de paises y los recorre para listarlos
    """
    titulo("LISTA DE PAÍSES:")
    for pais in paises:
        print(f"{pais['nombre']} - {pais['poblacion']} habitantes - {pais['superficie']} km2 - {pais['continente']}")
    tecla_para_continuar()