from PyQt6.QtWidgets import QMessageBox
from typing import TypeVar, Generic
from stack_node import Node

T = TypeVar('T')


class Queue(Generic[T]):
    def __init__(self):
        self.max: max = -1
        self.size: int = 0
        self.head: Node | None = None
        self.tail: Node | None = None

    def is_empty(self):
        return self.head is None and self.tail is None

    def insert(self, data: T):
        if self.max != -1 and self.size >= self.max:
            QMessageBox.setText('Desbordamiento de pila')
            QMessageBox.exec()
            raise Exception('Desbordamiento de pila')

        if self.is_empty():
            new_node = Node(data)
            self.head = new_node
            self.tail = new_node
            self.size += 1
        else:
            new_node = Node(data)
            self.tail.next = new_node
            self.tail = new_node
            self.size += 1

    def delete(self):
        if self.is_empty():
            self.tail = None
            raise Exception('Subdesbordamiento de cola')

        if self.head is self.tail:
            current = self.head
            self.head = None
            current.next = None
            self.size = 0

            return current.data
        else:
            current = self.head
            self.head = current.next
            current.next = None
            self.size -= 1

            return current.data

    def transversal(self) -> str:
        current = self.head
        result = ''
        while current is not None:
            result += str(current)
            if current is not self.tail:
                result += '\n⤷ '
            current = current.next

        return result

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
