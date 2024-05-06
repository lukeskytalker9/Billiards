import numpy as np
from State import State
from Ball import Ball

class System:
    dT = 0.01       # Size of big timestep.
    dt = 0.00001    # Size of little timestep.
    mu = 0.05       # Bascially the coefficient of friction.

    def __init__(self, initial_state: State, walls) -> None:
        self.history = [] # The list of all the states the system has been in.
        self.history.append(initial_state)
        self.walls = walls

        # We don't wany any missing states.
        assert(self.dT % self.dt == 0, "Big timestep should be divisible by little timestep.")

    def get_current_state(self):
        return self.history[-1]

    def run(self, steps: int) -> None:
        """Calculates the given number of subsequent states, which are added to self.history."""

        for _ in range(steps):
            # Get next state, and see if there are any balls overlaping (i.e., ball-ball collisions).
            temp_state = self.get_current_state().get_next(self.dT)
            overlaps = temp_state.has_overlap()

            if not overlaps:
                # If next frame has no collisions, we're good. Just add current state to history and move on.
                self.history.append(temp_state)
                continue
            else:
                # If collision detected next frame, transition to using little timesteps until the collision happens.
                for t in range(int(self.dT / self.dt)):
                    # First calculate new next frame w/ small timestep.
                    temp_state = self.get_current_state().get_next(self.dt)

                    # If there are any overlaps now...
                    overlaps = temp_state.has_overlap()
                    while len(overlaps) > 0:
                        # ... then perform collision procedure until there are no more overlaps.
                        # This loop is needed b/c collision procedure may produce new overlaps since it moves the balls apart.
                        # ? Will this actually update the balls in-place? I don't think it will...
                        for pair in overlaps:
                            pair[0].collision(pair[1])
                        overlaps = temp_state.has_overlap()

            self.history.append(temp_state)

    def __str__():


if __name__ == "__main__":
    balls = np.array([Ball(0, 0, 0, 0, 0.1), Ball(0, 0.5, 0, -1, 0.1)])
    system = System(initial_state=State(balls), walls=None)
    system.get_current_state().plot()
    system.run(50)
    system.get_current_state().plot()
    print("Test finished.")
