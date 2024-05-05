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

        assert(self.dT % self.dt == 0, "Big timestep should be divisible by little timestep.")

    def get_current_state(self):
        return self.history[-1]

    def run(self, steps: int) -> None:

        for _ in range(steps):
            temp_state = self.get_current_state().get_next(self.dT)
            overlaps = temp_state.has_overlap()

            if not overlaps:
                # Next frame has no collisions, we're good.
                self.history.append(temp_state)
                continue
            else:
                # Collision detected next frame, so transition to using little timesteps until the collision happens.
                for t in range(self.dT / self.dt):
                    temp_state = self.get_current_state().get_next(self.dt)

                    overlaps = temp_state.has_overlap()

                    while overlaps:
                        temp_state.perform_collision(overlaps)
                        overlaps = temp_state.has_overlap()

            self.history.append(temp_state)
