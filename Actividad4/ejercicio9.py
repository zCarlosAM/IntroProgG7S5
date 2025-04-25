#Ejercicio#9. Encontrar el mayor de tres números
# Ingresar el primer número
# Ingresar el segundo número
# Ingresar el tercer número
# Si el primero es mayor o igual que el segundo, comparar el primero con el tercero
# Si el primero es menor que el segundo, compara el segundo con el tercero
# Si los tres son iguales, mostrar “Los números son iguales”
def main():
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    num3 = int(input("Ingrese el tercer número: "))

    if(num1 == num2 and num2 == num3):
        print("Los tres números introducidos son iguales")
        return
    
    if(num1 >= num2):
        if(num1 >= num3):
            print("El número mayor de los tres es el primer número.")
        else:
            print("El número mayor de los tres es el tercer número")
    else:
        if(num2 >= num3):
            print("El número mayor de los tres es el segundo número")
        else:
            print("El número mayor de los tres es el tercer número")

main()