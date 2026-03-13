print("Bienvenido a la cafeteria Angela")
cafe = 4000
capuchino = 7000
pastel = 6000
seleccion = ""
total = 0
cliente = 0
total_dia = 0 

while seleccion != "salir":
    seleccion = input("Que desea pedir el dia de hoy? (cafe, capuchino, pastel o desea salir del menu? :")
    
    if seleccion == "salir":
        break
      
    
    unidades =int(input("Cuantas unidades desea comprar: "))

    if seleccion == "cafe":
        total = cafe * unidades
        if total > 20000:
          total = total - (total * 0.10)
          
    elif seleccion == "capuchino":
         total = capuchino * unidades
         if total > 20000:
            total = total - (total *0.10)
            
    elif seleccion == "pastel":
         total = pastel * unidades
         if total > 20000:
               total = total - (total *0.10)
               
    total_dia = total_dia + total          
    print("su total cliente:", total)        



print("el monto total ganado en el dia es", total_dia)
    

    

