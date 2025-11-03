# Lista para almacenar las notas (puedes usar números enteros o decimales)
notas = []

# Inicializamos la variable que guardará la opción elegida por el usuario
opcion = None 

# Definición de una función para mostrar el menú
def mostrar_menu():
    """Muestra las opciones del menú principal."""
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Agregar una nota")
    print("2. Mostrar todas las notas")
    print("3. Calcular promedio, mayor y menor")
    print("4. Terminar programa")

# Simulación del bucle principal tipo do-while
while True:
    mostrar_menu()

    try:
        opcion = int(input("Seleccione una opción (1-4): "))
    except ValueError:
        print("🛑 ¡Opción inválida! Por favor, ingrese un número del 1 al 4.")
        continue 

    if opcion == 1:
        # --- Lógica para Agregar una nota con validación de rango ---
        while True:  # Bucle interno para repetir si la nota es inválida
            try:
                nota = float(input("Ingrese la nota a agregar (0 a 100): "))

                # Validar rango lógico
                if nota < 0.0 or nota > 100.0:
                    print("⚠️ La nota debe estar entre 0 y 100. Inténtelo nuevamente.")
                    continue  # Repite el bucle interno

                # Si pasa la validación, se agrega y se sale del bucle
                notas.append(nota)
                print(f"✅ Nota {nota} agregada correctamente.")
                break  # Sale del bucle interno y vuelve al menú principal

            except ValueError:
                print("🛑 ¡Entrada inválida! Debe ingresar un número para la nota.")
                continue  # Repite el bucle interno si no es número

    elif opcion == 2:
        # --- Mostrar todas las notas ---
        if notas:
            print("\n--- LISTA DE NOTAS ---")
            for i, nota in enumerate(notas):
                print(f"Nota #{i+1}: {nota}")
        else:
            print("ℹ️ Aún no hay notas registradas.")

    elif opcion == 3:
        # --- Calcular promedio, mayor y menor ---
        if notas:
            promedio = sum(notas) / len(notas)
            mayor = max(notas)
            menor = min(notas)
            print("\n--- RESULTADOS ---")
            print(f"📊 Promedio de notas: {promedio:.2f}")
            print(f"⭐ Nota más alta: {mayor}")
            print(f"⬇️ Nota más baja: {menor}")
        else:
            print("ℹ️ No hay notas para calcular estadísticas.")

    elif opcion == 4:
        print("👋 Programa finalizado. ¡Hasta luego!")
        break  # Termina el programa

    else:
        print("🛑 Opción fuera de rango. Por favor, elija entre 1 y 4.")
