print("3")
n = int(input("Ingrese un número positivo: "))
if n > 0:
    print(f"Tabla de multiplicar del {n}")
    #Muestra la operación de multiplicar n por i.
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")
else:
    print("Debe ingresar un número positivo.")