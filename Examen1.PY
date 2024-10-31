print("Fco. Santiago Carrasco C.")
print(" ")
#se ingresa los tipos de materias que tengo
materias = ["matematicas", "fisica", "quimica", "historia", "lengua"]
notasrepetir = []
#se hace la magia, si obtuviste algo menor a 6 es tomada como reporbada
#y se suma uno al contador final
for materias in materias:
    nota = float(input(f"ingresa la nota en {materias}: "))
    if nota < 6:
        notasrepetir.append(materias)
#se muestra cunatas materias tienes por reprobadas
print("materias a repetir:", notasrepetir)
