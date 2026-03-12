asistencias = int(input("cuantas veces asististe en el mes a la academia?: "))

if asistencias < 5:
    print("tienes un rango de asistencias baja")

elif asistencias >= 5 and asistencias <= 8:
    print ("tienes un rango de asistencias media")
elif asistencias >= 9:
    print("bien trabajo, el rango de asistencias es alto")
