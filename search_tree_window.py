import sys
from search_tree import BinaryTree
from PyQt6.QtWidgets import (QLineEdit, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QApplication, QLabel)

app = QApplication(sys.argv)
tree = BinaryTree()


class Search_Tree_Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Árbol de búsqueda - Estructura de datos')

        self.principal_layout = QHBoxLayout()
        self.actions = QVBoxLayout()
        self.info = QVBoxLayout()
        self.insertlayout1 = QHBoxLayout()
        self.insertlayout2 = QHBoxLayout()
        self.searchlayout = QHBoxLayout()
        self.buttons = QHBoxLayout()
        self.vertical = QVBoxLayout()

        self.widget = QWidget()
        self.widget.setLayout(self.vertical)
        self.setCentralWidget(self.widget)

        self.title = QLabel(self)
        self.title.setText('Árboles binarios')
        self.actions.addWidget(self.title)

        self.insertlabel1 = QLabel(self)
        self.insertlabel1.setText('Insertar a la izquierda: ')
        self.actions.addWidget(self.insertlabel1)

        self.textbox1 = QLineEdit(self)
        self.insertlayout1.addWidget(self.textbox1)

        self.insertbutton1 = QPushButton('Añadir', self)
        self.insertbutton1.clicked.connect(self.insert_left_method)
        self.insertlayout1.addWidget(self.insertbutton1)

        self.actions.addLayout(self.insertlayout1)

        self.insertlabel2 = QLabel(self)
        self.insertlabel2.setText('Insertar a la derecha: ')
        self.actions.addWidget(self.insertlabel2)

        self.textbox2 = QLineEdit(self)
        self.insertlayout2.addWidget(self.textbox2)

        self.insertbutton2 = QPushButton('Añadir', self)
        self.insertbutton2.clicked.connect(self.insert_right_method)
        self.insertlayout2.addWidget(self.insertbutton2)

        self.actions.addLayout(self.insertlayout2)

        self.searchlabel = QLabel(self)
        self.searchlabel.setText('Buscar un valor')
        self.actions.addWidget(self.searchlabel)

        self.textbox3 = QLineEdit(self)
        self.searchlayout.addWidget(self.textbox3)

        self.searchbutton = QPushButton('Buscar', self)
        # self.searchbutton.clicked.connect()
        self.searchlayout.addWidget(self.searchbutton)

        self.actions.addLayout(self.searchlayout)

        self.deletebutton = QPushButton('Eliminar', self)
        # self.deletebutton.clicked.connect()
        self.buttons.addWidget(self.deletebutton)

        self.visualizar = QPushButton('Visualizar árbol', self)
        # self.visualizar.clicked.connect()
        self.buttons.addWidget(self.visualizar)

        self.guardar = QPushButton('Guardar como archivo', self)
        # self.guardar.clicked.connect()
        self.buttons.addWidget(self.guardar)

        self.label = QLabel(self)
        self.label.setText('Datos actuales del árbol')
        self.info.addWidget(self.label)

        self.root = QLabel(self)
        self.root.setText('Raíz: -')
        self.info.addWidget(self.root)

        self.preorder = QLabel(self)
        self.preorder.setText('Recorrido en preorden: -')
        self.info.addWidget(self.preorder)

        self.principal_layout.addLayout(self.actions)
        self.principal_layout.addLayout(self.info)

        self.vertical.addLayout(self.principal_layout)
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

