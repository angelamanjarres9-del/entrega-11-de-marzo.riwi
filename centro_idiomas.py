print("Bienvenido a la academia Angela")

bajo = 0
medio = 0
alto = 0
mejor_estudiante = ""
mejor_promedio = 0
total_promedios = 0
seleccion = ""

while seleccion != "salir":
    nombre = input("nombre del estudiante (o salir): ")
    if nombre == "salir":
        break
    speaking = int(input("nota speaking: "))
    listening = int(input("nota listening: "))
    reading = int(input("nota reading: "))
    
    promedio = (speaking + listening + reading) / 3
    total_promedios = total_promedios + promedio
    
    if promedio < 60:
        bajo = bajo + 1
    elif promedio >= 60 and promedio <= 79:
        medio = medio + 1
    else:
        alto = alto + 1
    
    if promedio > mejor_promedio:
        mejor_promedio = promedio
        mejor_estudiante = nombre

print("nivel bajo:", bajo)
print("nivel medio:", medio)
print("nivel alto:", alto)
print("mejor estudiante:", mejor_estudiante)