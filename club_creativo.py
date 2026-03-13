print("Bienvenido al club creativo Angela")
total_recaudado = 0
cal_basico = 0
cal_premium = 0
cal_familiar = 0

basico = 50000
premium = 90000
familiar = 130000

seleccion = ""

while seleccion != "salir":
    nombre = input("nombre (o salir): ")
    if nombre == "salir":
        break
    edad = int(input("edad: "))
    plan = input("tipo de plan (basico, premium, familiar): ")
    
    if edad < 18:
        print("registro juvenil")
    elif edad >= 60:
        print("beneficio senior")
    
    if plan == "basico":
        total_recaudado = total_recaudado + basico
        cal_basico = cal_basico + 1
    elif plan == "premium":
        total_recaudado = total_recaudado + premium
        cal_premium = cal_premium + 1
    elif plan == "familiar":
        total_recaudado = total_recaudado + familiar
        cal_familiar = cal_familiar + 1

print("total recaudado:", total_recaudado)
print("planes basico:", cal_basico)
print("planes premium:", cal_premium)
print("planes familiar:", cal_familiar)

if cal_basico > cal_premium and cal_basico > cal_familiar:
    print("plan mas vendido: basico")
elif cal_premium > cal_familiar:
    print("plan mas vendido: premium")
else:
    print("plan mas vendido: familiar")
