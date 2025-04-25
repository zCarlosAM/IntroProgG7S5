#Ejercicio#8. Verificación de inicio de sesión
# Ingresar nombre de usuario y clave.
# Si el usuario es “admin” y la clave “1234admin”, permitir acceso.
# Si no, denegar.

usuario_admin = "admin"
clave_admin = "1234admin"

usuario = input("Ingrese su usuario: ")
clave = input("Ingrese su contraseña: ")

if(usuario == usuario_admin and clave == clave_admin):
    print(f"Bienvenido, {usuario}")
else:
    print("Acceso denegado.")