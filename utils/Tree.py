import logging
from typing import List, Dict, Any

from library.jsonToQt import CHILDREN


class Tree:
    def __init__(self, root=None) -> None:
        self.__root: Dict[str, Any] = root
        self.__children: List[Tree] = []

    @staticmethod
    def create(root: Dict) -> "Tree":
        try:
            children = root.pop(CHILDREN)
        except KeyError:
            return Tree(root)

        logging.debug(f"Creating Tree with root {root} and children {children}")

        result = Tree(root)

        for child in children:
            result.add_child(Tree.create(child))

        return result

    @property
    def root(self) -> Dict[str, Any]:
        return {key: value for (key, value) in self.__root.items()
                if not key.startswith("*") and key not in ["type", "layout"]}

    @property
    def children(self) -> List["Tree"]:
        return self.__children

    @property
    def context(self) -> Dict[str, Any]:
        return {key[1:]: value for (key, value) in self.__root.items() if key.startswith("*")}

    def __getattribute__(self, name: str) -> Any:
        root = super().__getattribute__("_Tree__root")
        try:
            return root[name]
        except KeyError:
            return super().__getattribute__(name)

    def add_child(self, child) -> None:
        self.__children.append(child)

    def has_layout(self) -> bool:
        return "layout" in self.__root

    def has_children(self) -> bool:
        return self.__children != []
