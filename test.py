import sys

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel


class Widget(QWidget):

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.initUI()

    def initUI(self) -> None:
        self.setLayout(QVBoxLayout(self))
        lab1 = QLabel()
        lab1.setText("kek")
        self.layout().addWidget(lab1)
        lab2 = QLabel()
        lab2.setText("lol")
        self.layout().addWidget(lab2)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # widget = Widget()
    widget2 = QWidget()
    widget2.setLayout(QVBoxLayout(widget2))
    widget2.layout().addWidget(QLabel("kek"))
    widget2.layout().addWidget(QLabel("lol"))
    widget2.show()
    sys.exit(app.exec_())
