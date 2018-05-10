import logging
import sys

from PyQt5.QtWidgets import QVBoxLayout, QPushButton, QFileDialog, QApplication, QWidget, QLabel

from utils.Interpreter import Interpreter

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s::%(filename)s - %(message)s")


class Inst(QWidget):

    def __init__(self):
        super().__init__()
        self.layout_ = QVBoxLayout()


        self.initUI()

    def initUI(self):
        self.setLayout(self.layout_)
        self.layout().addWidget(self.inst)
        self.show()


class MainMenu(QWidget):

    def __init__(self, fake_widget) -> None:
        super().__init__()
        self.fake_widget = fake_widget
        self.layout_: QVBoxLayout = QVBoxLayout(self)
        self.open_button: QPushButton = QPushButton("Open")
        self.inst_button: QPushButton = QPushButton("Show syntax")
        self.edit: QPushButton = QPushButton("Edit")

        self.initUI()

    def initUI(self) -> None:
        self.setLayout(self.layout_)

        self.layout().addWidget(self.open_button)
        self.layout().addWidget(self.inst_button)
        self.layout().addWidget(self.edit)


        self.open_button.clicked.connect(self.run)
        self.inst_button.clicked.connect(self.show_inst)

        self.setWindowTitle("Main menu")
        self.show()

    def run(self) -> None:
        from os import getcwd

        file_name, _ = QFileDialog.getOpenFileName(self, "Choose file", getcwd(), "*.json")
        interpreter: Interpreter = Interpreter(file_name)
        widget = interpreter.run()

        fake_widget.layout().addWidget(widget)
        fake_widget.showMaximized()

        widget.show()

    def show_inst(self):
        text = open("./library/jsonToQt.py", "r").read()
        inst = QLabel(text)
        fake_widget.layout().addWidget(inst)
        fake_widget.showMaximized()


if __name__ == '__main__':
    logging.info("Starting QApplication")

    app = QApplication(sys.argv)

    fake_widget = QWidget()
    fake_widget.setLayout(QVBoxLayout())
    main_widget = MainMenu(fake_widget)

    logging.info("Application running")

    sys.exit(app.exec_())


