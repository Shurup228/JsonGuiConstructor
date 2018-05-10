from PyQt5.QtWidgets import QFormLayout, QVBoxLayout, QHBoxLayout, QGridLayout, QWidget, QLabel
from PyQt5.QtWidgets import QMainWindow, QPushButton

widgets = {
    "QMainWindow": QMainWindow,
    "QWidget": QWidget,
    "QLabel": QLabel,
    "QPushButton": QPushButton
}

layouts = {
    "QFormLayout": QFormLayout,
    "QVBoxLayout": QVBoxLayout,
    "QHBoxLayout": QHBoxLayout,
    "QGridLayout": QGridLayout
}

TYPE = "type"
CHILDREN = "children"
LAYOUT = "layout"
