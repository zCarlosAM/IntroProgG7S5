import datetime

fecha_inicio_sesion = input("Último inicio de sesión en formato YYYY-MM-DD: ")
fecha_inicio_sesion = datetime.datetime.strptime(fecha_inicio_sesion, "%Y-%m-%d")

fecha_actual = datetime.datetime.now()

contar_dias = (fecha_actual - fecha_inicio_sesion).days
if contar_dias > 30:
    print("Inactivo por más de 30 días")
else:
    print("Estamos bien.")