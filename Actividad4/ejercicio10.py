#Ejercicio#10. Verificación de validez de una fecha
# Ingresar día, mes, y año.
# Si el mes es febrero y el día > 29, mostrar error.
# Si el mes es abril, junio, septiembre o noviembre y el día > 30, mostrar error
# Si el mes es enero, marzo, mayo, julio, agosto, octubre, diciembre y el día > 31, mostrar error

dia = int(input("Ingrese un día: "))
mes = input("Ingrese un mes: ")
año = int(input("Ingrese un año: "))

mes = mes.lower()

if(mes == "febrero" and dia > 29):
    print("La fecha introducida no es válida.")    
elif((mes == "abril" or mes == "junio" or mes == "septiembre" or mes == "noviembre") and dia > 30):
    print("La fecha introducida no es válida.")
elif((mes == "enero" or mes == "marzo" or mes == "mayo" or mes == "julio" or mes == "agosto" or mes == "octubre" or mes == "diciembre") and dia > 31):
    print("La fecha introducida no es válida.")
else:
    print("La fecha introducida es válida.")