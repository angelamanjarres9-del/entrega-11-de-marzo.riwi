n = int(input("Ingrese un numero: "))


a = 0
b = 1


for i in range (0,n +1, 1):
    if i == 0:
        print(a)
    elif i == 1:
        print(b)
    else:
        c = a + b
        a = b
        b = c
        print(c)
