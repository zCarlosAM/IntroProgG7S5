temperatura = int(input("Ingrese una temperatura (en Celsius): "))

if(temperatura < 15):
    clima = "Frío"
elif(temperatura >= 15 and temperatura <= 24):
    clima = "Templado"
elif(temperatura >= 25 and temperatura <= 30):
    clima = "Cálido"
elif(temperatura > 30):
    clima = "Muy caluroso"
    
print("El clima actual es:", clima)