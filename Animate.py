from System import System
from State import State
import matplotlib.pyplot as plt
from Ball import Ball
import numpy as np

class Animate:

    def __init__(self, system: System, num_frames: int, fps=60) -> None:
        self.system = system
        self.num_frames = num_frames
        self.fps = fps

    def calc_then_show(self, show_arrows=True) -> None:
        """Calculate the states and then display them as a matplotlib animation."""

        # Run the system for however many timesteps were given. Also save initial state for later.
        self.system.run(self.num_frames)
        initial_state = self.system.history[0]
        num_balls = len(initial_state.balls)

        # Create plots.
        fig, ax = plt.subplots()

        # This is the conversion factor between pixels and plot units so we can actually draw the balls to scale.
        scatscale = (ax.get_window_extent().width / (system.x_lims[1] - system.x_lims[0] + 1) * 72 / fig.dpi) ** 2

        # Set plot aspect ratio to 1:1 and turn off axis ticks.
        plt.gca().set_aspect('equal')
        ax.axis("off")

        # Set the x, y ranges of the plot.
        ax.set_xlim(system.x_lims)
        ax.set_ylim(system.y_lims)

        # Create arrows to represent balls' velocities.
        arrow_scale = 1 / 10
        if show_arrows:
            arrows = [ax.arrow(0, 0, 0, 0, animated=True, fc='black', head_width=0.02) for i in range(num_balls)]

        # Make the plot for the balls (which is secretly just a scatter plot, don't tell anybody :3).
        ln = ax.scatter(np.zeros(num_balls), np.zeros(num_balls), animated=True, s=[scatscale * ball.radius / 2 for ball in initial_state.balls])

        # Some matplotlib stuff that we need for this to work.
        plt.show(block=False)
        plt.pause(0.1)
        bg = fig.canvas.copy_from_bbox(fig.bbox)
        ax.draw_artist(ln)
        fig.canvas.blit(fig.bbox)

        # Iterate over every state in the system's history.
        for frame, state in enumerate(self.system.history):

            # Redraw background.
            fig.canvas.restore_region(bg)

            # Update the plot points to reflect the balls' new locations.
            ln.set_offsets([ball.pos for ball in state.balls])

            # Redraw balls.
            ax.draw_artist(ln)

            # Update the arrows to reflect the balls' new positions and velocities and redraw them.
            if show_arrows:
                for i, arrow in enumerate(arrows):
                    pos = state.balls[i].pos
                    vel = state.balls[i].vel * arrow_scale
                    arrow.set_data(x=pos[0], y=pos[1], dx=vel[0] , dy=vel[1])
                
                    for arrow in arrows:
                        ax.draw_artist(arrow)

            # Some more matplotlib stuff that we need for this to work.
            fig.canvas.blit(fig.bbox)
            fig.canvas.flush_events()

            # Print frame number (with carriage return at the end).
            print(f'frame {frame}', end='\r')

            # Pause so we can control the framerate.
            plt.pause(1 / self.fps)


if __name__ == "__main__":
    print("Test file for Animate.py")
    balls = np.array([
        Ball(-1, 1, 0.5, -0.5, 0.1),
        # Ball(1, 1, -0.5, -0.5, 0.1),
        Ball(0, 0.5, 0, -0.5, 0.1), 
        Ball(0, 0.25, 0, -0.25, 0.1)
    ])
    system = System(initial_state=State(np.array(balls)), walls=None)
    Animate(system=system, num_frames=300, fps=60).calc_then_show(False)
    print("Test finished.")
