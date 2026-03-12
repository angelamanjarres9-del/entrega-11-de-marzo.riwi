primera_hora = 5000
adicional = 3000
contador=0

horas = int(input("ingresa el numero de horas que estuviste en el gym el dia de hoy?: "))

if horas == 1:
    total = 5000 * horas

elif horas >1:
    total = 5000  + (horas - 1) * 3000

print("el total a pagar es", total)