print("Bienvenido a parqueadero seguridad ante todo")
moto = 2000
carro = 4000
es_moto = 0
es_carro = 0
total = 0
pago_mayor = 0
total_recaudado = 0
placa_mayorPAGO = ""

for i in range (8):
    placa = input("Escribe tu placa aqui, para registar tu veliculo en sistema: ")
    tipo = input("tu vehiculo es un carro o una moto?: ")
    horas = int(input("cuantas horas deseas dejar tu vehiculo?: "))
    
    if tipo == "moto":
     total = moto * horas
     es_moto = es_moto + 1
     
    elif tipo == "carro":
     total = carro * horas
     es_carro = es_carro + 1
   
    total_recaudado = total_recaudado + total
    if total > pago_mayor:     
        pago_mayor = total
        placa_mayorPAGO = placa
   
print("total recaudado:", total_recaudado)
print("carros:", es_carro)
print("motos:", es_moto)
print("vehiculo que mas pago:", placa_mayorPAGO, "con", pago_mayor)



    
