lado1 = int(input("Ingresa el primer lado: "))
lado2 = int(input("Ingresa el segundo lado: "))
lado3 = int(input("Ingresa el tercer lado: "))

if lado1 == lado2 and lado1 == lado3:
    print("Es un triángulo equilátero")
elif (lado1 == lado2 and lado2 != lado3) or (lado2 == lado3 and lado3 != lado1) or (lado1 == lado3 and lado3 != lado2):
    print("Es un triángulo isóceles.")
elif lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
    print("Es un triángulo escaleno.")