# Calcular área y perímetro de un rombo

# Pedir datos al usuario
D = float(input("Ingresa la diagonal mayor: "))
d = float(input("Ingresa la diagonal menor: "))
L = float(input("Ingresa la longitud de un lado: "))

# Calcular área y perímetro
area = (D * d) / 2
perimetro = 4 * L

# Mostrar resultados
print(f"El área del rombo es: {area}")
print(f"El perímetro del rombo es: {perimetro}")
