from functools import partial
import numpy as np

class AppController:
    def __init__(self, state, window):
        self.state = state
        self.window = window
        self.connectSignals()
        self.update()

    def connectSignals(self):
        self.window.resetButton.clicked.connect(self.onResetButtonPressed)
        for i in range(len(self.window.sliders)):
            self.window.sliders[i].valueChanged.connect(partial(self.onSlidersValueChanged, i))

    def onResetButtonPressed(self):
        self.state.modelMatrix = np.eye(4, dtype=np.float32)
        self.update()

    def onSlidersValueChanged(self, i):
        self.state.modelMatrix[i%2, i//2] = self.window.sliders[i].value() / 10.0
        self.update()

    def update(self):
        modelMatrix = self.state.modelMatrix
        self.window.canvas.program['model'] = modelMatrix
        self.window.text.setText(f'{modelMatrix[0,0]:.2f} {modelMatrix[0,1]:.2f}\n{modelMatrix[1,0]:.2f} {modelMatrix[1,1]:.2f}' )
        self.window.canvas.update()

