vainilla = 0
chocolate = 0
fresa = 0
#ir recorriendo.
for i in range(5):
    sabor = input("ingresa el sabor de tu eleccion (vainilla, chocolate o fresa): ")
    if sabor == "vainilla":
        vainilla = vainilla +1
    elif sabor =="chocolate":
        chocolate = chocolate + 1
    elif sabor == "fresa":
        fresa = fresa + 1


print("las personas que pidieron vainilla fueron: ", vainilla)
print("las personas que pidieron chocolate fuerron: ", chocolate)
print("las personas que pidieron fresa fueron: ", fresa)


        