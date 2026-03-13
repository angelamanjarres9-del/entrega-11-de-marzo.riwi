
total_dia = 0
cal_corte = 0
cal_cepillado = 0
cal_tintura = 0

for i in range(7):
    nombre = input("Escribe tu nombre: ")
    servicio = input("Cual servicio escoges? (corte, cepillado o tintura): ")
    valor = int(input("Cual fue el valor pagado?: "))
    
    if servicio == "corte":
        cal_corte = cal_corte + 1
        total_dia = total_dia + valor
        
    elif servicio =="cepillado":
        cal_cepillado = cal_cepillado + 1 
        total_dia = total_dia + valor
        
    elif servicio == "tintura":
        cal_tintura = cal_tintura + 1
        total_dia = total_dia + valor
        
print("total del dia:", total_dia)
print("cortes:", cal_corte)
print("cepillados:", cal_cepillado)
print("tinturas:", cal_tintura)

if cal_corte > cal_cepillado and cal_corte > cal_tintura:
    print("el servicio mas solicitado fue corte")
elif cal_cepillado > cal_tintura:
    print("el servicio mas solicitado fue cepillado")
else:
    print("el servicio mas solicitado fue tintura")