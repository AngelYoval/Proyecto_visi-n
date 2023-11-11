import cv2
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QApplication, QSlider, QFileDialog, \
    QSpacerItem, QSizePolicy, QHBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QKeySequence, QAction, QPixmap, QImage


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        #Ventana principal
        self.setWindowTitle("Filtro Promedio ponderado")
        self.setGeometry(100, 100, 800, 600)
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.image_label = QLabel(self)
        self.layout.addWidget(self.image_label)

        button_layout = QHBoxLayout()

        #Boton para subir la imagen
        self.load_button = QPushButton("Cargar Imagen", self)
        self.layout.addWidget(self.load_button)
        button_layout.addWidget(self.load_button)
        self.load_button.clicked.connect(self.load_image)
        self.load_button.setMaximumSize(300,40)

        #Slider del filtro
        self.slider = QSlider()
        self.slider.setOrientation(Qt.Orientation.Horizontal)
        self.slider.setRange(0, 100)
        self.layout.addWidget(self.slider)
        button_layout.addWidget(self.slider)
        self.slider.setMaximumSize(300,40)

        #Boton para aplicar el filtro
        self.apply_button = QPushButton("Aplicar Filtro", self)
        self.layout.addWidget(self.apply_button)
        self.apply_button.clicked.connect(self.apply_filter)
        self.apply_button.setMaximumSize(300,40)
        button_layout.addWidget(self.apply_button)

        self.layout.addLayout(button_layout)
        self.layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)  # Alinea el layout principal en la parte inferior
    def load_image(self):
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("Images (*.png *.xpm *.jpg *.bmp *.tif);;All Files (*)")
        if file_dialog.exec():
            file_name = file_dialog.selectedFiles()[0]
            self.image = cv2.imread(file_name)
            self.display_image(self.image)

    def display_image(self, image):
        if image is not None:
            height, width, channel = image.shape
            bytes_per_line = 3 * width
            q_image = QImage(image.data, width, height, bytes_per_line, QImage.Format.Format_RGB888)
            pixmap = QPixmap.fromImage(q_image)
            self.image_label.setPixmap(pixmap)
            self.image_label.setScaledContents(True)
            self.image_label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
            self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.image_label.setScaledContents(False)  # Evita que la imagen se estire

    def apply_filter(self):
        if self.image is not None:
            intensity = self.slider.value()
            filtered_image = cv2.boxFilter(self.image, -1, (intensity, intensity))
            self.display_image(filtered_image)



app = QApplication([])
ventana = VentanaPrincipal()
ventana.show()

app.exec()