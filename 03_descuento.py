subtotal = float(input("Ingresa un subtotal guapo:"))
tipo_cliente_155= input("Ingrese el tipo de clinte que es (vip o regular):")
descuento= 0
if tipo_cliente_155 == "vip":
    descuento= subtotal*0.15
elif tipo_cliente_155== "regular":
    if subtotal>=100:
        descuento= subtotal*0.05
    else:
        descuento= 0
else:
    print("Tipo de cliente no valido")
    desuento= 0
total_final = subtotal - descuento
print("subtotal:", subtotal)
print("Descuento aplicado:", descuento)
print ("Total final:", total_final)
