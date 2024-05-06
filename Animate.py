from System import System
from State import State
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from Ball import Ball
import numpy as np
import matplotlib as mpl

class Animate:

    def __init__(self, system: System, num_frames, fps=60) -> None:
        self.system = system
        self.num_frames = num_frames
        self.fps = fps

    def show_live(self) -> None:
        """This calculates each frame and then shows that frame, then calculates the next one and shows it, etc."""

        fig, ax = plt.subplots()
        vis, _ = ax.plot([], [])

        ax.set_xlim([-1, 1])
        ax.set_ylim([-1, 1])

        state = system.get_current_state()
        px, py = 1.0 * np.array([[ball.pos[0] for ball in state.balls], [ball.pos[1] for ball in state.balls]])
        vx, vy = 0.1 * np.array([[ball.vel[0] for ball in state.balls], [ball.vel[1] for ball in state.balls]])

        def init():
            return vis,

        def update(_):
            self.system.run(1)
            state = self.system.get_current_state()
            circles = [plt.Circle((ball.pos[0], ball.pos[1]), radius=ball.radius, linewidth=10) for ball in state.balls]
            ax.add_collection(mpl.collections.PatchCollection(circles))

            ax.quiver(px, py, vx, vy)
            # vis.set_data([b.pos[0] for b in state.balls], [b.pos[1] for b in state.balls])
            return vis,

        ani = FuncAnimation(fig, update, frames=self.num_frames, interval=1000/self.fps, init_func=init, blit=True)
        plt.show()


    def calc_then_show(self, scale_fac=6000):
        """EXPERIMENTAL"""
        self.system.run(self.num_frames)

        # print(self.system.repr_history())
        fig, ax = plt.subplots()

        vmax, vmin = (1, -1)

        # This converts between pixels and plot units.
        scatscale = ((ax.get_window_extent().width / (vmax - vmin + 1) * 72 / fig.dpi) ** 2)

        plt.gca().set_aspect('equal')
        ax.axis("off")

        ax.set_xlim([vmin, vmax])
        ax.set_ylim([vmin, vmax])

        px, py = ([ball.pos[0] for ball in self.system.history[0].balls], [ball.pos[1] for ball in self.system.history[0].balls])
        vx, vy = ([ball.vel[0] for ball in self.system.history[0].balls], [ball.vel[1] for ball in self.system.history[0].balls])

        arrows = [ax.arrow(px[i], py[i], vx[i], vy[i], animated=True, fc='black', ec='black') for i in range(len(self.system.history[0].balls))]

        # collection = lambda: mpl.collections.PatchCollection([plt.Circle((ball.pos[0], ball.pos[1]), radius=ball.radius, linewidth=10) for ball in self.system.history[0].balls])

        # (ln,) = ax.plot(np.zeros(len(px)), np.zeros(len(py)), animated=True, marker='.', markersize=[ball.radius for ball in self.system.get_current_state().balls])
        ln = ax.scatter(np.zeros(len(px)), np.zeros(len(py)), animated=True, s=[scatscale * ball.radius / 2 for ball in self.system.get_current_state().balls])

        plt.show(block=False)
        plt.pause(0.1)
        bg = fig.canvas.copy_from_bbox(fig.bbox)
        ax.draw_artist(ln)
        fig.canvas.blit(fig.bbox)

        for state in self.system.history:

            px, py = 1.0 * np.array([[ball.pos[0] for ball in state.balls], [ball.pos[1] for ball in state.balls]])
            vx, vy = 10 * np.array([[ball.vel[0] for ball in state.balls], [ball.vel[1] for ball in state.balls]])

            fig.canvas.restore_region(bg)
            # collection.set_paths([plt.Circle((ball.pos[0], ball.pos[1]), radius=ball.radius, linewidth=10) for ball in state.balls])
            ln.set_offsets([ball.pos for ball in state.balls])
            ax.draw_artist(ln)

            for i, arrow in enumerate(arrows):
                arrow.set_data(x=px[i], y=py[i], dx=vx[i], dy=vy[i])

            fig.canvas.blit(fig.bbox)
            fig.canvas.flush_events()

            # print(f'frame {frame}', end='\r')

            plt.pause(1/self.fps)


if __name__ == "__main__":
    print("Test file for Animate.py")
    balls = np.array([Ball(0, 0, 0, 0, 0.1), Ball(0, 0.5, 0, -1, 0.1), Ball(0, 0.25, 0, -0.9, 0.1)])

    system = System(initial_state=State(np.array(balls)), walls=None)
    anim = Animate(system=system, num_frames=120, fps=60)
    anim.calc_then_show()
    print("Test finished.")
