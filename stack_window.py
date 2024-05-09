import sys
import graphviz
from graphviz import Source

from stack import Stack
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtWidgets import (QGraphicsView, QGraphicsScene, QLineEdit, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QPushButton,
                             QApplication, QLabel)

app = QApplication(sys.argv)
dot = graphviz.Digraph(comment='Stack')
stack = Stack()


class StackTransversal(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Otra ventana")
        layout.addWidget(self.label)
        self.setLayout(layout)


class Stack_Window(QMainWindow):
    stack_transversal_ = StackTransversal()

    def __init__(self):
        super().__init__()

        self.setWindowTitle('1. Pila - Estructura de datos')  # Crar ventana

        self.principal_layout = QVBoxLayout()  # Layout general
        self.actions_layout = QVBoxLayout()  # Layout de acciones en la pila
        self.info_layout = QVBoxLayout()  # Layout de información de la pila
        self.h_layout = QHBoxLayout()  # Layout horizontal
        self.buttons_layout = QHBoxLayout()  # Layout de botones de abajo
        self.insert_layout = QHBoxLayout()  # Layout de insertar
        self.search_layout = QHBoxLayout()  # Layout de buscar

        # Título
        self.title = QLabel(self)
        self.title.setText('Pilas')
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

        # Layout con los datos de la pila
        self.title1 = QLabel(self)
        self.title1.setText('Datos actuales de la pila: ')
        self.info_layout.addWidget(self.title1)

        self.head = QLabel(self)
        self.head.setText('\nCabeza: -')
        self.info_layout.addWidget(self.head)

        self.size = QLabel(self)
        self.size.setText('Tamaño: -')
        self.info_layout.addWidget(self.size)

        self.h_layout.addLayout(self.info_layout)

        self.principal_layout.addLayout(self.h_layout)

        self.save_stack = QPushButton('Guardar pila como archivo', self)
        self.buttons_layout.addWidget(self.save_stack)
        # self.save_stack.clicked.connect(self.visualize)

        self.principal_layout.addLayout(self.buttons_layout)

        self.widget = QWidget()
        self.widget.setLayout(self.principal_layout)
        self.setCentralWidget(self.widget)

    def update_grid(self):
        self.head.setText(f"\nCabeza: {stack.head}")
        self.size.setText(f"Tamaño: {stack.size}")

    def insertar(self):
        stack.insert(self.textbox1.text())
        self.textbox1.clear()
        self.update_grid()

    def eliminar(self):
        stack.delete()
        self.update_grid()

    def search(self):
        stack.search(self.textbox2)
