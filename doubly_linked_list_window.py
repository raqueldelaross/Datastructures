from typing import TypeVar, Generic
from doubly_linked_list_node import Node

T = TypeVar('T')


class DoublyLinkedList(Generic[T]):
    # Método constructor
    def __init__(self):
        self.head: Node | None = None
        self.tail: Node | None = None
        self.size = 0

    # Cuando la lista esta vacía
    def is_empty(self) -> bool:
        return self.head is None and self.tail is None

    # Agregar si la lista está vacía
    def insert_empty(self, data: T):
        new_node = Node(data)
        self.head = new_node
        self.tail = new_node
        self.size = 1

    # Agregar al inicio
    def append(self, data: T):
        if self.is_empty():
            self.insert_empty(data)
        else:
            new_node = Node(data)
            self.tail = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.size += 1

    # Agregar al inicio
    def prepend(self, data: T):
        if self.is_empty():
            self.insert_empty(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.size += 1

    # Recorrer la lista
    def transversal(self) -> str:
        current = self.head
        result = ''
        while current is not None:
            result += str(current.data) + "x^" + str(self.size-1)
            if current is not self.tail:
                return result
            current = current.next

        return result

    # Recorrer la lista de forma inversa
    def reverse_transversal(self) -> str:
        result = ''
        current = self.tail

        while current is not None:
            result += str(current.data)
            if current is not self.head:
                result += '->'
            current = current.prev

        return result

    # Buscar en una posición específica
    def find_at(self, pos: int) -> Node:
        current_pos = 0
        ref = self.head
        while ref is not None:
            if current_pos == pos:
                return ref
            else:
                ref = ref.next
                current_pos += 1

        raise Exception('No existe la posición')

    # Insertar en una posición específica
    def insert_at(self, pos: int, data: T):
        if pos == 0:
            self.prepend(data)
        elif pos == self.size - 1:
            self.append(data)
        else:
            ref = self.find_at(pos)
            next_node = ref.next
            new_node = Node(data)
            new_node.next = next_node
            new_node.prev = ref
            ref.next = new_node
            next_node.prev = new_node
            self.size += 1

        # if self.is_empty() and pos == 0:
        #     self.append(data)
        # else:
        #     ref = self.find_at(pos)
        #     new_node = Node(data)
        #     new_node.next = ref.next
        #     new_node.prev = ref
        #     ref.next = new_node
        #     self.size += 1

    # Insertar en una posición previa a...
    def insert_at_prev(self, pos: int, data: T):
        new_node = Node(data)
        prev_node = self.find_at(pos)

    # Eliminar al inicio
    def unshift(self) -> Node:
        if self.is_empty():
            raise Exception('La lista esta vacía')
        elif self.head is self.tail:
            ref = self.head
            self.head = None
            self.tail = None
            self.size = 0
            return ref
        else:
            ref = self.head
            self.head = ref.next
            ref.next = None
            self.head.prev = None
            self.size -= 1
            return ref

    # Remover un nodo al final
    def pop(self) -> Node:
        if self.is_empty():
            raise Exception("La lista está vacia")
        elif self.head is self.tail:
            ref = self.tail
            self.head = None
            self.tail = None
            self.size = 0
            return ref
        else:
            ref = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            ref.prev = None
            self.size -= 1
            return ref

    # Remover en una posición específica
    def remove_at(self, pos: int) -> Node:
        if self.is_empty():
            raise Exception('la lista está vacía')
        else:
            ref = self.find_at(pos)
            prev_node = ref.prev
            next_node = ref.next
            ref.prev = None
            ref.next = None
            prev_node.next = next_node
            next_node.prev = prev_node
        return ref

    def __iter__(self):
        self.current_node = self.head
        return self

    def __next__(self):
        if self.current_node is None:
            raise StopIteration
        elif self.current_node is self.tail:
            self.current_node = None
            return self.tail.data
        else:
            current_data = self.current_node.data
            self.current_node = self.current_node.next
            return current_data
