from System import System
from State import State
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from Ball import Ball
import numpy as np
import matplotlib as mpl

class Animate:

    def __init__(self, system: System, num_frames: int, fps=60) -> None:
        self.system = system
        self.num_frames = num_frames
        self.fps = fps

    def calc_then_show(self) -> None:
        """EXPERIMENTAL"""

        # Run the system for however many timesteps were given. Also save initial state for later.
        self.system.run(self.num_frames)
        initial_state = self.system.history[0]

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

        # Calculate position and velocity lists with x and y components separated (need for plotting).
        px, py = ([ball.pos[0] for ball in initial_state.balls], [ball.pos[1] for ball in initial_state.balls])
        vx, vy = ([ball.vel[0] for ball in initial_state.balls], [ball.vel[1] for ball in initial_state.balls])

        # Draw arrows for balls' velocities.
        arrow_scale = 10.0
        arrows = [ax.arrow(px[i], py[i], vx[i], vy[i], animated=True, fc='black', ec='black') for i in range(len(initial_state.balls))]

        # Make the plot for the balls (which is secretly just a scatter plot, don't tell anybody).
        ln = ax.scatter(np.zeros(len(px)), np.zeros(len(py)), animated=True, s=[scatscale * ball.radius / 2 for ball in initial_state.balls])

        # Some wierd matplotlib stuff that we need for this to work.
        plt.show(block=False)
        plt.pause(0.1)
        bg = fig.canvas.copy_from_bbox(fig.bbox)
        ax.draw_artist(ln)
        fig.canvas.blit(fig.bbox)

        # For every state in the system's history...
        for frame, state in enumerate(self.system.history):

            # Calculate position and velocity arrays with x and y components separated (need for plotting).
            px, py = np.array([[ball.pos[0] for ball in state.balls], [ball.pos[1] for ball in state.balls]])
            vx, vy = np.array([[ball.vel[0] for ball in state.balls], [ball.vel[1] for ball in state.balls]])

            # Redraw background.
            fig.canvas.restore_region(bg)

            # Update the plot points to reflect the balls' new locations.
            ln.set_offsets([ball.pos for ball in state.balls])

            # Redraw balls.
            ax.draw_artist(ln)

            # Update the arrows to reflect the balls' new velocities.
            for i, arrow in enumerate(arrows):
                arrow.set_data(x=px[i], y=py[i], dx=vx[i], dy=vy[i])

            # Redraw arrows.
            for arrow in arrows:
                ax.draw_artist(arrow)

            # Some more wierd matplotlib stuff that we need for this to work.
            fig.canvas.blit(fig.bbox)
            fig.canvas.flush_events()

            print(f'frame {frame}', end='\r')

            # Pause so we can control the framerate.
            plt.pause(1/self.fps)


if __name__ == "__main__":
    print("Test file for Animate.py")
    balls = np.array([Ball(0, 0, 0, 0, 0.1), Ball(0, 0.5, 0, -1, 0.1), Ball(0, 0.25, 0, -0.25, 0.1)])
    system = System(initial_state=State(np.array(balls)), walls=None)
    Animate(system=system, num_frames=120, fps=60).calc_then_show()
    print("Test finished.")
