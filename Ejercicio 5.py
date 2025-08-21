precios = {"Churrasco":1500, "Completo":1000, "Vegetariano":2000, "Barros Luco":3000}
cant = {}
for p in precios:
    cant[p] = int(input(f"Cantidad de {p}: "))
neto = 0
for p in precios:
    neto += precios[p] * cant[p]
iva = neto * 0.19
total = neto + iva
if input("¿Tiene código de descuento? (s/n): ") == "s":
    descuento = total * 0.10
    total -= descuento
else:
    descuento = 0  
print("\n--- BOLETA ---")
for p in precios:
    if cant[p] > 0:
        print(f"{p} x{cant[p]} = ${precios[p]*cant[p]}")
print(f"Neto: ${neto}")
print(f"IVA: ${iva}")
if descuento > 0:
    print(f"Descuento (10%): -${descuento}")
print(f"TOTAL A PAGAR: ${total}")
