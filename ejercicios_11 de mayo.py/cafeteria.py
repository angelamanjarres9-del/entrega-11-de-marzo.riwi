

bebida = input("bienvenido a la cafeteria, que clase deseas (cafe, te o jugo): ")
cantidad = int(input("cuantas unidades deseas comprar? "))


if bebida == "cafe":
    total = 4000 * cantidad
    print("debes pagar",total)
elif bebida== "te":
    total = 3500 * cantidad
    print("debes pagar", total )
elif bebida == "jugo":
    total = 5000* cantidad
    print("debes pagar", total)



