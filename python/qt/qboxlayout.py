"""
QBoxLayout class lines up the widgets vertically or horizontally.
Its derived classes are QVBoxLayout (for arranging widgets vertically) 
and QHBoxLayout (for arranging widgets horizontally).
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QDialog, QPushButton, QVBoxLayout, QHBoxLayout


def vertical():
    app = QApplication(sys.argv)
    win = QWidget()

    btn1 = QPushButton('Button 1')
    btn2 = QPushButton('Button 2')

    vbox = QVBoxLayout()
    vbox.addStretch()
    vbox.addWidget(btn1)
    vbox.addWidget(btn2)

    win.setLayout(vbox)
    win.setWindowTitle('PyQt')
    win.show()
    sys.exit(app.exec_())


def horizontal():
    app = QApplication(sys.argv)
    win = QWidget()

    btn1 = QPushButton('Button 1')
    btn2 = QPushButton('Button 2')

    hbox = QHBoxLayout()
    hbox.addStretch()
    hbox.addWidget(btn1)
    hbox.addWidget(btn2)
    win.setLayout(hbox)
    win.setWindowTitle('PyQt')
    win.show()
    sys.exit(app.exec_())


def verticalandhorizontal():
    app = QApplication(sys.argv)
    win = QWidget()

    btn1 = QPushButton('Button 1')
    btn2 = QPushButton('Button 2')
    vbox = QVBoxLayout()
    vbox.addStretch()
    vbox.addWidget(btn1)
    vbox.addWidget(btn2)

    btn3 = QPushButton('Button 3')
    btn4 = QPushButton('Button 4')
    hbox = QHBoxLayout()
    hbox.addStretch()
    hbox.addWidget(btn3)
    hbox.addWidget(btn4)

    vbox.addLayout(hbox)
    win.setLayout(vbox)
    win.setWindowTitle('PyQt')
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    # vertical()
    # horizontal()
    verticalandhorizontal()
