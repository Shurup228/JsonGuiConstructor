from json import load
from sys import argv, exit

from PyQt5.QtWidgets import QApplication

from JsonGuiConstructor.library.jsonToQt import widgets

if __name__ == '__main__':
    with open('../test.json', 'r') as markupFile:
        markup = load(markupFile)

    for w, _ in markup.items():
        try:
            widget = widgets[w]
        except KeyError:
            pass

    app = QApplication(argv)
    mainWidget = widget()
    mainWidget.show()
    exit(app.exec_())
