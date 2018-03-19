from typing import List


class Node:

    @classmethod
    def get_class(cls):
        return cls

    def __init__(self, root: object) -> None:
        super().__init__()
        self.__children: List[Node] = []
        self.__root = root

    def get_children(self) -> List[get_class()]:
        return self.__children

    def get_child(self, identifier: int) -> get_class():
        child: self.get_class()
        for ch in self.__children:
            if ch.id == identifier:
                return child
        return None

    def add_child(self, child: object) -> None:
        self.__children.append(Node(child))

    def add_children(self, *children: List[get_class()]):
        self.__children.extend(children)

    def has_children(self) -> bool:
        return self.__children == []

    def __call__(self) -> object:
        return self.__root
