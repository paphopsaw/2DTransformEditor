import numpy as np

class AppState:
    def __init__(self):
        self.modelMatrix = np.eye(4, dtype=np.float32)