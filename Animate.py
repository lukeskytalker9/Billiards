from System import System
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Animate:

    def __init__(self, system: System, num_frames, fps=30) -> None:
        self.system = system
        self.num_frames = num_frames
        self.fps = fps

    def show_live(self) -> None:
        fig, ax = plt.subplots()
        vis, _ = ax.plot([], [])

        def init():
            return vis, _

        def update(_):
            self.system.run(1)
            state = self.system.get_current_state()
            vis.set_data([b.pos[0] for b in state.balls], [b.pos[1] for b in state.balls])
            return vis, _

        ani = FuncAnimation(fig, update, frames=self.num_frames, interval=1000/self.fps, init_func=init, blit=True)
        plt.show()


    def calc_then_show(self):
        fig, ax = plt.subplots()
        vis, _ = ax.plot([], [])

        self.system.run(self.num_frames)

        def init():
            return vis, _

        def update(frame):
            state = self.system.history[frame]
            vis.set_data([b.pos[0] for b in state.balls], [b.pos[1] for b in state.balls])
            return vis, _

        ani = FuncAnimation(fig, update, frames=self.num_frames, interval=1000/self.fps, init_func=init, blit=True)
        plt.show()


if __name__ == "__main__":
    print("Test file for Animate.py")
    pass
