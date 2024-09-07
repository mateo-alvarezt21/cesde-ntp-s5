def crear_diccionario_palabras():
    diccionario = {}
    while True:
        palabra = input("Ingresa una palabra (o 'salir' para terminar): ")
        if palabra == 'salir':
            break
        definicion = input(f"Ingresa la definición de {palabra}: ")
        diccionario[palabra] = definicion
    print("Diccionario de palabras y definiciones:", diccionario)

crear_diccionario_palabras()
