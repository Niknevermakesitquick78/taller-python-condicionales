n1 = float(input("Ingrese nota 1: "))
n2 = float(input("Ingrese nota 2: "))
n3 = float(input("Ingrese nota 3: "))
if n1 < 0 or n1 > 100:
    print("Error: nota inválida")
    exit()
if n2 < 0 or n2 > 100:
    print("Error: nota inválida")
    exit()
if n3 < 0 or n3 > 100:
    print("Error: nota inválida")
    exit()
promedio = (n1 + n2 + n3) / 3
if 90 <= promedio <= 100:
    clasificacion = "Excelente"
elif 80 <= promedio <= 89:
    clasificacion = "Muy bueno"
elif 70 <= promedio <= 79:
    clasificacion = "Bueno"
elif 60 <= promedio <= 69:
    clasificacion = "Supletorio"
else:
    clasificacion = "Reprobado"
print("Notas ingresadas de los poderosos estudiantes:", n1, n2, n3)
print("Promedio:", round(promedio, 2))
print("Clasificación final:", clasificacion)