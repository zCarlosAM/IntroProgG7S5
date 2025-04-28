calificacion = input("Ingrese una letra de calificación según el sistema estadounidense (A, B, C, D, E, F): ")

calificacion = calificacion.upper()

print("La calificación introducida es: ", end="")
if(calificacion == "A"):
    print("Muy buena")
elif(calificacion == "B"):
    print("Buena")
elif(calificacion == "C"):
    print("Regular")
elif(calificacion == "D"):
    print("Mala")
elif(calificacion == "E"):
    print("Muy mala")
elif(calificacion == "F"):
    print("Pésima")
else:
    print("Inválida.")