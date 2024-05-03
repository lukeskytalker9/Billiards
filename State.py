import numpy as np
from __future__ import annotations

class State:
    def __init__(self, balls=None):
        self.balls = np.array(balls)

    def get_next(self, timestep) -> State:
        """Return the next state after this one (i.e., the state after one timestep)."""
        pass

    def has_overlap(self) -> bool:
        """Are any balls overlapping each other?"""
        # Iterate over each ball and every other ball.
        for ball in self.balls:
            for other in self.balls:
                # If they're not the same ball...
                if id(ball) != id(other):
                    # ...and if they overlap...
                    if ball.overlaps(other):
                        # ...return true.
                        return True
        # If there's no overlap, return false.
        return False
    
    def calculate_collision():
        pass