def promedio_notas(diccionario):
    suma_notas = 0
    for nota in diccionario.values():
        suma_notas += nota
    promedio = suma_notas / len(diccionario) if diccionario else 0
    print(f"Promedio de notas: {promedio}")

alumnos_notas = {'Juan': 8.5, 'Maria': 9.0, 'Pedro': 7.5}
promedio_notas(alumnos_notas)
