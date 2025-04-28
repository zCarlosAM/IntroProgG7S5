num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

if(num1 == num2 and num2 == num3):
    print("Todos los números son iguales")
elif(num1 > num2 and num2 > num3):
    num_mayor = "primer número"
    num_menor = "tercer número"
elif(num1 < num2 and num2 > num3):
    num_mayor = "segundo numero"
    num_menor = "tercer número"
elif(num1 < num2 and num2 < num3):
    num_mayor = "tercer número"
    num_menor = "primer numero"
elif(num1 > num2 and num2 < num3):
    num_mayor = "tercer número"
    num_menor = "segundo numero"
    
print("El número mayor es el", num_mayor)
print("Mientras que el menor es el", num_menor)