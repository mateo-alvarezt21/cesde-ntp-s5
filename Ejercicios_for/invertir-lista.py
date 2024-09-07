def invertir_lista(lista):
    lista_invertida = []
    for i in range(len(lista) - 1, -1, -1):
        lista_invertida.append(lista[i])
    return lista_invertida

numeros = [1, 2, 3, 4, 5]
print(invertir_lista(numeros)) 
