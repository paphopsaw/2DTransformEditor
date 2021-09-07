from PyQt5.QtWidgets import QApplication
import sys
from window import MainWindow
from controller import AppController
from state import AppState

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    state = AppState()
    AppController(state, window)
    app.exec_()

if __name__ == '__main__':
    main()