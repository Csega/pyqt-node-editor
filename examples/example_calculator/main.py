import sys
from PyQt5.QtWidgets import *

from examples.example_calculator.calc_window import CalculatorWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)

    wnd = CalculatorWindow()
    wnd.show()

    sys.exit(app.exec_())
