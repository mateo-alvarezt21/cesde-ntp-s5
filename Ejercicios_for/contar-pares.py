def contar_pares(lista):
    contador = 0
    for num in lista:
        if num % 2 == 0:
            contador += 1
    return contador
numeros = [1, 2, 3, 4, 5, 6]
print(contar_pares(numeros))  
