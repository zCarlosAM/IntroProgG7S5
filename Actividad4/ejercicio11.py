# Ejercicio 11. Determinar si hay saldo suficiente para una compra
# Ingresar precio del producto y saldo disponible.
# Si el saldo alcanza, permitir la compra.
# Si no, mostrar “Saldo insuficiente”.

precio = int(input("Ingrese el precio del producto: "))
saldo = int(input("Ingrese el saldo disponible: "))

if(saldo >= precio):
    print("Puede proceder con la compra.")
else:
    print("Saldo insuficiente.")