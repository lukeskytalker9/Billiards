import numpy as np

class State:
    def __init__(self, balls=None):
        self.balls = np.array(balls)

    def get_next(self, timestep):
        pass
