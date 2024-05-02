import numpy as np
class Ball:

    def __init__(self, pos_x, pos_y, vel_x , vel_y , radius, isPocketed=False):
        self.pos = np.arary([pos_x, pos_y])
        self.vel = np.array([vel_x, vel_y])
        self.radius = radius
        self.isPocketed = isPocketed

    #Uses euler-cromer method to update the position of the ball
    def update(self, x, y):
        for i in range(self.pos.shape[0]):
            
  
            self.pos[i] += self.vel[i]
            if self.pos[i] < 0 or self.pos[i] > x:
                self.vel[i] *= -1


    def overlaps(self, other):

        #return np.linalg.norm(self.pos - other.pos) < self.radius + other.radius
        return
