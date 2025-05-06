def sensor():
    while True:
        try:
            humedad = float(input("Ingrese la humedad relativa (%): "))
        except ValueError:
            print("Por favor, ingrese un valor numérico válido.")
            continue

        if humedad > 70:
            print("Humedad alta. Activando ventilador...")
        else:
            print("Humedad aceptable. No se activa el ventilador.")

        continuar = input("¿Desea medir nuevamente? (S/N): ").strip().upper()
        if continuar != "S":
            break

    print("Fin del programa.")


sensor()