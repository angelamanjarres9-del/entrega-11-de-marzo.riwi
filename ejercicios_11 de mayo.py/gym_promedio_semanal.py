
print("Bienvenido al gym-Angela")
bajo = 0
medio= 0
alto = 0

for i in range (5):
    nombre = input("ingresa tu nombre de usuario: ")
    dias =int(input("cuantos dias asististe a la semana? :"))
    minutos =int(input ("cuantos minutos en promedio sientes que entrenas por dia?: "))
    if dias < 3:
      print("tienes un comrpomiso bajo")
      bajo = bajo + 1
    elif dias >= 3 and dias <= 4:
     print("tienes un compromiso medio")
     medio= medio +1
    elif dias >= 5 :
     print("tienes un compromiso alto")
     alto = alto +1
     
print("los usuarios con bajo rendimiento son", bajo)
print("los usuarios con rendimiento medioa son", medio)
print("los usuarios que optuvieron alto rendimiento son", alto)
    




    
    
    