# Calcular el área y perímetro de un trapecio isósceles

# Pedir datos al usuario
B = float(input("Ingresa la base mayor: "))
b = float(input("Ingresa la base menor: "))
h = float(input("Ingresa la altura: "))
L = float(input("Ingresa la longitud del lado no paralelo: "))

# Calcular área y perímetro
area = ((B + b) * h) / 2
perimetro = B + b + (2 * L)

# Mostrar resultados
print(f"El área del trapecio isósceles es: {area}")
print(f"El perímetro del trapecio isósceles es: {perimetro}")
