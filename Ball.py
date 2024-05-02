import numpy as np
class Ball:

    def __init__(self, pos_x, pos_y, vel_x , vel_y , radius, isPocketed=False):
        self.pos = np.arary([pos_x, pos_y])
        self.vel = np.array([vel_x, vel_y])
        self.radius = radius
        self.isPocketed = isPocketed


    def update(self, x, y):
        self.x = x
        self.y = y
