from simply_linked_list_node import Node


class SimplyLinkedList:
    # Método constructor
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    # Si la lista está vacía
    def is_empty(self):
        return self.head is None and self.tail is None

    # Insertar al inicio
    def unshift(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            self.size += 1
        else:
            new_node.next = self.head
            self.head = new_node
            self.size += 1

    # Insertar al final
    def append(self, data):
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

    # Insertar en una posición específica
    def insert_at(self, data, index):
        if index == 0:
            self.unshift(data)
        elif self.is_empty():
            self.unshift(data)
        elif index == self.size:
            self.append(data)
        else:
            new_node = Node(data)
            previous = self.find_at(index - 1)
            new_node.next = previous.next
            previous.next = new_node
            return new_node

    # Buscar elemento por valor
    def find_by(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                return current
            else:
                current = current.next
        raise Exception("El elemento no esta en la cola")

    # Buscar elemento por posición
    def find_at(self, index):
        current = self.head
        contador = 0

        while current is not None:
            if contador == index:
                return current
            else:
                current = current.next
                contador += 1
        raise Exception("La posicion no existe")

    # Eliminar al inicio
    def shift(self):
        if self.head is None:
            raise Exception("Subdesbordamiento de pila")
        if self.head == self.tail:
            current = self.head
            self.head = None
            self.tail = None
            self.size = 0

            return current.data
        else:
            current = self.head
            self.head = current.next
            current.next = None
            self.size -= 1
            return current.data

    # Eliminar al final
    def pop(self):
        current = self.tail
        if self.is_empty():
            raise Exception("Subdesbordamiento")
        elif self.head is self.tail:
            self.head = None
            self.tail = None
            current.next = None
            self.size = 0
            return current.data
        else:
            prev = self.find_at(self.size - 2)
            self.tail = prev
            prev.next = None
            self.size -= 1
            return current.data

    # Eliminar en una posición específica
    def remove_at(self, index):
        if index == 0:
            return self.shift()
        elif self.is_empty():
            return self.shift()
        elif index == self.size - 1:
            return self.pop()
        else:
            current = self.find_at(index)
            prev = self.find_at(index - 1)
            prev.next = current.next
            current.next = None
            self.size -= 1
            return current

    # Eliminar un valor específico
    def remove_by(self, index, data):
        current = self.find_by(data)
        if index == 0:
            return self.shift()
        elif self.is_empty():
            return self.shift()
        elif index == self.size - 1:
            return self.pop()
        else:
            current = self.find_by(data)
            pos = self.get_index(current)
            prev = self.find_at(pos - 1)  # otra opcion seria de poner self.remove_at(pos)
            prev.next = current.next
            current.next = None
            self.size -= 1

    # Obtener posición
    def get_index(self, ref):
        current = self.head
        pos = 0
        while current is not None:
            if current is ref:
                return pos
            else:
                current = current.next
                pos += 1
        raise Exception("La direccion de memoria no existe")

    # Recorrer la lista
    def transversal(self):
        current = self.head
        result = ""
        while current is not None:
            result += str(current)
            if current is not self.tail:
                result += "\n"
            current = current.next
        return result

    def __iter__(self):
        self._current_node = self.head
        return self

    def __next__(self):
        if self._current_node is None:
            raise StopIteration
        elif self._current_node is self.tail:
            self._current_node = None
            return self.tail.data
        else:
            current_data = self._current_node.data
            self._current_node = self._current_node.next
            return current_data