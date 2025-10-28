# Practico Integrador - Menendez - Barretto

## Gestión de Datos de Países

Sistema de gestión y análisis de datos geográficos que permite buscar, filtrar, ordenar y visualizar estadísticas de países a partir del archivo Paises.csv.

## Descripción

Esta aplicación de consola permite administrar y consultar información sobre países del mundo, incluyendo datos de población, superficie y continente.

Ofrece una interfaz interactiva con múltiples opciones de búsqueda, filtrado y análisis estadístico mediante un menú basado en la sintaxis match-case.

## Características

- Visualización general: Muestra todos los países cargados desde el CSV.
- Búsqueda por nombre: Encuentra países por coincidencia parcial (sin importar mayúsculas o minúsculas).
- Filtrado por continente: Permite seleccionar América, Europa, Asia, África u Oceanía.
- Filtrado por población: Define rangos de población mínima y máxima.
- Filtrado por superficie: Define rangos de superficie mínima y máxima en km².
- Ordenamiento múltiple: Ordena la lista por nombre, población o superficie (ascendente o descendente).
- Estadísticas globales: Calcula el país con mayor y menor población, promedios de población y superficie, y cantidad de países por continente.
- Validación robusta: Usa funciones de entrada seguras (pedir_entero, try/except) para evitar cierres por errores del usuario o formato.

## Requisitos

- Python 3.10 o superior (utiliza la sintaxis match-case)

## Descripción de Archivos

### Main

main.py

Archivo principal del programa.
Se encarga de:

- Mostrar el mensaje de bienvenida.
- Llamar al menú principal (menu()).
- Iniciar la ejecución del programa.

### Menu

menu.py

Controla el menú interactivo del sistema.
Usa match-case para manejar las opciones del usuario y coordina las llamadas a las funciones principales.

Opciones disponibles:

- Ver todos los países
- Buscar un país
- Filtrar países (por continente, población o superficie)
- Ordenar países
- Mostrar estadísticas
- Agregar nuevo país
- Editar un país existente
- Eliminar un país
- Salir del programa

### Opciones Menu

la carpeta opciones_menu contiene archivos con la lógica principal de cada opción.

- ver_paises.py: contiene la función para mostrar los países cargados.
- buscar_pais.py: contiene la función para buscar países por nombre.
- filtrar_países.py: contiene las funciones para filtrar países por rango de población, rango de superficie y continente.
- ordenar_paises.py: contiene las funciónes para ordenar por nombre, población, superficie y continente.
- mostrar_estadisticas.py: contiene la función que calcula y muestra las estadísticas globales.
- nuevo_pais.py: contiene la función que agrega un nuevo país al csv.
- editar_pais.py: contiene la función que edita un país del csv.
- eliminar_pais.py: contiene la función que elimina un país del csv.

### Funciones

funciones.py

Contiene la lógica reutilizable del sistema:

- listar_paises(): Lista todos los países y sus datos.
- tecla_para_continuar(): imprime un input para continuar acciones.
- imprimir_lista(): Imprime una lista.
- pedir_entero(): Pide un entero al usuario hasta que sea valido.
- pedir_pais(): Pide el nombre de un país a un usuario hasta que sea valido.
- pedir_continente(): Pide el nombre de un continente a un usuario hasta que sea valido.
- separador(): Imprime una linea separadora.
- titulo(): Imprime el formato de los titulos.
- buscar_linea(): Busca una linea de una lista por nombre.
- buscar_pais(): Busca un único país con exactitud.

### Lector de archivos

lector_archivos.py

Encargado de leer el archivo CSV (Paises.csv).
Usa try-except para manejar errores de archivo inexistente o mal formateado.
Utiliza la función validar_linea para que ignorar las lineas invalidas. Se ignoran las siguientes lineas:

- Encabezado
- lineas vacias
- cantidad de campos incorrectos(deben ser 4)
- nombre con formato invalido(números, caracteres especiales, vacio)
- nombre repetido
- población con formato invalido(debe ser un número positivo)
- superficie con formato invalido(debe ser un número positivo)
- continente invalido(números, caracteres especiales, vacio)
- continente inexistente

