import numpy as np
from State import State

class System:
    dT = 0.01       # Size of big timestep.
    dt = 0.00001    # Size of little timestep.
    mu = 0.05       # Bascially the coefficient of friction.

    def __init__(self, initial_state: State, walls) -> None:
        self.history = np.ndarray(dtype=State) # The list of all the states the system has been in.
        self.history[0] = initial_state
        self.walls = walls

    def run(self, steps: int) -> None:
        for T in range(steps):
            temp_state = self.history[-1].get_next(self.dT)

            if not temp_state.has_overlap():
                # no collision, we're good
                self.history.append(temp_state)
            else:
                # collision detected, so transition to using little timesteps until the collision happens
                for t in range(self.dT / self.dt):
                    temp_state = self.history[-1].get_next(self.dt)

                    if temp_state.has_overlap():
                        temp_state.deal_with_overlap()

                self.history.append(temp_state)
