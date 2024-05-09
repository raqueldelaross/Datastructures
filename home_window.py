import sys
from stack_window import Stack_Window
from queue_window import Queue_Window
from binary_tree_window import Binary_Tree_Window
from search_tree_window import Search_Tree_Window
from circular_list_window import Circular_List_Window
from doubly_linked_list_window import Doubly_Linked_List_Window
from simply_linked_list_window import Simply_Linked_List_Window
from circular_doubly_list_window import Circular_Doubly_List_Window
from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QPushButton, QApplication, QLabel)

stack = Stack_Window()
queue = Queue_Window()
binary_tree = Binary_Tree_Window()
circular_list = Circular_List_Window()
search_tree_window = Search_Tree_Window()
doubly_linked_list = Doubly_Linked_List_Window()
simply_linked_list = Simply_Linked_List_Window()
circular_doubly_linked_list = Circular_Doubly_List_Window()
app = QApplication(sys.argv)


class Home(QMainWindow):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()  # Layout con los botones de acceso

        # Crear ventana
        self.setWindowTitle('INICIO')

        # Label de título
        self.title = QLabel(self)
        self.title.setText('Estructuras dinámicas de datos:')

        # Crear botones
        self.stack = QPushButton('Pilas', self)
        self.stack.clicked.connect(self.goto_stack)

        self.queue = QPushButton('Colas', self)
        self.queue.clicked.connect(self.goto_queue)

        self.simply_linked_list = QPushButton('Listas simplemente ligadas', self)
        self.simply_linked_list.clicked.connect(self.goto_simply_linked_list)

        self.circular_list = QPushButton('Listas circulares', self)
        self.circular_list.clicked.connect(self.goto_circular_list)

        self.doubly_linked_list = QPushButton('Listas doblemente ligadas', self)
        self.doubly_linked_list.clicked.connect(self.goto_doubly_linked_list)

        self.circular_doubly_linked_list = QPushButton('Listas circulares doblemente ligadas', self)
        self.circular_doubly_linked_list.clicked.connect(self.goto_circular_doubly_linked_list)

        self.binnary_tree = QPushButton('Árboles binarios', self)
        self.binnary_tree.clicked.connect(self.goto_binnary_tree)

        self.search_tree = QPushButton('Árboles de búsqueda', self)
        self.search_tree.clicked.connect(self.goto_search_tree)

        # Agregar al layout
        self.layout.addWidget(self.title)
        self.layout.addWidget(self.stack)
        self.layout.addWidget(self.queue)
        self.layout.addWidget(self.simply_linked_list)
        self.layout.addWidget(self.circular_list)
        self.layout.addWidget(self.doubly_linked_list)
        self.layout.addWidget(self.circular_doubly_linked_list)
        self.layout.addWidget(self.binnary_tree)
        self.layout.addWidget(self.search_tree)

        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)

    def goto_stack(self):
        stack.show()

    def goto_queue(self):
        queue.show()

    def goto_simply_linked_list(self):
        simply_linked_list.show()

    def goto_circular_list(self):
        circular_list.show()

    def goto_doubly_linked_list(self):
        doubly_linked_list.show()

    def goto_circular_doubly_linked_list(self):
        circular_doubly_linked_list.show()

    def goto_binnary_tree(self):
        binary_tree.show()

    def goto_search_tree(self):
        search_tree_window.show()
