hora_de_llegada  =int(input("Para descuentos en proximas ocasiones, digite a que hora llego a la peluqueria entre EN FORMATO 24 HORAS: "))

if hora_de_llegada  >=6 and hora_de_llegada <= 11:
   print("llegaste a la peluqueria en el turno de la mañana")

elif hora_de_llegada >= 12 and hora_de_llegada <=17:
   print("llegaste a la peluqueria en el turno de la tarde")

elif hora_de_llegada >= 18 and hora_de_llegada <= 22:
   print("llegaste a la peluqueria en e turno de la noche")

else:
  print("fuera del horario")








