from __future__ import annotations
import numpy as np

"""
This is the Ball class and is used to store vital ball data as well as updating the position of the ball

By: Jack Biggins
"""
class Ball:

    __frictionContant = 0.05

    __slots__ = ['pos', 'vel', 'radius', 'isPocketed']

    def __init__(self, pos_x, pos_y, vel_x , vel_y , radius, isPocketed=False):
        self.pos = np.array([pos_x, pos_y] , dtype=float)
        self.vel = np.array([vel_x, vel_y] , dtype=float)
        self.radius = radius
        self.isPocketed = isPocketed

    #Uses euler-cromer method to update the position of the ball
    def update(self, tempstep) -> None:

        if self.isPocketed:
            return
        
        self.vel += -self.__frictionContant * tempstep * self.vel 
        self.pos += self.vel * tempstep



    def overlaps(self, other:Ball) -> bool:
        #Get distance between the two balls
        distance = np.linalg.norm(self.pos - other.pos)

        return distance < ( self.radius + other.radius )
    
    def placeInPocket(self):
        self.isPocketed = True
    
    # def bounce_velocity(self, other):
    #     # n = np.linalg.norm([1, -1/slope])
    #     n = other.pos - self.pos
    #     n = n / np.linalg.norm(n)
    #     self.vel = self.vel - 2 * (np.dot(self.vel, n)) * n

    def __str__(self) -> str:
        return f"Ball at {self.pos} with velocity {self.vel} and radius {self.radius} is pocketed: {self.isPocketed}"



if __name__ == "__main__":
    print("You are running the test file for Ball.py")

    x = Ball(0,0,1,0,1)
    y = Ball(2,0,1,0,1)
    print(x.overlaps(y))
    print(x)
    x.update(1)
    print(str(x))


