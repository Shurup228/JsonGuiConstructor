import sys
from json import load

from PyQt5.QtWidgets import QApplication, QWidget

from library.jsonToQt import widgets, layouts
from utils.Tree import Tree


class Interpreter:
    def __init__(self, file_name) -> None:
        self.__file_name = file_name

    def get_tree(self) -> Tree:
        with open(self.__file_name, 'r') as file:
            d = load(file)

            return Tree.create(d)

    def set_attributes(self, widget: QWidget, tree: Tree) -> None:
        attributes = tree.get_root()
        print(f"Setting attributes {attributes}")

        for attr in attributes.keys():
            method = getattr(widget, "set" + attr[0].upper() + attr[1:])
            args = attributes[attr]

            if isinstance(args, list):
                method(*args)
            else:
                method(args)

    def set_layout(self, widget: QWidget, tree: Tree):
        try:
            layout = layouts[tree.layout](widget)

            print(f"Setting layout {layout}")

            widget.setLayout(layout)
        except AttributeError:
            print("Can't set layout")
            return

    def add_widgets(self, widget: QWidget, tree: Tree) -> None:
        print(f"Adding widgets {tree.get_children()}")

        for child_widget in tree.get_children():
            child_widget: QWidget = self.create_widget(child_widget)
            print(f"Adding widget {child_widget} to layout {widget.layout()} for {widget}")
            widget.layout().addWidget(child_widget)

    def create_widget(self, tree: Tree) -> QWidget:
        print(f"Creating widget {tree.type}")
        widget = widgets[tree.type]()
        self.set_layout(widget, tree)

        self.set_attributes(widget, tree)
        self.add_widgets(widget, tree)

        return widget

    def run(self) -> None:
        tree = self.get_tree()
        app = QApplication(sys.argv)

        root_widget = self.create_widget(tree)
        root_widget.show()

        sys.exit(app.exec_())

