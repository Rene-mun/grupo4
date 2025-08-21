nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
genero = input("Ingrese su genero (Varón/Mujer): ")
numero_celular = input("Ingrese su número de celular: ")

if genero.lower() in ["varón", "varon"]:
    print(f"\nNombre: {nombre}")
    print(f"Edad: {edad}")
elif genero.lower() == "mujer":
    print(f"\nNombre: {nombre}")
    print(f"Número de celular: {numero_celular}")
else:
    print("\nGénero no reconocido. Por favor, ingresa 'Varón' o 'Mujer'.")