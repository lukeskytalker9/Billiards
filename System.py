import numpy as np
from State import State

class System:
    dT = 0.01
    dt = 0.00001
    mu = 0.05

    def __init__(self, initial_state: State, walls) -> None:
        # the list of all the states the system has been in
        self.history = np.ndarray(dtype=State)
        self.history[0] = initial_state
        self.walls = walls

    def run(self, steps: int) -> None:
        for T in range(steps):
            temp_state = self.history[-1].get_next(self.dT)

            if not temp_state.has_overlap():
                # no collision, we're good
                self.history.append(temp_state)
            else:
                # collision detected
                for t in range(self.dT / self.dt):
                    temp_state = self.history[-1].get_next(self.dt)

                    if temp_state.has_overlap():
                        temp_state.deal_with_overlap()

                self.history.append(temp_state)
