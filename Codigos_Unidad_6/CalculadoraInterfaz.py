import tkinter as tk
from tkinter import messagebox

# Funciones matemáticas corregidas
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"

# Función para obtener entrada, ejecutar operación y mostrar resultado
def calcular(operacion):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        if operacion == 'suma':
            resultado = suma(num1, num2)
        elif operacion == 'resta':
            resultado = resta(num1, num2)
        elif operacion == 'multiplicacion':
            resultado = multiplicacion(num1, num2)
        elif operacion == 'division':
            resultado = division(num1, num2)

        resultado_label.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese números válidos.")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")

# Etiquetas y campos de entrada
tk.Label(ventana, text="Primer número:").grid(row=0, column=0, padx=5, pady=5)
entry1 = tk.Entry(ventana)
entry1.grid(row=0, column=1)

tk.Label(ventana, text="Segundo número:").grid(row=1, column=0, padx=5, pady=5)
entry2 = tk.Entry(ventana)
entry2.grid(row=1, column=1)

# Botones para cada operación
tk.Button(ventana, text="Suma", command=lambda: calcular('suma')).grid(row=2, column=0, padx=5, pady=5)
tk.Button(ventana, text="Resta", command=lambda: calcular('resta')).grid(row=2, column=1, padx=5, pady=5)
tk.Button(ventana, text="Multiplicación", command=lambda: calcular('multiplicacion')).grid(row=3, column=0, padx=5, pady=5)
tk.Button(ventana, text="División", command=lambda: calcular('division')).grid(row=3, column=1, padx=5, pady=5)

# Etiqueta para mostrar el resultado
resultado_label = tk.Label(ventana, text="Resultado: ")
resultado_label.grid(row=4, column=0, columnspan=2, pady=10)

# Ejecutar la interfaz
ventana.mainloop()
