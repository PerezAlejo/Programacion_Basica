import time  # Para pausas
from Archivos import guardar_diccionarios_en_csv, leer_diccionarios_de_csv
archivo = "dulces.csv"
# Lista de productos con precios e inventario

dulces =[ 
    {"Chocolate": [15, 1]},
    {"Gomitas": [10, 1]},
    {"Paleta": [5, 1]}
]

def mostrar_menu():
    print("\n--- Menú ---")
    print("1. Ver productos")
    print("2. Comprar dulce")
    print("3. Salir")

def ver_productos():
    for dulce, datos in dulces.items():
        print(f"{dulce}: ${datos[0]} - Stock: {datos[1]}")

def comprar_dulce():
    ver_productos()
    producto = input("¿Cuál quieres comprar? ")
    if producto in dulces and dulces[producto][1] > 0:
        print(f"Compraste {producto}. ¡Disfruta!")
    else:
        print("No disponible.")

def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")
        if opcion == "1":
            ver_productos()
        elif opcion == "2":
            comprar_dulce()
        elif opcion == "3":
            print("¡Gracias por tu compra!")
            break
        else:
            print("Opción no válida.")
        time.sleep(1)

if __name__ == "__main__":
    main()

datos = [
    {"Nombre": "Juan", "Edad": 25, "Ciudad": "Madrid"},
    {"Nombre": "Ana", "Edad": 30, "Ciudad": "Barcelona"},
    {"Nombre": "Luis", "Edad": 35, "Ciudad": "Valencia"}
]

archivo = "ExamenP3.py"

guardar_diccionarios_en_csv(archivo, dulces)

datos_leidos = leer_diccionarios_de_csv(archivo)
print("Datos leidos del archivo csv:")
print(datos_leidos)