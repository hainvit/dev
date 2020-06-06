"""
Signals and slot
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QDialog, QPushButton


def main():
    app = QApplication(sys.argv)

    win = QDialog()

    btn1 = QPushButton(win)
    btn1.setText('Button 1')
    btn1.move(50, 20)
    btn1.clicked.connect(clicked_btn1)

    btn2 = QPushButton(win)
    btn2.setText('Button 2')
    btn2.move(50, 50)
    btn2.clicked.connect(clicked_btn2)

    win.setGeometry(100, 100, 200, 100)
    win.setWindowTitle('Signals and slot')
    win.show()
    sys.exit(app.exec_())


def clicked_btn1():
    print('Clicked btn1')


def clicked_btn2():
    print('Clicked btn2')


if __name__ == '__main__':
    main()
