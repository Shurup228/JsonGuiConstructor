from typing import Dict

from PyQt5.Qt import QObject, QLayout
from PyQt5.QtWidgets import QFormLayout, QVBoxLayout, QHBoxLayout, QGridLayout, QWidget
from PyQt5.QtWidgets import QMainWindow

widgets: Dict[str, QObject] = {
    "QMainWindow": QMainWindow,
    "QWidget": QWidget
}

layouts: Dict[str, QLayout] = {
    "QFormLayout": QFormLayout,
    "QVBoxLayout": QVBoxLayout,
    "QHBocLayout": QHBoxLayout,
    "QGridLayout": QGridLayout
}