Retorna una lista de diccionarios con los datos de cada país.
Ejemplo de lectura:

    {"nombre": "Argentina", "poblacion": 45376763, "superficie": 2780400, "continente": "América"}

### Validaciones

validaciones.py

Incluye las validaciones para para el lector de archivos y otras funciones:

- validar_linea(): Valida que la linea csv sea valida y en caso de serlo devuelve la linea formateada en diccionario.
- parsear_numero(): Parsea un string a entero.
- validar_texto(): valida que un texto sea valido.
- buscar_continente(): valida si un continente ingresado existe, y devuelve el continente formateado.
- parsear_text(): parsea un texto a lower y sin tíldes.
- validar_repetido(): valida que el nombre de un país no se encuentre en la lista de paises.

## Ejemplos de uso

### Muestra del menú

    GESTIÓN DE PAISES
    MENÚ DE OPCIONES
    1. Ver todos los países.
    2. Buscar un país.
    3. Filtrar países.
    4. Ordenar países.
    5. Mostar estadisticas.
    6. Agregar nuevo país
    7. Editar un país existente
    8. Eliminar un país
    0. Salir.
    Ingrese l

### Opción 1. Ver todos los países

    LISTA DE PAÍSES:
    Argentina - 45376763 habitantes - 2780400 km2 - América
    Japon - 125800000 habitantes - 377975 km2 - Asia
    Brasil - 213993437 habitantes - 8515767 km2 - América
    Alemania - 83149300 habitantes - 357022 km2 - Europa
    Canada - 40334000 habitantes - 9984670 km2 - América
    Australia - 26842000 habitantes - 7692024 km2 - Oceanía
    Egipto - 112716000 habitantes - 1002450 km2 - África
    India - 1428627663 habitantes - 3287263 km2 - Asia
    Sudafrica - 62239000 habitantes - 1221037 km2 - África
    Francia - 68233000 habitantes - 551695 km2 - Europa

### Opción 2. Buscar un país

    Ingrese el nombre del país a buscar: ar

    ===================================================

    BUSCANDO PAÍSES... 'ar'

    ===================================================

    LISTA DE PAÍSES:
    Argentina - 45376763 habitantes - 2780400 km2 - América

### Opción 3. Filtrar país

    Filtar países por:
    1. Continente
    2. Rango de población
    3. Rango de superficie
    0. Volver al menú

#### Opción 3,1. Por continente

    CONTINENTES:
    1. América
    2. Europa
    3. Asia
    4. África
    5. Oceanía
    Ingrese el continente a filtrar: 2

    PAÍSES DEL CONTINENTE: Europa

    ===================================================

    LISTA DE PAÍSES:

    Alemania - 83149300 habitantes - 357022 km2 - Europa
    Francia - 68233000 habitantes - 551695 km2 - Europa

#### Opción 3,2. Por población

    Ingrese la población mínima: 40000000
    Ingrese la población máxima: 100000000

    PAÍSES CON POBLACIÓN ENTRE 40000000 Y 100000000

    ===================================================

    LISTA DE PAÍSES:

    Argentina - 45376763 habitantes - 2780400 km2 - América
    Alemania - 83149300 habitantes - 357022 km2 - Europa
    Canada - 40334000 habitantes - 9984670 km2 - América
    Sudafrica - 62239000 habitantes - 1221037 km2 - África
    Francia - 68233000 habitantes - 551695 km2 - Europa

#### Opción 3,3. Por superficie

    Ingrese la superficie mínima: 25000 
    Ingrese la superficie máxima: 50000

    PAÍSES CON UNA SUPERFICIE ENTRE 25000 Y 50000 KM2

    No se encontraron países con una superficie entre 25000 y 50000.

### Opción 4. Ordenar Países

    Ordenar países por:
    1. Nombre
    2. Población
    3. Superficie
    0. Volver al menú

