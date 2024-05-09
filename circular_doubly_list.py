from typing import Optional, TypeVar, Generic

from circular_doubly_list_node import Node

T = TypeVar('T')


class CircularList(Generic[T]):
    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self.size: int = 0

    def _search_position(self, data: T):
        position_current = 0
        current = self.head
        while current is not None:
            if current.data == data:
                return position_current
            else:
                position_current += 1
                current = current.next
        raise Exception('No exite')

    def _search_by_position(self, position: int) -> Node:
        current = self.head
        current_position = 0
        while current_position < self.size:
            if current_position == position:
                return current
            else:
                current = current.next
                return current
        raise "Position doesn't exist inside the list"

    def _search_by_data(self, data: T) -> Node:
        current = self.head
        while current is not self.tail:
            if current.data == data:
                return current
            else:
                current = current.next
        if current.data == self.tail.data:
            return self.tail
        else:
            raise Exception("The node doesn't exist inside the list")

    def is_empty(self) -> bool:
        return self.head is None and self.tail is None and self.size == 0

    def append(self, data: T) -> None:
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.tail.next = self.head
        self.size += 1

    def prepend(self, data: T) -> None:
        if self.is_empty():
            new_node = Node(data)
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
            self.size += 1
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head
            self.size += 1

    def traversal(self) -> str:
        result: str = ''
        aux: Node = self.head
        while aux is not self.tail:
            result += str(aux.data) + '->'
            aux = aux.next
        result += str(self.tail.data)
        return result

    def shift(self) -> T:
        current = self.head
        if self.is_empty():
            raise Exception('Vacio ')
        elif self.size == 1:
            self.head = None
            self.size = None
        else:
            self.head = current.next
            current.next = None
        self.size -= 1
        return current.data

    def pop(self) -> T:
        # es diferente al que se toma con first ,
        current = self.head
        if self.is_empty():
            raise Exception('Vacio ')
        elif self.size == 1:
            self.head = None
            self.size = None
        else:
            self.head = current.next
            current.next = None
        self.size -= 1
        return current.data

    def remove(self, data: T) -> T:
        current = self._search_by_data(data)
        if current is self.head:
            return self.shift()
        elif current is self.tail:
            return self.pop()
        else:
            slot = self._search_position(data)
            anterior = self._search_position(slot - 2)
            anterior.next = current.next
            current.next = None
        self.size -= 1
        return current.data

    def rotate_left(self):
        current = self.head.data
        self.shift()
        self.append(current)

    def rotate_right(self):
        current = self.tail.data
        self.pop()
        self.prepend(current)
