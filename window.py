from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from canvas import AppCanvas

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)
        self.mainLayout = QVBoxLayout(self.centralWidget)
        #Canvas
        self.canvas = AppCanvas()
        self.mainLayout.addWidget(self.canvas.native)
        #Info
        self.text = QLabel("1 0 \n 0 1")
        self.text.setAlignment(Qt.AlignCenter)
        font = QFont()
        font.setBold(True)
        font.setPointSize(20)
        self.text.setFont(font)
        self.mainLayout.addWidget(self.text)
        #Controller
        self.controllerWidget = QFrame()
        self.mainLayout.addWidget(self.controllerWidget)
        controllerLayout = QHBoxLayout(self.controllerWidget)
        self.sliders = []
        for i in range(4):
            slider = QSlider()
            slider.setMaximum(50)
            slider.setMinimum(-50)
            slider.setValue(10 if (i == 0 or i == 3) else 0)
            self.sliders.append(slider)
            controllerLayout.addWidget(slider)
        #Reset button
        self.resetButton = QPushButton("Reset")
        self.mainLayout.addWidget(self.resetButton)

