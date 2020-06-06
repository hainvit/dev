#!/usr/bin/python

"""
ZetCode PyQt5 tutorial

In this example, we create a simple
window in PyQt5.

Author: Jan Bodnar
Website: zetcode.com
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel


def main():

    app = QApplication(sys.argv)

    w = QWidget()
    # The resize() method resizes the widget. It is 250px wide and 150px high.
    w.resize(500, 150)
    # The move() method moves the widget to a position on the screen at x=300, y=300 coordinates.
    w.move(300, 300)
    w.setWindowTitle('Hello World')
    # set label
    b = QLabel(w)
    b.setText('Hello World')
    b.move(250, 75)
    w.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
