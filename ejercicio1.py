range_min = int(input("Ingrese el inicio de un rango: "))
range_max = int(input("Ingrese el limite de ese rango: "))

if(range_min < range_max):
    num = int(input("Ingrese un número que se encuentre entre ese rango: "))
    if(num >= range_min and num <= range_max):
        print(f"El número {num} está dentro del rango.")
    else:
        print(f"El número {num} está fuera del rango.")

else:
    print("Error: El inicio del rango no puede ser mayor al límite del rango.")