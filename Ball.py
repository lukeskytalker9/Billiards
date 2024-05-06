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
        
        self.vel += -1 * self.__frictionContant * tempstep * self.vel 
        self.pos += self.vel * tempstep



    def overlaps(self, other:Ball) -> bool:
        #Get distance between the two balls
        distance = np.linalg.norm(self.pos - other.pos)

        return distance < ( self.radius + other.radius )
    
    def placeInPocket(self):
        self.isPocketed = True


    """
    Here is the code to deal with collisions between balls.

    Note: Will I wrote this code here because you were having pushing error so I will
    temporarily write the code here and then move it to the system class later
    """
    def collision(self, other:Ball):
        #Update positions of the balls
        d = self.radius + other.radius - np.linalg.norm(other.pos - self.pos)

        normPositionVector = (other.pos - self.pos) / np.linalg.norm(other.pos - self.pos)

        updateLength = normPositionVector * d / 2

        self.pos = self.pos - updateLength * normPositionVector
        other.pos = other.pos + updateLength * normPositionVector


        #Update velocities of the balls

        tangentPosistionVector = np.array([-normPositionVector[1], normPositionVector[0]])
        tangentPosistionVector /= np.linalg.norm(tangentPosistionVector)

        Vi1t = np.dot(self.vel, tangentPosistionVector)
        Vi1n = np.dot(self.vel, normPositionVector)
        
        Vi2t = np.dot(other.vel, tangentPosistionVector)
        Vi2n = np.dot(other.vel, normPositionVector)

        #With constant velocity velecoties are just switched
        Vf1t = Vi2t
        Vf1n = Vi2n

        Vf2t = Vi1t
        Vf2n = Vi1n

        self.vel = Vf1t * tangentPosistionVector + Vf1n * normPositionVector
        other.vel = Vf2t * tangentPosistionVector + Vf2n * normPositionVector




    
    
    def __str__(self) -> str:
        return f"Ball at {self.pos} with velocity {self.vel} and radius {self.radius} is pocketed: {self.isPocketed}"


    

if __name__ == "__main__":
    print("You are running the test file for Ball.py")

    print("Testing the overlaps method")
    x = Ball(0,0,1,0,1)
    y = Ball(2,0,1,0,1)
    print(x.overlaps(y))
    print(x)
    x.update(1)
    print(str(x))
    print("\n\n")


    print("Testing the collision method")
    x = Ball(0,1,1,-1,1)
    y = Ball(1,0,-2,0,1)
    print(x)
    print(y)
    x.collision(y)
    print(x)
    print(y)

    print("\n\n")

