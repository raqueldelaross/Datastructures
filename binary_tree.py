from typing import TypeVar, Generic
from binary_tree_node import Node

T = TypeVar("T")


def split_text(text: str) -> (str, str):
    left = ''
    right = ''
    flag = True

    count = 0
    for i in text:
        if i == '(':
            count += 1
        elif i == ')':
            count -= 1
        else:
            if count == 1 and i == ',':
                flag = False

        if flag:
            left += i
        else:
            right += i

    left = left[1:]
    right = right[1:]
    return left, right


class BinaryTree(Generic[T]):
    def __init__(self):
        self.__root: Node | None = None

    def insert_root(self, data: T):
        new_node = Node(data)
        self.__root = new_node

    def __insert_by_preorder(self, text: str, subtree: str):
        left, right = split_text(text)

        if left != '':
            if left[0] != '_':
                left_data = left[0]
                self.insert_left(left_data, subtree)
                left = left[1:]
                self.__insert_by_preorder(left, left_data)

        if right != '':
            if right[0] != '_':
                right_data = right[0]
                self.insert_right(right_data, subtree)
                right = right[1:]
                self.__insert_by_preorder(right, right_data)

    def insert_by_preorder(self, preorder: str):
        root = preorder[0]
        self.insert_root(root)

        preorder = preorder[1:]
        self.__insert_by_preorder(preorder, root)

    def insert_left(self, data: T, ref: T | None = None):
        if ref is None:
            self.insert_root(data)
        else:
            new_node = Node(data)
            node_ref = self.search(ref)
            if node_ref is not None:
                node_ref.left = new_node

    def insert_right(self, data: T, ref: T | None = None):
        if ref is None:
            self.insert_root(data)
        else:
            new_node = Node(data)
            node_ref = self.search(ref)
            if node_ref is not None:
                node_ref.right = new_node

    def __preorder(self, subtree: Node | None) -> str:
        result = 'None'

        if subtree is not None:
            result = f"{subtree.data} - {self.__preorder(subtree.left)} - {self.__preorder(subtree.right)}"

        return result

    def preorder(self) -> str:
        return self.__preorder(self.__root)

    def __inorder(self, subtree: Node | None) -> str:
        result = 'None'

        if subtree is not None:
            result = f"{self.__inorder(subtree.left)} - {subtree.data} - {self.__inorder(subtree.right)}"

        return result

    def inorder(self) -> str:
        return self.__inorder(self.__root)

    def __postorder(self, subtree: Node | None) -> str:
        result = 'None'

        if subtree is not None:
            result = f"{self.__postorder(subtree.left)} - {self.__postorder(subtree.right)} - {subtree.data}"

        return result

    def postorder(self) -> str:
        return self.__postorder(self.__root)

    def __get_path(self, ref: T, subtree: Node | None) -> str:
        if subtree is None:
            return ''

        elif subtree.data == ref:
            return subtree.data

        if subtree.left is not None:
            left = self.__get_path(ref, subtree.left)
            if left is not None:
                return f'Left - {left}'

        if subtree.right is not None:
            right = self.__get_path(ref, subtree.right)
            if right is not None:
                return f'Right - {right}'

    def get_path(self, ref: T) -> str:
        return self.__get_path(ref, self.__root)

    def __search(self, ref: T, subtree: Node | None = None) -> Node | None:

        if subtree is None:
            return None
        elif subtree.data == ref:
            return subtree

        if subtree.left is not None:
            left = self.__search(ref, subtree.left)
            if left is not None:
                return left

        if subtree.right is not None:
            right = self.__search(ref, subtree.right)
            if right is not None:
                return right

    def search(self, ref: T) -> Node | None:
        return self.__search(ref, self.__root)

    def return_root(self):
        root = self.__root
        return root
