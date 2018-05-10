import logging
from json import load
from typing import Any, Dict

from PyQt5.QtWidgets import QWidget

from library.jsonToQt import widgets, layouts
from utils.Tree import Tree


class Interpreter:
    def __init__(self, file_name) -> None:
        logging.debug(f"Creating Interpreter with {file_name}")

        self.__file_name: str = file_name
        self.__context: Dict[str, Any] = {}

    def get_tree(self) -> Tree:
        with open(self.__file_name, 'r') as file:
            d = load(file)

            return Tree.create(d)

    @staticmethod
    def set_attributes(widget: QWidget, tree: Tree) -> None:
        attributes = tree.root

        logging.debug(f"Setting attributes {attributes} for widget {widget}")

        for attr in attributes.keys():
            method = getattr(widget, "set" + attr[0].upper() + attr[1:])
            args = attributes[attr]

            if isinstance(args, list):
                method(*args)
            else:
                method(args)

    @staticmethod
    def set_layout(widget: QWidget, tree: Tree) -> None:
        layout = layouts[tree.layout](widget)

        logging.debug(f"Setting layout {layout} for widget {widget}")

        widget.setLayout(layout)

    def add_widgets(self, widget: QWidget, tree: Tree) -> None:
        for child in tree.children:
            child_widget: QWidget = self.create_widget(child)

            logging.debug(f"Adding child widget {child_widget} to widget {widget}")

            widget.layout().addWidget(child_widget)

    def create_widget(self, tree: Tree) -> QWidget:
        widget = widgets[tree.type]()

        logging.debug(f"Creating new widget: {tree.type}")

        if tree.has_layout():
            self.set_layout(widget, tree)

        self.set_attributes(widget, tree)

        if tree.has_layout() and tree.has_children():
            self.add_widgets(widget, tree)

        if tree.has_children() and not tree.has_layout():
            raise AttributeError("Can't add child widgets without layout")

        return widget

    def run(self) -> QWidget:
        logging.info("Running interpreter")

        tree = self.get_tree()

        logging.info("Creating context and root widget")

        self.__context = tree.context

        root_widget = self.create_widget(tree)

        return root_widget

