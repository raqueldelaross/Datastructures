from PyQt6.QtWidgets import QMessageBox
from typing import TypeVar, Generic
from stack_node import Node

T = TypeVar('T')


class Stack(Generic[T]):
    def __init__(self):
        self.size: int = 0
        self.max: max = -1
        self.head: Node | None = None

    def insert(self, data: T):
        if self.max == -1 or self.size < self.max:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            self.size += 1
        else:
            QMessageBox.setText('Desbordamiento de pila')
            QMessageBox.exec()
            raise Exception('Desbordamiento de pila')

    def delete(self):
        if self.head is None:
            QMessageBox.setText('Subdesbordamiento de pila')
            QMessageBox.exec()
            raise Exception('Subdesbordamiento de pila')
        else:
            current = self.head
            self.head = self.head.next
            self.head = current.next
            current.next = None
            self.size -= 1
            return current.data

    def transversal(self) -> str:
        result = ''
        current = self.head

        while current is not None:
            result += str(current)
            if current.next is not None:
                result += '\n↓\n'

            current = current.next

        return result

    def search(self, data) -> int:
        current = self.head
        accessed_nodes = 0
        while accessed_nodes < self.size:
            if data == current.data:
                return accessed_nodes
            else:
                current = current.siguiente
                accessed_nodes += 1

    def visualize(self):
        # Grafica
        dot = Digraph()
        dot.attr(rankdir='LR')
        current = lista.head
        n = 0
        while current is not None:
            if buscar is None:
                dot.node(str(n), str(current.data), shape='box')
            else:
                if buscar.data == current.data:
                    dot.node(str(n), str(current.data), shape='box', fillcolor='yellow', style='filled')
                else:
                    dot.node(str(n), str(current.data), shape='box')
            if current.next is not None:
                dot.edge(str(n), str(n + 1), dir='forward')
            current = current.next
            n += 1
        source = Source(dot.source)
        scene = QGraphicsScene()
        view = QGraphicsView(scene)
        self.diagram_layout.addWidget(view)
        scene.addPixmap(QPixmap.fromImage(QImage.fromData(source.pipe(format='png'))))
        self.show()

    def is_empty(self):
        return self.head is None

    def __iter__(self):
        self._current_node = self.head
        return self

    def __next__(self):
        if self._current_node is None:
            raise StopIteration
        else:
            current_data = self._current_node.data
            self._current_node = self._current_node.next
            return current_data
