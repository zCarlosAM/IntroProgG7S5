#Calificación cualitativa
#Solicita una calificación numérica entre 0 y 100 y muestra si es 
# "Reprobado (menos de 70)", "Regular (70-79)", "Bueno(80-89)", "Muy bueno(90-95)" o "Excelente(96<)".

calificacion = int(input("Ingrese su calificación: "))

if(calificacion >= 0 and calificacion < 70):
    print("Usted está reprobado.")
elif(calificacion >= 70 and calificacion <= 79):
    print("Usted tiene una calificación regular.")
elif(calificacion >= 80 and calificacion <= 89):
    print("Usted tiene una calificación buena.")
elif(calificacion >= 90 and calificacion <= 95):
    print("Usted tiene una calificación muy buena.")
elif(calificacion >= 96 and calificacion <= 100):
    print("Usted tiene una calificación excelente.")
else:
    print("La calificación introducida no es válida.")
