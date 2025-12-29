# Programa sencillo para calcular el promedio de notas

# Pedimos las notas al usuario
nota1 = float(input("Ingresa la primera nota: "))
nota2 = float(input("Ingresa la segunda nota: "))
nota3 = float(input("Ingresa la tercera nota: "))

# Calculamos el promedio
promedio = (nota1 + nota2 + nota3) / 3

# Mostramos el resultado
print("El promedio de las notas es:", promedio)

# Evaluamos si aprueba o no
if promedio >= 7:
    print("¡Felicidades! El estudiante aprobó.")
else:
    print("El estudiante no aprobó.")