edad = int(input("Ingrese su edad: "))

if(edad > 0 and edad < 12):
    print("Usted es un niño.")
elif(edad >= 12 and edad <= 17):
    print("Usted es un adolescente.")
elif(edad >= 18 and edad <= 65):
    print("Usted es un adulto.")
elif(edad >= 66 and edad <= 120):
    print("Usted es un anciano.")
else:
    print("La edad introducida no es válida.")