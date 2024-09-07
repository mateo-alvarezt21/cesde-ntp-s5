def suma_elementos(lista):
    suma = 0
    for num in lista:
        suma += num
    return suma

numeros = [1, 2, 3, 4, 5]
print(suma_elementos(numeros)) 
