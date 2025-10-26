# Lista para guardar las notas
notas = []

# Bucle principal
while True:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Agregar una nota")
    print("2. Mostrar todas las notas")
    print("3. Calcular promedio, mayor y menor")
    print("4. Terminar programa")

    opcion = input("Seleccione una opción (1-4): ")

    if opcion == "1":
        # Agregar nota
        try:
            nota = float(input("Ingrese la nota (0-10): "))
            if 0 <= nota <= 10:
                notas.append(nota)
                print("✅ Nota agregada correctamente.")
            else:
                print("⚠️ La nota debe estar entre 0 y 10.")
        except ValueError:
            print("⚠️ Por favor, ingrese un número válido.")

    elif opcion == "2":
        # Mostrar todas las notas
        if len(notas) == 0:
            print("📭 No hay notas registradas.")
        else:
            print("📋 Todas las notas:")
            for i, n in enumerate(notas, start=1):
                print(f"Nota {i}: {n}")

    elif opcion == "3":
        # Calcular promedio, mayor y menor
        if len(notas) == 0:
            print("⚠️ No hay notas para calcular.")
        else:
            promedio = sum(notas) / len(notas)
            mayor = max(notas)
            menor = min(notas)
            print(f"📊 Promedio: {promedio:.2f}")
            print(f"🔺 Nota mayor: {mayor}")
            print(f"🔻 Nota menor: {menor}")

    elif opcion == "4":
        # Terminar el programa
        print("👋 Programa finalizado. ¡Hasta luego!")
        break

    else:
        print("❌ Opción no válida. Intente de nuevo.")
