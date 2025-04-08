import random
def menu_riego():
    while True:
        print("---- MENÚ ----")
        print("1. Medir humedad")
        print("2. Salir")
        opcion = input("Elija una opción: ")

        if opcion == "1":
            humedad = random.randint(10, 100)
            print(f"Humedad actual: {humedad}%")
            if humedad <= 40:
                print("Humedad baja. Activando riego...")
            else:
                print("Humedad suficiente. No se activa riego.")
        elif opcion == "2":
            print("Fin del programa.")
            break
        else:
            print("Opción no válida.")
menu_riego()