import numpy as np
from __future__ import annotations

class State:
    def __init__(self, balls=None) -> None:
        self.balls = np.array(balls)

    def get_next(self, timestep) -> State:
        """Return the next state after this one (i.e., the state after one timestep)."""
        next = self.balls.copy()

        for ball in next.balls():
            if not ball.isPocketed():
                ball.update(timestep)

        return next

    def has_overlap(self) -> bool:
        """Are any balls overlapping each other?"""
        # Iterate over each ball and every other ball.
        for ball in self.balls:

            if ball.isPocketed:
                continue

            for other in self.balls:

                if other.isPocketed:
                    continue

                # If they're not the same ball...
                if id(ball) != id(other):
                    # ...and if they overlap...
                    if ball.overlaps(other):
                        # ...return true.
                        return True
        # If there's no overlap, return false.
        return False

    def perform_collision():
        pass