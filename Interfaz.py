import cv2
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QApplication, QSlider, QFileDialog
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QKeySequence, QAction, QPixmap

class VentanaPrincipal(QMainWindow):
    def __int__(self):
        super().__int__()
        #Ventana principal
        self.setWindowTitle("Filtro Promedio ponderado")
        self.setGeometry(100, 100, 800, 600)
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.image_label = QLabel(self)
        self.layout.addWidget(self.image_label)

        #Boton para subir la imagen
        self.load_button = QPushButton("Cargar Imagen", self)
        self.layout.addWidget(self.load_button)

        #Slider del filtro
        self.slider = QSlider()
        self.slider.setOrientation(Qt.Orientation.Horizontal)
        self.slider.setRange(0, 100)
        self.layout.addWidget(self.slider)

        #Boton para aplicar el filtro
        self.apply_button = QPushButton("Aplicar Filtro", self)
        self.layout.addWidget(self.apply_button)

        self.apply_button.clicked.connect(self.apply_filter)

app = QApplication([])
ventana = VentanaPrincipal()
ventana.show()

app.exec()