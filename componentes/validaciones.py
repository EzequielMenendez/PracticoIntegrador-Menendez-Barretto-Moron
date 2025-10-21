import unicodedata

#Función para validar cada linea del archivo
def validar_linea(linea, contador, paises):
    if contador == 1:
        return None

    linea = linea.strip()

    if linea == "":
        return None
    
    datos = linea.split(",")
    
    if len(datos) != 4:
        print(f"Se ignoro el país número {contador}. Cantidad de campos incorrectos, debe tener 4.")
        return None
    
    nombre, poblacion, superficie, continente = datos

    # Validaciones del nombre

    nombre_valido = validar_texto(nombre)
    if not nombre_valido:
        print(f"Se ignoro el país número {contador}. El nombre no puede estar vacio y no puede contener números o caracteres especiales.")
        return None
    
    nombre_unico = validar_repetido(nombre, paises)
    if not nombre_unico:
        print(f"Se ignoro el país número {contador}. El país se encuentra repetido.")
    
    # Validaciones del dato población

    poblacion = parsear_numero(poblacion)
    if not poblacion:
        print(f"Se ignoro el país número {contador}. La población debe ser un número positivo.")
        return None
    
    #Validaciones del dato superficie

    superficie = parsear_numero(superficie)
    if not superficie:
        print(f"Se ignoro el país número {contador}. La superficie debe ser un número positivo.")
        return None
    
    #Validaciones del continente

    continente_valido = validar_texto(continente)
    if not continente_valido:
        print(f"Se ignoro el país número {contador}. El continente no puede estar vacio y no puede contener números o caracteres especiales.")
        return None

    continentes = ["América","Europa","Asia","África","Oceanía"]

    continente = buscar_continente(continente, continentes)
    
    if not continente in continentes:
        print(f"Se ignoro el país número {contador}. El continente no es un continente existente.")
        return None

    return {
        "nombre": nombre, #str | clave
        "poblacion": int(poblacion), #int | clave
        "superficie": int(superficie), #int | clave
        "continente": continente #str | clave
    }

#Función para parsear a número
def parsear_numero(num):
    try:
        num = int(num)
    except ValueError:
        return None
    
    if num <= 0:
        return None
    
    return num

#Función para validar un caracter
def validar_texto(str):
    if str.strip() == "":
        return False
    
    permitidos = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZáéíóúÁÉÍÓÚñÑ "
    
    return all(c in permitidos for c in str)

#Función para validar si el continente es real y parsearlo a un formato estandar
def buscar_continente(continente, continentes):
    continente_parseado = unicodedata.normalize('NFD', continente.lower())#unicode se utiliza para parsear caracteres a un tipo de datos, en este caso 'NFD' que separa las letras de sus tíldes
    continente_parseado = continente_parseado.encode('ascii', 'ignore').decode('utf-8')#encode parsea el texto a ASCII, e ignora los caracteres no validos con tíltes. con decode lo vuelvo a parsear a utf-8

    for cont in continentes:
        cont_parseado = unicodedata.normalize('NFD', cont.lower())
        cont_parseado = cont_parseado.encode('ascii', 'ignore').decode('utf-8')

        if continente_parseado == cont_parseado:#Si el continente se encuentra dentro de la lista de continentes
            continente = cont #Parseo el continente

    return continente

#Función para validar que un país no se repita
def validar_repetido(nombre, paises):
    valido = True
    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            valido = False
    return valido