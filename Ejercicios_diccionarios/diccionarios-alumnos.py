def crear_diccionario_alumnos():
    alumnos = {}
    while True:
        nombre = input("Ingresa el nombre del alumno (o 'salir' para terminar): ")
        if nombre == 'salir':
            break
        nota = float(input(f"Ingresa la nota de {nombre}: "))
        alumnos[nombre] = nota
    print("Alumnos y sus notas:", alumnos)

crear_diccionario_alumnos()
