dia = input("Ingrese un día de la semana: ")

dia = dia.lower();
if(dia == "lunes"):
    print("El día introducido es un día laboral")
elif(dia == "martes"):
    print("El día introducido es un día laboral")
elif(dia == "miércoles" or dia == "miercoles"):
    print("El día introducido es un día laboral")
elif(dia == "jueves"):
    print("El día introducido es un día laboral")
elif(dia == "viernes"):
    print("El día introducido es un día laboral")
elif(dia == "sábado" or dia == "sabado"):
    print("El día introducido es un fin de semana")
elif(dia == "domingo"):
    print("El día introducido es un fin de semana")
else:
    print("El día introducido no es válido")