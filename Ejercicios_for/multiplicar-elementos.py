def multiplicar_elementos(lista):
    nueva_lista = []
    for num in lista:
        nueva_lista.append(num * 2)
    return nueva_lista
numeros = [1, 2, 3, 4, 5]
print(multiplicar_elementos(numeros))  
