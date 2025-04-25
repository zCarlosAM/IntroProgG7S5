#Ejercicio 7. Cálculo de propina según satisfacción
#Ingresar monto total y nivel de satisfacción (buena/mala).
#Si es buena, calcular 15% propina; si es mala, 5%.
#Mostrar total a pagar.

monto_total = int(input("Ingrese el monto total: "))
satisfaccion = input("Ingrese su nivel de satisfacción (b = bueno, m = malo): ")

if(satisfaccion == 'b'):
    propina = 15 / 100
else:
    propina = 5 / 100
    
propina *= int(monto_total)
pago_total = int(monto_total + propina)
print(f"El total a pagar será: {pago_total}")