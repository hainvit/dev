"""
A GridLayout class object presents with a grid of cells arranged in rows and columns.
The class contains addWidget() method. Any widget can be added by specifying the number
of rows and columns of the cell. Optionally, a spanning factor for row as well as column,
if specified makes the widget wider or taller than one cell.
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QDialog, QPushButton, QGridLayout


def main():
    app = QApplication(sys.argv)
    win = QWidget()
    grid = QGridLayout()

    for i in range(1, 5):
        for j in range(1, 5):
            grid.addWidget(QPushButton('B'+str(i)+str(j)), i, j)

    win.setLayout(grid)
    win.setGeometry(100, 100, 200, 100)
    win.setWindowTitle('PyQt')
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
