# Menú de operaciones básicas
# Presenta un menú con las opciones: sumar, restar, multiplicar o dividir dos números. Elige la opción con un número y realiza la operación.
def main():
    print("\nOperaciones:")
    print("-" * 32)
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("-" * 32)

    operacion = int(input("Ingrese el tipo de operación: "))

    num1 = int(input("Ahora, ingrese un número: "))
    num2 = int(input("Ingrese el segundo número: "))
    
    print("-" * 32)
    if(operacion == 1):
        resultado = num1 + num2
    elif(operacion == 2):
        resultado = num1 - num2
    elif(operacion == 3):
        resultado = num1 * num2
    elif(operacion == 4):
        resultado = num1 / num2
    else:
        print("La operación introducida no es válida.")
        return
    
    print("El resultado de la operación escogida es: ", resultado)
     
main()