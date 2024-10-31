print("Fco. Santiago Carrasco C.")
print(" ")
#se metera en una lista los datos generales de una persona, iniciando por "usuario"
usuario = {}

#se pregunta el nombre
usuario["nombre"] = input("ingresa tu nombre: ")
# la edad..
usuario["edad"] = input("ingresa tu edad: ")
#la adreess del individuo en cuestion
usuario["direccion"] = input("ingresa tu direccion: ")
#su telefono para cambiarlo a movistar 
usuario["telefono"] = input("ingresa tu telefono: ")

print("ahora se juntaran todos los datos de forma un poco mas ordenada")
print(" ")
print(f"{usuario['nombre']} tiene {usuario['edad']} años, vive en {usuario['direccion']} y su numero de telefono es {usuario['telefono']}.")
