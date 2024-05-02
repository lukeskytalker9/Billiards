import numpy as np

class State:
    def __init__(self, balls=None):
        self.balls = np.array(balls)

    def get_next(self, timestep):
        pass

    def has_overlap(self):
        for ball in self.balls:
            for other in self.balls:
                # if they're not the same ball...
                if id(ball) != id(other):
                    # ...and if they overlap...
                    if ball.overlaps(other):
                        # return true
                        return True
        # ... if there's no overlap, return false.
        return False