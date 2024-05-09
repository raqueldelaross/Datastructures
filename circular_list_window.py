import sys
from circular_list import CircularList
from PyQt6.QtWidgets import (QLineEdit, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QApplication,
                             QLabel)

lista = CircularList()
app = QApplication(sys.argv)


class Circular_List_Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Lista circular simple - Estructura de datos')

        self.principal_layout = QVBoxLayout()  # layout de toda la ventana
        self.actions_layout = QVBoxLayout()  # layout con las acciones
        self.info_layout = QVBoxLayout()  # layout con la información de la lista
        self.h_layout = QHBoxLayout()
        self.append_layout = QHBoxLayout()
        self.prepend_layout = QHBoxLayout()
        self.rotate_buttons = QHBoxLayout()
        self.search_layout = QHBoxLayout()
        self.buttons_layout = QHBoxLayout()  # layout de los botones de abajo

        self.title = QLabel(self)
        self.title.setText('Listas Circulares')
        self.principal_layout.addWidget(self.title)

        self.append_label = QLabel(self)
        self.append_label.setText('Insertar al inicio')
        self.actions_layout.addWidget(self.append_label)

        self.textbox1 = QLineEdit()
        self.append_layout.addWidget(self.textbox1)

        self.append_button = QPushButton('Añadir', self)
        self.append_layout.addWidget(self.append_button)
        self.append_button.clicked.connect(self.append)

        self.actions_layout.addLayout(self.append_layout)

        self.prepend_label = QLabel(self)
        self.prepend_label.setText('Insertar al final')
        self.actions_layout.addWidget(self.prepend_label)

        self.textbox2 = QLineEdit()
        self.prepend_layout.addWidget(self.textbox2)

        self.prepend_button = QPushButton('Añadir', self)
        self.prepend_layout.addWidget(self.prepend_button)
        self.prepend_button.clicked.connect(self.prepend)

        self.actions_layout.addLayout(self.prepend_layout)

        self.search_label = QLabel(self)
        self.search_label.setText('Buscar un elemento')
        self.actions_layout.addWidget(self.search_label)

        self.textbox4 = QLineEdit()
        self.search_layout.addWidget(self.textbox4)

        self.search_button = QPushButton('Buscar', self)
        self.search_layout.addWidget(self.search_button)

        self.actions_layout.addLayout(self.search_layout)

        self.rotate = QPushButton('Rotar lista', self)
        self.rotate_buttons.addWidget(self.rotate)
        self.rotate.clicked.connect(self.rotate_list)

        self.actions_layout.addLayout(self.rotate_buttons)

        self.shift_button = QPushButton('Eliminar al inicio', self)
        self.shift_button.clicked.connect(self.shift)
        self.actions_layout.addWidget(self.shift_button)

        self.pop_button = QPushButton('Eliminar al final', self)
        self.pop_button.clicked.connect(self.pop)
        self.actions_layout.addWidget(self.pop_button)

        self.h_layout.addLayout(self.actions_layout)

        self.title1 = QLabel(self)
        self.title1.setText('Datos actuales de la lista:')
        self.info_layout.addWidget(self.title1)

        self.cabeza = QLabel(self)
        self.cabeza.setText('\nCabeza: -')
        self.info_layout.addWidget(self.cabeza)

        self.cola = QLabel(self)
        self.cola.setText('Cola: -')
        self.info_layout.addWidget(self.cola)

        self.size = QLabel(self)
        self.size.setText('Tamaño: -')
        self.info_layout.addWidget(self.size)

        self.h_layout.addLayout(self.info_layout)

        self.principal_layout.addLayout(self.h_layout)

        self.save_list = QPushButton('Guardar lista como archivo')
        self.buttons_layout.addWidget(self.save_list)

        self.principal_layout.addLayout(self.buttons_layout)

        self.widget = QWidget()
        self.widget.setLayout(self.principal_layout)
        self.setCentralWidget(self.widget)

    def update_grid(self):
        self.textbox1.clear()
        self.textbox2.clear()
        self.textbox4.clear()
        self.cabeza.setText(f"Cabeza: {lista.head}")
        self.cola.setText(f"Cola: {lista.tail}")
        self.size.setText(f"Tamaño: {lista.size}")

    def append(self):
        data = self.textbox1.text()
        lista.append(data)
        self.update_grid()

    def prepend(self):
        data = self.textbox2.text()
        lista.prepend(data)
        self.update_grid()

    def shift(self):
        lista.shift()
        self.update_grid()

    def pop(self):
        lista.pop()
        self.update_grid()

    def rotate_list(self):
        lista.rotate()
        self.update_grid()
