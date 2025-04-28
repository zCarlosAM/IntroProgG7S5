edad = int(input("Ingrese su edad: "))

if(edad >= 0 and edad <= 12):
    print("Usted puede entrar a ver una película infantil")
elif(edad >= 13 and edad <= 17):
    print("Usted puede entrar a ver una película para adolescentes")
elif(edad >= 18 and edad <= 120):
    print("Usted puede entrar a ver una película para adultos")
else:
    print("La edad introducida no es válida")