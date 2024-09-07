def elemento_mas_grande(lista):
    if not lista:
        return None 
    mayor = lista[0]
    for num in lista:
        if num > mayor:
            mayor = num
    return mayor
numeros = [1, 2, 3, 10, 5]
print(elemento_mas_grande(numeros))  
