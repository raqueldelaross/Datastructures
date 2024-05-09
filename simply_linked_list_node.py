from typing import TypeVar, Generic

T = TypeVar('T')


class Node(Generic[T]):
    def __init__(self, data: T):
        self.data: T = data
        self.next = None

    def __str__(self):
        return str(self.data)

    def set_siguiente(self, new_next):
        self.next = new_next

    def get_siguiente(self):
        return self.next

    def get_data(self):
        return self.data