def buscar_palabra(diccionario, palabra):
    definicion = diccionario.get(palabra)
    if definicion:
        print(f"La definición de {palabra} es: {definicion}")
    else:
        print(f"La palabra '{palabra}' no se encuentra en el diccionario.")

diccionario_palabras = {'Python': 'Lenguaje de programación', 'Django': 'Framework web'}
palabra_a_buscar = input("Ingresa la palabra que quieres buscar: ")
buscar_palabra(diccionario_palabras, palabra_a_buscar)
