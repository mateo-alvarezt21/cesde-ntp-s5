def eliminar_duplicados(lista):
    resultado = []
    i = 0
    while i < len(lista):
        if lista[i] not in resultado:
            resultado.append(lista[i])
        i += 1
    return resultado

numeros = [1, 2, 2, 3, 4, 4, 5]
print(eliminar_duplicados(numeros)) 
