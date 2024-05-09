from typing import TypeVar, Generic

T = TypeVar('T')


class Node(Generic[T]):
    def __init__(self, data: T):
        self.data: T = data
        self.next: Node | None = None

    def __str__(self):
        return str(self.data)
