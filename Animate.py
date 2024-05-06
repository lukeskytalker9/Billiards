from System import System
from State import State
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from Ball import Ball
import numpy as np
import matplotlib as mpl

class Animate:

    def __init__(self, system: System, num_frames, fps=30) -> None:
        self.system = system
        self.num_frames = num_frames
        self.fps = fps

    def show_live(self) -> None:
        """This calculates each frame and then shows that frame, then calculates the next one and shows it, etc."""

        fig, ax = plt.subplots()
        vis, _ = ax.plot([], [])

        ax.set_xlim([-1, 1])
        ax.set_ylim([-1, 1])

        px = [ball.pos[0] for ball in self.balls]
        py = [ball.pos[1] for ball in self.balls]
        vx = [ball.vel[0] for ball in self.balls]
        vy = [ball.vel[1] for ball in self.balls]

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


    def calc_then_show(self):
        """This calculates all the frames and then plays them back after."""

        hist = self.system.run(self.num_frames)

        fig, ax = plt.subplots()
        vis, = ax.plot([], [])
        collection = mpl.collections.PatchCollection([])
        ax.add_collection(collection)

        plt.gca().set_aspect('equal')
        ax.set_xlim([-1, 1])
        ax.set_ylim([-1, 1])

        def init():
            return vis,

        def update(frame):
            state = self.system.history[frame]
            px = [ball.pos[0] for ball in state.balls]
            py = [ball.pos[1] for ball in state.balls]
            vx = [ball.vel[0] for ball in state.balls]
            vy = [ball.vel[1] for ball in state.balls]
            # state.plot(ax_p=ax)
            # ax.add_collection(mpl.collections.PatchCollection(circles))
            collection.set_paths([plt.Circle((ball.pos[0], ball.pos[1]), radius=ball.radius, linewidth=10) for ball in state.balls])
            # quiver = ax.quiver(px, py, vx, vy)
            print(f'frame {frame}', end='\r')
            return vis,

        ani = FuncAnimation(fig, update, frames=self.num_frames, interval=1000/self.fps, init_func=init, blit=False)
        plt.show()


    def calc_then_show_EXP(self):
        """EXPERIMENTAL"""
        self.system.run(self.num_frames)

        fig, ax = plt.subplots()

        plt.gca().set_aspect('equal')
        ax.set_xlim([-1, 1])
        ax.set_ylim([-1, 1])
        px, py = ([ball.pos[0] for ball in self.system.history[0].balls], [ball.pos[1] for ball in self.system.history[0].balls])

        collection = mpl.collections.PatchCollection([plt.Circle((ball.pos[0], ball.pos[1]), radius=ball.radius, linewidth=10) for ball in self.system.history[0].balls])
        ax.add_collection(collection)

        (ln,) = ax.plot(px, py, animated=True)

        plt.show(block=False)
        plt.pause(0.1)
        bg = fig.canvas.copy_from_bbox(fig.bbox)
        ax.draw_artist(ln)
        fig.canvas.blit(fig.bbox)

        for frame in range(self.num_frames):
            state = self.system.history[frame]

            px, py = 1.0 * np.array([[ball.pos[0] for ball in state.balls], [ball.pos[1] for ball in state.balls]])
            vx, vy = 0.1 * np.array([[ball.vel[0] for ball in state.balls], [ball.vel[1] for ball in state.balls]])

            fig.canvas.restore_region(bg)
            collection.set_paths([plt.Circle((ball.pos[0], ball.pos[1]), radius=ball.radius, linewidth=10) for ball in state.balls])

            for i in range(len(state.balls)):
                ax.arrow(px[i], py[i], vx[i], vy[i], animated=True)

            ax.draw_artist(ln)

            fig.canvas.blit(fig.bbox)
            fig.canvas.flush_events()

            print(f'frame {frame}', end='\r')

            plt.pause(1 / 60)




if __name__ == "__main__":
    print("Test file for Animate.py")
    balls = np.array([Ball(0, 0, 0, 0, 0.1), Ball(0, 0.5, 0, -1, 0.1)])
    system = System(initial_state=State(balls), walls=None)
    anim = Animate(system=system, num_frames=50)
    anim.calc_then_show_EXP()
    print("Test finished.")
