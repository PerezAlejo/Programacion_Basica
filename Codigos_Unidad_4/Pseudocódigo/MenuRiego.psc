Algoritmo MenuRiego
	Definir opcion Como Entero
    Definir humedad Como Real
	
    Repetir
        Escribir "---- MEN� ----"
        Escribir "1. Medir humedad"
        Escribir "2. Salir"
        Escribir "Elija una opci�n:"
        Leer opcion
		
        Si opcion = 1 Entonces
            humedad <- Aleatorio(10, 100)
            Escribir "Humedad actual: ", humedad, "%"
            Si humedad < 40 Entonces
                Escribir "Humedad baja. Activando riego..."
            Sino
                Escribir "Humedad suficiente. No se activa riego."
            FinSi
        FinSi
		
        Si opcion <> 1 Y opcion <> 2 Entonces
            Escribir "Opci�n no v�lida."
        FinSi
		
    Hasta Que opcion = 2
	
    Escribir "Fin del programa."

FinAlgoritmo
