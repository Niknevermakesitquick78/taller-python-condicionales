distancia= float(input("Ingrese la distancia recorrdia en km:"))
hora = int(input("Ingrese la hora del viaje (0-23):"))
total = 1.0
if 6<= hora <= 19:
    tipo_horario= "diruno"
    costo_km= 0.65
else:
    print("Hora invalida mi so")
    costo_km = 0
    tipo_horario = "desconocido"
total += distancia* costo_km
if distancia>10:
    total += 2
print("Horario", tipo_horario)
print("Distancia recorrida", distancia, "km")
print("Debes pagar en total", round(total, 2))
