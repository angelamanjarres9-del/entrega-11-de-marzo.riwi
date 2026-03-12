cono = 3000
vaso = 4000
banana = 9000
total_vendido = 0
clientes = 0
cal_cono = 0
cal_vaso = 0
cal_bana = 0

seleccion = ""
while seleccion != "salir":
    seleccion = input("selecciona (cono/vaso/banana o salir): ")
    
    if seleccion == "salir":
        break
        print ("saliendo del menu...")
    
    cantidad = int(input("cuantos deseas?: "))
    
    if seleccion == "cono":
        total_vendido = total_vendido + (cono * cantidad)
        cal_cono = cal_cono + 1
        clientes = clientes + 1

    elif seleccion == "vaso":
        total_vendido = total_vendido + (vaso * cantidad)
        cal_vaso = cal_vaso + 1
        clientes = clientes +1

    elif seleccion == "banana":
        total_vendido = total_vendido + (banana + cantidad )
        cal_bana = cal_bana + 1
        clientes = clientes +1

