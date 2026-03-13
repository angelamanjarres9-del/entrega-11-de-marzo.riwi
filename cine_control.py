print("Bienvenido a la sala de cine Angel: ")

capacidad = int(input("cual es la capacidad de la sala: "))
niños = 0
adultos = 0
adulto_mayor = 0
total_personas = 0

while total_personas < capacidad:
    edad = int(input("cuantos años tienes?: "))
    if edad < 12:
     niños = niños + 1
    
    elif edad >= 12 and edad <= 59:
        adultos = adultos + 1
    elif edad >= 60:
        adulto_mayor = adulto_mayor + 1 
        
    total_personas = total_personas + 1
     
print("El total de personas es", total_personas)
print("El total de niños en sala es", niños)
print("El total de adultos en sala es",adultos)
print("El total de adultos mayores en sala es", adulto_mayor)    

if total_personas == capacidad:
    print("la sala se lleno")
else:
    print ("no se lleno la sala")
    
    
     
    

