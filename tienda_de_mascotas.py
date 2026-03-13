print("Bienvenido a peg feliz")
cal_alimento = 0
cal_juguetes = 0
cal_accesorios= 0

for i in range (10):
    categoria = input("Que categoria deseas comprar? (alimento,juguetes o accesorios")
    valor = int(input("cuanto vale el valor de tu compra?: "))
    
    if categoria == "alimento":
        cal_alimento = cal_alimento + valor
    
    elif categoria == "juguetes":
        cal_juguetes = cal_juguetes + valor
        
    elif categoria == "accesorios":
        cal_accesorios = cal_accesorios + valor
    
    print("total de la categoria alimentos",cal_alimento)
    print("total de la categoria juguetes",cal_juguetes)
    print("total de la categoria accesorios",cal_accesorios)
    


if cal_alimento > cal_juguetes and cal_alimento > cal_accesorios:
    print("la categoria que mas vendio fue alimento")
elif cal_juguetes > cal_accesorios:
    print("la categoria que mas vendio fue juguetes")
else:
    print("la categoria que mas vendio fue accesorios")
    