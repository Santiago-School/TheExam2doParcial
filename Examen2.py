print("Fco. Santiago Carrasco C.")
print(" ")
#se genera la seccion de las materias y sus respectivas calificaciones
materias = {"matematicas": 6, "fisica": 3, "quimica": 8}
#el total de puntos por materia hasta el momento:
totalpuntos = 0

#la magia que hace contar los puntos de cada materia
for materia, puntos in materias.items():
    print(f"{materia} tiene {puntos} puntos")
    totalpuntos += puntos

#se imprime el total de numero en todo el curso respondiente a las materias
print("numero total de puntos del curso:", totalpuntos)