#### Opción 4,1. Por nombre

    ORDENANDO POR NOMBRE...

    Alemania - 83149300 habitantes - 357022 km2 - Europa
    Argentina - 45376763 habitantes - 2780400 km2 - América
    Australia - 26842000 habitantes - 7692024 km2 - Oceanía
    Brasil - 213993437 habitantes - 8515767 km2 - América
    Canada - 40334000 habitantes - 9984670 km2 - América
    Egipto - 112716000 habitantes - 1002450 km2 - África
    Francia - 68233000 habitantes - 551695 km2 - Europa
    India - 1428627663 habitantes - 3287263 km2 - Asia
    Japon - 125800000 habitantes - 377975 km2 - Asia
    Sudafrica - 62239000 habitantes - 1221037 km2 - África

#### Opción 4,2. Por población

    Ingrese 1 si quiere un orden descendente o cualquier otra tecla si quiere orden ascendente: 1

    ORDENANDO POR POBLACIÓN...

    India - 1428627663 habitantes - 3287263 km2 - Asia
    Brasil - 213993437 habitantes - 8515767 km2 - América
    Japon - 125800000 habitantes - 377975 km2 - Asia
    Egipto - 112716000 habitantes - 1002450 km2 - África
    Alemania - 83149300 habitantes - 357022 km2 - Europa
    Francia - 68233000 habitantes - 551695 km2 - Europa
    Sudafrica - 62239000 habitantes - 1221037 km2 - África
    Argentina - 45376763 habitantes - 2780400 km2 - América
    Canada - 40334000 habitantes - 9984670 km2 - América
    Australia - 26842000 habitantes - 7692024 km2 - Oceanía

#### Opción 4,3. Por superficie

    Ingrese 1 si quiere un orden descendente o cualquier otra tecla si quiere orden ascendente: 1

    ORDENANDO POR SUPERFICIE...

    Canada - 40334000 habitantes - 9984670 km2 - América
    Brasil - 213993437 habitantes - 8515767 km2 - América
    Australia - 26842000 habitantes - 7692024 km2 - Oceanía
    India - 1428627663 habitantes - 3287263 km2 - Asia
    Argentina - 45376763 habitantes - 2780400 km2 - América
    Sudafrica - 62239000 habitantes - 1221037 km2 - África
    Egipto - 112716000 habitantes - 1002450 km2 - África
    Francia - 68233000 habitantes - 551695 km2 - Europa
    Japon - 125800000 habitantes - 377975 km2 - Asia
    Alemania - 83149300 habitantes - 357022 km2 - Europa

### Opción 5. Mostrar estadísticas

    ESTADÍSTICAS:

    País con mayor población: India (1428627663)
    País con menor población: Australia (26842000)
    Promedio de población: 220731116
    Promedio de superficie: 3577030

    Cantidad de países por continente:
    América: 3
    Asia: 2
    Europa: 2
    Oceanía: 1
    África: 2

### Opción 6. Agregar nuevo país

### Opción 7. Editar un país existente
    EDITAR PAÍS

    ===================================================

    Ingrese el nombre del país a buscar: japon
    Se encontró el país Japon
    Ingrese la nueva cantidad de población: 1200000
    Ingrese la nueva cantidad de superficie: 1200000
    Ingrese el nuevo continente: Oceania
    ===================================================

    Los datos del país 'Japon' fueron actualizados correctamente.

Si ahora se busca japon:

    BUSCANDO PAÍSES... 'japon'

    ===================================================

    Japon - 1200000 habitantes - 1200000 km2 - Oceanía

### Opción 8. Eliminar un país

    ELIMINAR PAÍS

    ===================================================

    Ingrese el nombre del país a buscar: francia
    ===================================================

    El país 'Francia' se elimino correctamente.

Si ahora busco Francia

    BUSCANDO PAÍSES... 'Francia'

    ===================================================

    No se encontraron países.

## Participación de integrantes

Ezequiel Menéndez: Estructura del proyecto, lectura de archivos y manejo de errores.

Nicolas Morón: Implementación de la API.

Santiago Barretto: Implementación del menú interactivo, funciones de filtrado, ordenamiento y validación de datos.

## Link del video

- 🎥 Video explicativo disponible en el repositorio oficial del proyecto: xxxxxxx.com
- 🔗 https://github.com/EzequielMenendez/PracticoIntegrador-Menendez-Barretto