numero = int(input("Ingresa sus creditos: "))

if numero <= 79:
    print("Creditos insuficientes, hacer serrvicio.")
elif numero >= 119:
    print("Creditos suficientes, puedes hacer residencias.")
else:
    print("Puedes hacer servicio")