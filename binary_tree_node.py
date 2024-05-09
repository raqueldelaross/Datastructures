from typing import TypeVar, Generic


T = TypeVar('T')


class Node(Generic[T]):
    def __init__(self, data: T):
        self.data = data
        # izquierda
        self.left: Node | None = None
        # derecha
        self.right: Node | None = None

    def is_leaf(self):
        return self.left is None and self.right is None
