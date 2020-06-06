"""
QFormLayout is a convenient way to create two column form, 
where each row consists of an input field associated with a label. 
As a convention, the left column contains the label and the right column contains an input field.
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QDialog, QPushButton, QVBoxLayout, QHBoxLayout, QRadioButton, QLineEdit, QFormLayout


def main():
    app = QApplication(sys.argv)
    win = QWidget()
    fbox = QFormLayout()

    l1 = QLabel('Name')
    nm = QLineEdit()
    fbox.addRow(l1, nm)

    l2 = QLabel('Address')
    add1 = QLineEdit()
    add2 = QLineEdit()
    vbox = QVBoxLayout()
    vbox.addStretch()
    vbox.addWidget(add1)
    vbox.addWidget(add2)
    fbox.addRow(l2, vbox)

    r1 = QRadioButton("Male")
    r2 = QRadioButton("Female")
    hbox = QHBoxLayout()
    hbox.addStretch()
    hbox.addWidget(r1)
    hbox.addWidget(r2)
    fbox.addRow(QLabel('Sex'), hbox)

    fbox.addRow(QPushButton('Submit'), QPushButton('Cancel'))

    win.setLayout(fbox)
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
