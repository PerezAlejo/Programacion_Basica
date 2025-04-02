# Herencia
# Clase base o padre
class Camionetas:
    def __init__(self, Tipo_de_Traccion, Capacidad_de_carga, Motor, Transmision, Suspension):
        self.Tipo_de_Traccion = Tipo_de_Traccion
        self.Capacidad_de_carga = Capacidad_de_carga
        self.Motor = Motor
        self.Transmision = Transmision
        self.Suspension = Suspension

    def presentarse(self):
        return f"Camioneta Ranger 1994, tiene una traccion {self.Tipo_de_Traccion} y su capacidad de carga es de {self.Capacidad_de_carga}, su motor es un¨{self.Motor}, su transmision es {self.Transmision}, su sus pension es {self.Suspension}."

# Clase derivada o hija
class PickUp(Camionetas):
    def __init__(self,Tipo_de_Traccion, Capacidad_de_carga, Motor, Transmision, Suspension, Caja_Carga, Remolque):
        super().__init__(Tipo_de_Traccion, Capacidad_de_carga, Motor, Transmision, Suspension )  # Llamada al constructor de la clase padre
        self.Caja_Carga = Caja_Carga
        self.Remolque = Remolque

    def presentarse(self):
        # Sobrescribimos el método de la clase padre
        return f"Nissan D21 su capacidad de carga es{self.Caja_Carga}, la capacidad de remolque es de {self.Remolque}."

# Otra clase derivada
class PickUp_Laboral(Camionetas):
    def __init__(self,Tipo_de_Traccion, Capacidad_de_carga, Motor, Transmision, Suspension, Resistencia, Capacidad_de_Remolque):
        super().__init__(Tipo_de_Traccion, Capacidad_de_carga, Motor, Transmision, Suspension )
        self.Resistencia = Resistencia
        self.Capacidad_de_Remolque = Capacidad_de_Remolque

    def presentarse(self):
        return f"Nissan Frontier 2022 su resistencia es de {self.Resistencia}, su capacidad de remolque es de {self.Capacidad_de_Remolque}."

# Programa principal
if __name__ == "__main__":
    Camionetas = Camionetas("4x4", "700kg", "4.0L V6", "Manual 5 veocidades", "Twin I-Beam")
    PickUp = PickUp("4x4", "2,200KG", "3.0L V6", "Manual 5 velocidades", "Suspensión independiente", "Caja Corta", "2,000KG")
    PickUp_Laboral = PickUp_Laboral( "4x4", "3,000KG", "3.5L V6", "Manual 5 velocidades", "Suspensión McPherson", "Alta", "3,500KG" )

    print(Camionetas.presentarse())
    print(PickUp.presentarse())
    print(PickUp_Laboral.presentarse())