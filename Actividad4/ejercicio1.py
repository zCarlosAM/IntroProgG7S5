rango_inicial = int(input("Ingrese el inicio de un rango: "))
rango_final = int(input("Ingrese el limite de ese rango: "))

if(rango_inicial < rango_final):
    num = int(input("Ingrese un número que se encuentre entre ese rango: "))
    if(num >= rango_inicial and num <= rango_final):
        print(f"El número {num} está dentro del rango.")
    else:
        print(f"El número {num} está fuera del rango.")

else:
    print("Error: El inicio del rango no puede ser mayor al límite del rango.")