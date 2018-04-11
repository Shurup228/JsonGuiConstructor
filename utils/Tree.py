from typing import List, Dict, Any

from library.jsonToQt import CHILDREN


class Tree:
    def __init__(self, root=None) -> None:
        self.__root: Dict = root
        self.__children: List[Tree] = []

    def get_root(self):
        return {key: value for (key, value) in self.__root.items() if key not in ["type", "layout"]}

    def get_children(self):
        return self.__children

    def add_child(self, child) -> None:
        self.__children.append(child)

    def __getattribute__(self, name: str) -> Any:
        root = super().__getattribute__("_Tree__root")
        try:
            return root[name]
        except KeyError:
            return super().__getattribute__(name)

    @staticmethod
    def create(dict_: Dict):
        root = dict_.copy()
        try:
            root.pop(CHILDREN)
        except KeyError:
            return Tree(root)

        result = Tree(root)

        for child in dict_[CHILDREN]:
            result.add_child(Tree.create(child))

        return result
