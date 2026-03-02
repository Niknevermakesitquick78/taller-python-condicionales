distancia = float(input("Ingrese la distancia recorrida en km: "))
hora = int(input("Ingrese la hora del viaje (0-23): "))
total = 1.0
if 6 <= hora <= 19:
    tipo_horario = "diurno"
    costo_km = 0.50
elif 0 <= hora <= 23:
    tipo_horario = "nocturno"
    costo_km = 0.65
else:
    print("Hora inválida")
    exit()
total += distancia * costo_km
if distancia > 10:
    total += 2
print("Horario:", tipo_horario)
print("Distancia:", distancia, "km")
print("Total a pagar: $", round(total, 2))
