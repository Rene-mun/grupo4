# Ingreso de datos: el programa pide al usuario cuántos productos de cada tipo va a comprar
print("4")
mascarillas = int(input("Cantidad de mascarillas : "))
guantes = int(input("Cantidad de guantes : "))
delantal = int(input("Cantidad de delantales : "))
amonio = int(input("Cantidad de amonio : "))

# Calcula el subtotal multiplicando la cantidad de cada producto por su precio
subtotal = (mascarillas * 1000 +
            guantes * 1000 +
            delantal * 2000 +
            amonio * 3000)

print(f"\nValor inicial: ${subtotal}")
# Pregunta si tiene código de descuento
tiene_descuento = input("¿Tiene código de descuento? (S/N): ").upper()
if tiene_descuento == "S":
    descuento = float(input("Ingrese el porcentaje de descuento (%): "))
    subtotal -= subtotal * (descuento / 100)

# Cálculo del IVA
iva = subtotal * 0.19
total = subtotal + iva

# Muestra los resultados 0f → muestra el número como decimal con formato de flotante pero con 0 decimales
print(f"\nSubtotal con descuento: ${subtotal:,.0f}")
print(f"IVA (19%): ${iva:,.0f}")
print(f"TOTAL A PAGAR: ${total:,.0f}")