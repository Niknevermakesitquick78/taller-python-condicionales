subtotal = float(input("Ingresa un subtotal guapo: "))
tipo_cliente = input("Ingrese el tipo de cliente que es (vip o regular): ")
descuento = 0
if tipo_cliente == "vip":
    descuento = subtotal * 0.15
elif tipo_cliente == "regular":
    if subtotal >= 100:
        descuento = subtotal * 0.05
else:
    print("Tipo de cliente no válido")
    descuento = 0
total_final = subtotal - descuento
print("Subtotal:", subtotal)
print("Descuento aplicado:", descuento)
print("Total final:", total_final)
