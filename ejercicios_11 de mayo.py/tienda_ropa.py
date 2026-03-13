agotado = 0
stock_bajo = 0
stock_normal = 0

for i in range(10):
    nombre = input("nombre del producto: ")
    cantidad = int(input("cantidad disponible: "))
    
    if cantidad == 0:
        agotado = agotado + 1
    elif cantidad >= 1 and cantidad <= 5:
        stock_bajo = stock_bajo + 1
    else:
        stock_normal = stock_normal + 1

print("agotados:", agotado)
print("stock bajo:", stock_bajo)
print("stock normal:", stock_normal)

