Algoritmo Sensor
	Definir humedad Como Real
	Definir continuar Como Caracter
	
	Repetir
		Escribir "Ingrese la humedad relativa (%):"
		Leer humedad
		
		Si humedad > 70 Entonces
			Escribir "Humedad alta. Activando ventilador..."
		Sino
			Escribir "Humedad aceptable. No se activa el ventilador."
		FinSi
		
		Escribir "¿Desea medir nuevamente? (S/N):"
		Leer continuar
		
	Hasta Que continuar = "1" O continuar = "1"
	
	Escribir "Fin del programa."
FinAlgoritmo
