# Ejercicio 12. Detección de condiciones extremas en servidor
# Ingresar temperatura y uso de CPU.
# Si la temperatura > 80 °C o el CPU > 95%, iniciar protocolo de emergencia.

temperatura = int(input("Ingrese la temperatura del equipo: "))
uso_cpu = int(input("ingrese el uso del CPU: "))

if(temperatura > 80 or uso_cpu > 95):
    print("Atención! El equipo se apagará para prevenir posibles daños.")
else:
    print("Todo en orden")