import sys
from queue import Queue
from PyQt6.QtWidgets import (QLineEdit, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QApplication, QLabel)

app = QApplication(sys.argv)
queue = Queue()


class Queue_Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Cola - Estructura de datos')  # Crar ventana

        self.principal_layout = QVBoxLayout()  # Layout general
        self.actions_layout = QVBoxLayout()  # Layout de acciones en la cola
        self.info_layout = QVBoxLayout()  # Layout de información de la cola
        self.h_layout = QHBoxLayout()  # Layout horizontal
        self.buttons_layout = QHBoxLayout()  # Layout de botones de abajo
        self.insert_layout = QHBoxLayout()  # Layout de insertar
        self.search_layout = QHBoxLayout()  # Layout de buscar

        # Título
        self.title = QLabel(self)
        self.title.setText('Colas')
        self.principal_layout.addWidget(self.title)

        # Opción de agregar a la pila
        self.insert_label = QLabel(self)
        self.insert_label.setText('Agregar un elemento')
        self.actions_layout.addWidget(self.insert_label)

        self.textbox1 = QLineEdit()
        self.insert_layout.addWidget(self.textbox1)

        self.insert = QPushButton('Agregar', self)
        self.insert_layout.addWidget(self.insert)
        self.insert.clicked.connect(self.insertar)

        self.actions_layout.addLayout(self.insert_layout)

        # Opción de buscar en la pila
        self.search_label = QLabel(self)
        self.search_label.setText('Buscar un elemento')
        self.actions_layout.addWidget(self.search_label)

        self.textbox2 = QLineEdit()
        self.search_layout.addWidget(self.textbox2)

        self.search_button = QPushButton('Buscar', self)
        self.search_layout.addWidget(self.search_button)

        self.actions_layout.addLayout(self.search_layout)

        # Opción de eliminar
        self.delete = QPushButton('Eliminar elemento', self)
        self.actions_layout.addWidget(self.delete)
        self.delete.clicked.connect(self.eliminar)

        self.h_layout.addLayout(self.actions_layout)

        # Layout con los datos de la cola
        self.title1 = QLabel(self)
        self.title1.setText('Datos actuales de la cola: ')
        self.info_layout.addWidget(self.title1)

        self.head = QLabel(self)
        self.head.setText('\nCabeza: -')
        self.info_layout.addWidget(self.head)

        self.tail = QLabel(self)
        self.tail.setText('Cola: -')
        self.info_layout.addWidget(self.tail)

        self.size = QLabel(self)
        self.size.setText('Tamaño: -')
        self.info_layout.addWidget(self.size)

        self.h_layout.addLayout(self.info_layout)

        self.principal_layout.addLayout(self.h_layout)

        self.save_queue = QPushButton('Guardar cola como archivo', self)
        self.buttons_layout.addWidget(self.save_queue)

        self.principal_layout.addLayout(self.buttons_layout)

        self.widget = QWidget()
        self.widget.setLayout(self.principal_layout)
        self.setCentralWidget(self.widget)

    def update_grid(self):
        self.head.setText(f"\nCabeza: {queue.head}")
        self.size.setText(f"Tamaño: {queue.size}")
        self.tail.setText(f"Cola: {queue.tail}")


    def insertar(self):
        queue.insert(self.textbox1.text())
        self.textbox1.clear()
        self.update_grid()

    def eliminar(self):
        queue.delete()
        self.update_grid()
        if self.head is None:
            self.tail = None
        else:
            self.tail.setText(f"Cola: {queue.head}")