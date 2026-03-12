filas = int(input("ingresa un numero para la fila: "))
columna = int(input("ingresa un numero para la columna: "))
triangulo = []

for f in range(filas):
    fila = []
    for c in range(columna):
        if f == 0 or c == 0:
            fila.append(1)
        else:
            fila.append(triangulo[f-1][c] + fila[c-1])
    triangulo.append(fila)

for fila in triangulo:
    for numero in fila:
        print(numero, end=" ")
    print()
