from typing import Optional, TypeVar, Generic
from circular_list_node import Node

T = TypeVar('T')


class CircularList(Generic[T]):
    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self.size: int = 0

    def append(self, data: T):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node

        else:
            self.tail.next = new_node
        self.tail = new_node
        self.tail.next = self.head
        self.size += 1

    def find_by(self, data: T) -> Node:
        current = self.head

        while current is not self.tail:
            if current.data == data:
                return current
            else:
                current = current.next
        if self.tail.data == data:
            return current
        else:
            raise Exception('El elemento no Existe')

    def find_at(self, pos: T) -> Node:
        current = self.head
        iteration = 0

        while iteration < self.size:
            if iteration is pos:
                return current
            else:
                iteration += 1
                current = current.next

        raise Exception('La posicion que ingreso no existe')

    def is_empty(self) -> bool:
        return self.head is None and self.tail is None and self.size == 0

    def insert_at(self, data: T, pos: int):
        new_node = Node(data)
        if self.is_empty():
            raise Exception('La lista esta vacia')
        elif pos == 0:
            self.prepend(data)
        else:
            position = self.find_at(pos)
            previous = self.find_at(pos-1)
            previous.next = new_node
            new_node.next = position

    def pop(self):
        current1 = self.tail
        if self.is_empty():
            raise Exception('Lista Vacia')
        elif self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            current = self.find_at(self.size - 2)
            current.next = self.head
            self.tail.next = None
            self.tail = current

        self.size -= 1
        return current1

    def prepend(self, data: T):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.tail.next = self.head
        self.size += 1

    def shift(self):
        if self.is_empty():
            raise Exception('Lista Vacia')
        elif self.head is self.tail:
            current = self.head
            self.head = None
            self.tail = None
            self.size -= 1
            return current
        else:
            current = self.head
            self.head = current.next
            self.tail.next = None
            current.next = None
            self.tail.next = self.head
            self.size -= 1

            return current

    def traversal(self) -> str:
        result = ''
        current = self.head
        while current is not self.tail:
            result += str(current.data) + '->'
            current = current.next

        if current is not None:
            result += str(self.tail.data)

        return result

    def rotate(self):
        tail = self.find_at(self.size - 2)

        self.head = self.tail
        self.tail = tail
