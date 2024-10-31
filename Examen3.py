print("Fco. Santiago Carrasco C.")
print(" ")
#nuevamente se ingresa las materias correspondientes
asignaturas = ["matematicas", "fisica", "quimica", "historia", "lengua"]
notas = {}

#en la magia de hoy se aplicara este metodo para obtener el nombre de la materia
# y su respectiva nota o calificacion 

#se pregunta que nota ha obtenido en la materia
for asignatura in asignaturas:
    nota = float(input(f"ingresa la nota en {asignatura}: "))
    notas[asignatura] = nota
print(" Es todo, ahora de dare una lista de los datos que me acabas de proporcionar")
print(" ")
print(" Ahora te muestro todos los datos obtenidos pero de forma mas ordenada")
#Se imprime en pantalla el nombre de las asignaturas y sus correspondientes notas
for asignatura, nota in notas.items():
    print(f"en {asignatura} has sacado {nota}")
