edad =int(input("para ingresar al gym, necesito que me digas tu edad: "))

if edad < 13:
    print(" no puedes ingresar al gym, no cumples con la edad minima")
elif edad >= 13 and edad < 18:
    print("eres clase juvenil")
elif edad >= 18 and edad < 60:
    print("eres clase adulto")
else:
    edad >= 60
    print("eres clase senior")

