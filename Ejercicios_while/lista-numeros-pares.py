def lista_numeros_pares():
    pares = []
    num = 1
    while num <= 100:
        if num % 2 == 0:
            pares.append(num)
        num += 1
    return pares

print(lista_numeros_pares()) 
