import sys
from binary_tree import BinaryTree
from PyQt6.QtWidgets import (QLineEdit, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QApplication, QLabel)

tree = BinaryTree()
app = QApplication(sys.argv)


class Binary_Tree_Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Árbol Binario - Estructura de datos')

        self.actions = QVBoxLayout()
        self.info = QVBoxLayout()
        self.vertical = QVBoxLayout()
        self.principal = QHBoxLayout()
        self.insert_right = QHBoxLayout()
        self.insert_left = QHBoxLayout()
        self.search = QHBoxLayout()
        self.buttons = QHBoxLayout()

        self.widget = QWidget()
        self.widget.setLayout(self.vertical)
        self.setCentralWidget(self.widget)

        self.title = QLabel(self)
        self.title.setText('Árboles binarios')
        self.actions.addWidget(self.title)

        self.right_label = QLabel(self)
        self.right_label.setText('Insertar a la derecha')
        self.actions.addWidget(self.right_label)

        self.textbox1 = QLineEdit()
        self.insert_right.addWidget(self.textbox1)

        self.insert_right_button = QPushButton('Añadir', self)
        self.insert_right.addWidget(self.insert_right_button)
        self.insert_right_button.clicked.connect(self.insert_right_method)

        self.actions.addLayout(self.insert_right)

        self.left_label = QLabel(self)
        self.left_label.setText('Insertar a la izquierda')
        self.actions.addWidget(self.left_label)

        self.textbox2 = QLineEdit()
        self.insert_left.addWidget(self.textbox2)

        self.insert_left_button = QPushButton('Añadir', self)
        self.insert_left.addWidget(self.insert_left_button)
        self.insert_left_button.clicked.connect(self.insert_left_method)

        self.actions.addLayout(self.insert_left)

        self.search_label = QLabel(self)
        self.search_label.setText('Buscar un valor')
        self.actions.addWidget(self.search_label)

        self.textbox3 = QLineEdit()
        self.search.addWidget(self.textbox3)

        self.search_button = QPushButton('Buscar', self)
        self.search.addWidget(self.search_button)
        # self.insert_left_button.clicked.connect()
        self.actions.addLayout(self.search)

        self.eliminar = QPushButton('Eliminar', self)
        self.buttons.addWidget(self.eliminar)
        # self.insert_left_button.clicked.connect()

        self.guardar = QPushButton('Guardar como archivo', self)
        self.buttons.addWidget(self.guardar)
        # self.insert_left_button.clicked.connect()

        self.principal.addLayout(self.actions)

        self.title1 = QLabel(self)
        self.title1.setText('Datos actuales del árbol')
        self.info.addWidget(self.title1)

        self.root = QLabel(self)
        self.root.setText('Raíz: -')
        self.info.addWidget(self.root)

        self.preorder = QLabel(self)
        self.preorder.setText(f"Recorrido en preorden: -")
        self.info.addWidget(self.preorder)

        self.principal.addLayout(self.info)

        self.vertical.addLayout(self.principal)
        self.vertical.addLayout(self.buttons)

    def update_grid(self):
        self.root.setText(f"Raíz: {tree.return_root}")
        self.preorder.setText(f"Recorrido en preorden: {tree.preorder()}")

    def insert_right_method(self):
        tree.insert_right(self.textbox1.text(), tree.return_root())
        self.textbox1.clear()
        self.update_grid()

    def insert_left_method(self):
        tree.insert_left(self.textbox2.text(), tree.return_root())
        self.textbox2.clear()
        self.update_grid()

    def delete(self):
        pass