import sys
from simply_linked_list import SimplyLinkedList
from PyQt6.QtWidgets import (QLineEdit, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QApplication, QLabel)

app = QApplication(sys.argv)
list = SimplyLinkedList()


class Simply_Linked_List_Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Lista simplemente enlazada - Estructura de datos')

        self.principal_layout = QVBoxLayout()  # layout de toda la ventana
        self.actions_layout = QVBoxLayout()  # layout con las acciones
        self.info_layout = QVBoxLayout()  # layout con la información de la lista
        self.h_layout = QHBoxLayout()
        self.unshift_layout = QHBoxLayout()
        self.append_layout = QHBoxLayout()
        self.insert_at_layout = QHBoxLayout()
        self.search_layout = QHBoxLayout
        self.buttons_layout = QHBoxLayout()  # layout de los botones de abajo

        self.title = QLabel(self)
        self.title.setText('Listas Simplemente Ligadas')
        self.principal_layout.addWidget(self.title)

        self.unshift_label = QLabel(self)
        self.unshift_label.setText('Insertar al inicio')
        self.actions_layout.addWidget(self.unshift_label)

        self.textbox1 = QLineEdit()
        self.unshift_layout.addWidget(self.textbox1)

        self.unshift_button = QPushButton('Añadir', self)
        self.unshift_layout.addWidget(self.unshift_button)
        self.unshift_button.clicked.connect(self.unshift)

        self.actions_layout.addLayout(self.unshift_layout)

        self.append_label = QLabel(self)
        self.append_label.setText('Insertar al final')
        self.actions_layout.addWidget(self.append_label)

        self.textbox2 = QLineEdit()
        self.append_layout.addWidget(self.textbox2)

        self.append_button = QPushButton('Añadir', self)
        self.append_button.clicked.connect(self.append)
        self.append_layout.addWidget(self.append_button)

        self.actions_layout.addLayout(self.append_layout)

        self.insert_at_label = QLabel(self)
        self.insert_at_label.setText('Insertar en una posición específica')
        self.actions_layout.addWidget(self.insert_at_label)

        self.position_label = QLabel(self)
        self.position_label.setText('Posición                                Elemento')
        self.actions_layout.addWidget(self.position_label)

        self.pos_textbox = QLineEdit()
        self.insert_at_layout.addWidget(self.pos_textbox)

        self.textbox3 = QLineEdit()
        self.insert_at_layout.addWidget(self.textbox3)

        self.insert_at_button = QPushButton('Añadir', self)
        self.insert_at_layout.addWidget(self.insert_at_button)
        self.insert_at_button.clicked.connect(self.insert_at)

        self.actions_layout.addLayout(self.insert_at_layout)

        self.shift_button = QPushButton('Eliminar al inicio', self)
        self.actions_layout.addWidget(self.shift_button)
        self.shift_button.clicked.connect(self.shift)

        self.pop_button = QPushButton('Eliminar al final', self)
        self.actions_layout.addWidget(self.pop_button)
        self.pop_button.clicked.connect(self.pop)

        self.h_layout.addLayout(self.actions_layout)

        self.title1 = QLabel(self)
        self.title1.setText('Datos actuales de la lista:')
        self.info_layout.addWidget(self.title1)

        self.cabeza = QLabel(self)
        self.cabeza.setText('\nCabeza:')
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
        self.cabeza.setText(f"Cabeza: {list.head}")
        self.cola.setText(f"Cola: {list.tail}")
        self.size.setText(f"Tamaño: {list.size}")

    def unshift(self):
        list.unshift(self.textbox1.text())
        self.textbox1.clear()
        self.update_grid()

    def append(self):
        list.append(self.textbox2.text())
        self.textbox2.clear()
        self.update_grid()

    def insert_at(self):
        data = self.textbox3.text()
        pos = self.pos_textbox.text()
        list.insert_at(data, pos)
        self.textbox3.clear()
        self.pos_textbox.clear()
        self.update_grid()

    def shift(self):
        list.shift()
        self.update_grid()

    def pop(self):
        list.pop()
        self.update_grid()
