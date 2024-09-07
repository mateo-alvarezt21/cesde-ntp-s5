def alumno_con_mejor_nota(diccionario):
    if not diccionario:
        print("El diccionario está vacío.")
        return
    mejor_alumno = max(diccionario, key=diccionario.get)
    print(f"El alumno con mejor nota es {mejor_alumno} con una nota de {diccionario[mejor_alumno]}")

alumnos_notas = {'Juan': 8.5, 'Maria': 9.0, 'Pedro': 7.5}
alumno_con_mejor_nota(alumnos_notas)
