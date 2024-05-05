from __future__ import annotations
import numpy as np
from Ball import Ball
import matplotlib.pyplot as plt
import matplotlib as mpl

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

    def has_overlap(self):
        """Are any balls overlapping each other?"""
        # Iterate over each ball and every other ball.
        overlaps = []

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
                        # ...add that pair to the list of overlaps, if they're not already in there.
                        if not any([ball in o and other in o for o in overlaps]):
                            overlaps.append([ball, other])
        # Return overlaps
    
        return overlaps

    def perform_collision(self, overlaps: list):
        print(f"overlaps: ", *overlaps)
        for pair in overlaps:
            # move 'em apart
            dist_vec = pair[1].pos - pair[0].pos
            d = pair[0].radius + pair[1].radius - np.linalg.norm(dist_vec)
            factor = (dist_vec) / np.linalg.norm(dist_vec) / 2 * d
            # print(factor)
            pair[0].pos = pair[0].pos - factor
            pair[1].pos = pair[1].pos + factor

            # n = pair[0].pos - pair[1].pos
            # n = n / np.linalg.norm(n)
            # self.vel = self.vel - 2 * (np.dot(self.vel, n)) * n


            # pair[0].bounce_velocity(pair[1])
            # pair[1].bounce_velocity(pair[0])
        
        


if __name__ == "__main__":
    balls = [Ball(0, 0, 0, 0, 1), Ball(0, 0.5, 0, -1, 1)]
    state = State(balls)
    print("Balls before: ", *balls)
    # state.perform_collision(state.has_overlap())
    print("Balls after: ", *balls)
    fig, ax = plt.subplots()
    ax.set_xlim([-1, 1])

    ax.set_ylim([-1, 1])
    x = [ball.pos[0] for ball in balls]
    y = [ball.pos[1] for ball in balls]
    vx = [ball.vel[0] for ball in balls]
    vy = [ball.vel[1] for ball in balls]


    circles = [plt.Circle((xi,yi), radius=0.5, linewidth=0) for xi,yi in zip(x,y)]
    c = mpl.collections.PatchCollection(circles)
    ax.add_collection(c)
    plt.gca().set_aspect('equal')
    ax.quiver(x, y, vx, vy)

    plt.show()    
