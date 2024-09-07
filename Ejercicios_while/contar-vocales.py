def contar_vocales(frase):
    vocales = "aeiouAEIOU"
    contador = 0
    i = 0
    while i < len(frase):
        if frase[i] in vocales:
            contador += 1
        i += 1
    return contador

frase = input("Ingresa una frase: ")
print(f"La frase contiene {contar_vocales(frase)} vocales.")
