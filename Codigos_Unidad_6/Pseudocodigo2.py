# Pedir al usuario un texto
texto = input("Introduce un texto para analizar: ")

# Inicializar contadores
contador_vocales = 0
contador_consonantes = 0
contador_numeros = 0
contador_otros = 0

# Recorrer cada letra del texto
for i in range(len(texto)):
    caracter = texto[i]
    caracter = caracter.lower()

    if caracter == 'a' or caracter == 'e' or caracter == 'i' or caracter == 'o' or caracter == 'u':
        contador_vocales = contador_vocales + 1
    elif caracter >= 'a' and caracter <= 'z':
        contador_consonantes = contador_consonantes + 1
    elif caracter >= '0' and caracter <= '9':
        contador_numeros = contador_numeros + 1
    else:
        contador_otros = contador_otros + 1

# Mostrar los resultados
print("Vocales:", contador_vocales)
print("Consonantes:", contador_consonantes)
print("Números:", contador_numeros)
print("Otros caracteres:", contador_otros)
