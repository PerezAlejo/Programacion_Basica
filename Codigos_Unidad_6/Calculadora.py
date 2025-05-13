import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QHBoxLayout

class TypecastingApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Operaciones con Float")
        self.setGeometry(100, 100, 300, 250)
        
        self.initUI()

    def initUI(self):
        # Crear widgets
        self.label1 = QLabel("Ingresa el primer número:", self)
        self.text_input1 = QLineEdit(self)

        self.label2 = QLabel("Ingresa el segundo número:", self)
        self.text_input2 = QLineEdit(self)

        self.result_label = QLabel("", self)

        # Botones
        self.button_suma = QPushButton("Suma", self)
        self.button_resta = QPushButton("Resta", self)
        self.button_mult = QPushButton("Multiplicación", self)
        self.button_div = QPushButton("División", self)

        # Conectar botones con funciones
        self.button_suma.clicked.connect(self.sumar)
        self.button_resta.clicked.connect(self.restar)
        self.button_mult.clicked.connect(self.multiplicar)
        self.button_div.clicked.connect(self.dividir)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label1)
        layout.addWidget(self.text_input1)
        layout.addWidget(self.label2)
        layout.addWidget(self.text_input2)

        # Layout para botones
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.button_suma)
        button_layout.addWidget(self.button_resta)
        button_layout.addWidget(self.button_mult)
        button_layout.addWidget(self.button_div)

        layout.addLayout(button_layout)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def get_inputs(self):
        try:
            num1 = float(self.text_input1.text())
            num2 = float(self.text_input2.text())
            return num1, num2
        except ValueError:
            QMessageBox.warning(self, "Error", "Por favor ingresa números válidos.")
            return None, None

    def sumar(self):
        num1, num2 = self.get_inputs()
        if num1 is not None:
            resultado = num1 + num2
            self.result_label.setText(f"Resultado: {resultado}")

    def restar(self):
        num1, num2 = self.get_inputs()
        if num1 is not None:
            resultado = num1 - num2
            self.result_label.setText(f"Resultado: {resultado}")

    def multiplicar(self):
        num1, num2 = self.get_inputs()
        if num1 is not None:
            resultado = num1 * num2
            self.result_label.setText(f"Resultado: {resultado}")

    def dividir(self):
        num1, num2 = self.get_inputs()
        if num1 is not None:
            if num2 == 0:
                QMessageBox.warning(self, "Error", "No se puede dividir entre cero.")
            else:
                resultado = num1 / num2
                self.result_label.setText(f"Resultado: {resultado}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = TypecastingApp()
    ventana.show()
    sys.exit(app.exec_())
