from __future__ import annotations
import numpy as np
from Ball import Ball
import matplotlib.pyplot as plt
import matplotlib as mpl

class State:
    def __init__(self, balls=None) -> None:
        self.balls = np.array(balls)

    def get_next(self, timestep) -> State:
        """Returns the next state after this one (i.e., the state after one timestep)."""
        next = State(balls=self.balls)

        # Update the balls (unless they're pocketed).
        for ball in next.balls:
            if not ball.isPocketed:
                ball.update(timestep)
        return next

    def has_overlap(self) -> list:
        """Returns a list of pairs of balls which overlap each other, or empty list if none do."""
        overlaps = []
        # Compare every ball to every ball.
        for ball in self.balls:
            for other in self.balls:
                # If neither ball is pocketed...
                if not ball.isPocketed and not other.isPocketed:
                    # ...and they're not the same ball...
                    if id(ball) != id(other):
                        # ...and they overlap...
                        if ball.overlaps(other):
                            # ...then add that pair to the list of overlaps, but only if it's not already in there.
                            if not any([ball in o and other in o for o in overlaps]):
                                overlaps.append([ball, other])
        return overlaps

    def plot(self, xlims=[-1, 1], ylims=[-1, 1]) -> None:
        """Draws the current state to a matplotlib plot."""
        fig, ax = plt.subplots()
        ax.set_xlim(xlims)
        ax.set_ylim(ylims)
        px = [ball.pos[0] for ball in self.balls]
        py = [ball.pos[1] for ball in self.balls]
        vx = [ball.vel[0] for ball in self.balls]
        vy = [ball.vel[1] for ball in self.balls]
        circles = [plt.Circle((ball.pos[0], ball.pos[1]), radius=ball.radius, linewidth=10) for ball in self.balls]
        ax.add_collection(mpl.collections.PatchCollection(circles))
        plt.gca().set_aspect('equal')
        ax.quiver(px, py, vx, vy)
        plt.show()


if __name__ == "__main__":
    balls = [Ball(0, 0, 0, 0, 0.1), Ball(0, 0.5, 0, -1, 0.1)]
    state = State(balls)
    state.plot()