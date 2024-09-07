def calculadora():
    while True:
        print("Operaciones: +, -, *, / o 'salir' para terminar.")
        operacion = input("Elige una operación: ")
        
        if operacion == 'salir':
            break

        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        
        if operacion == '+':
            resultado = num1 + num2
        elif operacion == '-':
            resultado = num1 - num2
        elif operacion == '*':
            resultado = num1 * num2
        elif operacion == '/':
            if num2 != 0:
                resultado = num1 / num2
            else:
                print("Error: división por cero no permitida.")
                continue
        else:
            print("Operación no válida.")
            continue
        
        print(f"El resultado es: {resultado}")
calculadora()
