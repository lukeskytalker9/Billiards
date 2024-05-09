from __future__ import annotations
import numpy as np
from numpy.linalg import norm

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

        self.vel = self.vel + -self.__frictionContant * tempstep * self.vel
        self.pos = self.pos + self.vel * tempstep



    def overlaps(self, other: Ball) -> bool:
        #Get distance between the two balls
        distance = np.linalg.norm(self.pos - other.pos)

        return distance < ( self.radius + other.radius )

    def placeInPocket(self):
        self.isPocketed = True


    def bestCollision(self, other:Ball):
        d = self.radius + other.radius - np.linalg.norm(other.pos - self.pos)

        normPositionVector = (other.pos - self.pos) / np.linalg.norm(other.pos - self.pos)

        tangentPosistionVector = np.array([-normPositionVector[1], normPositionVector[0]])
        tangentPosistionVector = tangentPosistionVector / np.linalg.norm(tangentPosistionVector)

        Vi1t = np.dot(self.vel, tangentPosistionVector)
        Vi1n = np.dot(self.vel, normPositionVector)

        Vi2t = np.dot(other.vel, tangentPosistionVector)
        Vi2n = np.dot(other.vel, normPositionVector)


        velSum = np.abs(Vi1n) + np.abs(Vi2n)

        if velSum == 0:
            raise(ValueError, "Both balls have zero velocity, yet they are colliding!")
        selfFrac = Vi1n / velSum
        otherFrac = Vi2n / velSum

        print(f"selfFrac = {selfFrac}, otherFrac = {otherFrac}")
        print("normPositionVector = ", normPositionVector)
        print("d = ", d)

        update_length_self = normPositionVector * d * selfFrac
        update_length_other = normPositionVector * d * otherFrac

        print(f"update_length_self = {update_length_self}, update_length_other = {update_length_other}")

        #Switch back
        self.pos = self.pos - update_length_self
        other.pos = other.pos + update_length_other
        print(f"self.pos = {self.pos}, other.pos = {other.pos}")

        #Tangents Remain Unchanged - Think of bouncing off of a wall
        Vf1t = Vi1t
        Vf2t = Vi2t

        #Normals are switched - Think of bounign off a wall and the velocity is reversed
        Vf1n = Vi2n
        Vf2n = Vi1n

        self.vel = Vf1t * tangentPosistionVector + Vf1n * normPositionVector
        other.vel = Vf2t * tangentPosistionVector + Vf2n * normPositionVector





    """
    Here is the code to deal with collisions between balls.

    Note: Will I wrote this code here because you were having pushing error so I will
    temporarily write the code here and then move it to the system class later
    """
    def collision(self, other:Ball):
        #Update positions of the balls
        d = self.radius + other.radius - np.linalg.norm(other.pos - self.pos)

        normPositionVector = (other.pos - self.pos) / np.linalg.norm(other.pos - self.pos)
        """
        vel_sum = np.abs(self.vel) + np.abs(other.vel)
        # print(f"vel_sum = {vel_sum}", end='\r')

        if vel_sum[0] == vel_sum[1] == 0:
            # raise(ValueError, "Both balls have zero velocity, yet they are colliding!")
            updateLength = normPositionVector * d / 2
            self.pos = self.pos - updateLength
            other.pos  = other.pos + updateLength


        # ! Method 1: Move them apart according to the ratio of their velocites
        self_fraction = np.linalg.norm(self.vel) / vel_sum
        other_fraction = np.linalg.norm(other.vel) / vel_sum

        # updateLength = normPositionVector * d / 2
        update_length_self = normPositionVector * d * self_fraction
        update_length_other = normPositionVector * d * other_fraction

        self.pos = self.pos - update_length_self * normPositionVector
        other.pos = other.pos + update_length_other * normPositionVector
        """
        # Update velocities of the balls




         # ! Method 2: Move only the fastest ball back
        # updateLength = normPositionVector * d

        # if np.linalg.norm(self.vel) > np.linalg.norm(other.vel):
        #     self.pos = self.pos - updateLength * normPositionVector
        # else:
        #     other.pos = other.pos - updateLength * normPositionVector


        tangentPosistionVector = np.array([-normPositionVector[1], normPositionVector[0]])
        tangentPosistionVector = tangentPosistionVector / np.linalg.norm(tangentPosistionVector)

        Vi1t = np.dot(self.vel, tangentPosistionVector)
        Vi1n = np.dot(self.vel, normPositionVector)

        Vi2t = np.dot(other.vel, tangentPosistionVector)
        Vi2n = np.dot(other.vel, normPositionVector)


        # ! Method 3: Jack's method
        # #Update positions here
        velSum = np.abs(Vi1n) + np.abs(Vi2n)
        if velSum == 0:
            raise(ValueError, "Both balls have zero velocity, yet they are colliding!")
        selfFrac = Vi1n / velSum
        otherFrac = Vi2n / velSum

        update_length_self = normPositionVector * d * selfFrac
        update_length_other = normPositionVector * d * otherFrac

        self.pos = self.pos - update_length_self
        other.pos = other.pos + update_length_other


        # ! Method 4: Will
        #Update positions here

        # updateLength = normPositionVector * d

        # if np.linalg.norm(self.vel) > np.linalg.norm(other.vel):
        #     self.pos = self.pos - updateLength
        # else:
        #     other.pos = other.pos + updateLength

        # update_length_self = normPositionVector * d
        # update_length_other = normPositionVector * d

        # self.pos = self.pos - update_length_self
        # other.pos = other.pos + update_length_other

        #Tangents Remain Unchanged - Think of bouncing off of a wall
        Vf1t = Vi2t
        Vf2t = Vi1t

        #Normals are switched - Think of bounign off a wall and the velocity is reversed
        Vf1n = Vi2n
        Vf2n = Vi1n

        self.vel = Vf1t * tangentPosistionVector + Vf1n * normPositionVector
        other.vel = Vf2t * tangentPosistionVector + Vf2n * normPositionVector

    def __str__(self) -> str:
        return f"{self.pos}, {self.vel},"

    def __repr__(self) -> str:
        return self.__str__()

    def good_collision(self: Ball, other: Ball, method: int=2) -> None:
        """Rewriting the collision function because it got super cluttered."""

        # The distance between the centers of the two balls.
        dist_between_centers = norm(other.pos - self.pos)

        # The distance that they overlap, i.e., the distance that they must be moved apart.
        dist_overlapping = self.radius + other.radius - dist_between_centers

        # A unit vector which points from the center of self to the center of other.
        norm_dist_vec = (other.pos - self.pos) / norm(other.pos - self.pos)

        # A unit vector which is orthogonal to norm_dist_vec
        ortho_norm_vec = np.array([-norm_dist_vec[1], norm_dist_vec[0]]) / norm(np.array([-norm_dist_vec[1], norm_dist_vec[0]]))

        # The initial components of self.vel and other.vel which are in the direction of norm_dist_vec and ortho_dist_vec.
        init_self_ortho_vel = np.dot(self.vel, ortho_norm_vec)
        init_self_norm_vel = np.dot(self.vel, norm_dist_vec)
        init_other_ortho_vel = np.dot(other.vel, ortho_norm_vec)
        init_other_norm_vel = np.dot(other.vel, norm_dist_vec)

        # * First, update the positions using the given method.
        if method == 0:
            # Move only the fastest one
            if norm(self.vel) > norm(other.vel):
                self.pos = self.pos - norm_dist_vec * dist_overlapping
            else:
                other.pos = other.pos + norm_dist_vec * dist_overlapping
        elif method == 1:
            # move both by half
            self.pos = self.pos - norm_dist_vec * dist_overlapping / 2
            other.pos = other.pos + norm_dist_vec * dist_overlapping / 2

        elif method == 2:
            #This is the method where it updates depengin on the fraction
            
            velSum = np.abs(init_self_norm_vel) + np.abs(init_other_norm_vel)
            if velSum == 0:
                raise(ValueError, "Both balls have zero velocity, yet they are colliding!")
            selfFrac = init_self_norm_vel / velSum
            otherFrac = init_other_norm_vel / velSum

            update_length_self = norm_dist_vec * dist_overlapping * selfFrac
            update_length_other = norm_dist_vec * dist_overlapping * otherFrac

            self.pos = self.pos - update_length_self
            other.pos = other.pos + update_length_other
        else:
            if int(method) != method:
                raise TypeError("Method should be an int.")
            else:
                print("No collision method selected.")


        # * Now, update the velocities.

        # Apperently, orthogonal components are unchanged and the normal components switch.
        final_self_ortho_vel = init_self_ortho_vel
        final_other_ortho_vel = init_other_ortho_vel
        final_self_norm_vel = init_other_norm_vel
        final_other_norm_vel = init_self_norm_vel

        self.vel = final_self_ortho_vel * ortho_norm_vec + final_self_norm_vel * norm_dist_vec
        other.vel = final_other_ortho_vel * ortho_norm_vec + final_other_norm_vel * norm_dist_vec

if __name__ == "__main__":
    print("You are running the test file for Ball.py")

    print("Testing the overlaps method")
    x = Ball(0,0,1,0,1)
    y = Ball(2,0,1,0,1)
    print(x.overlaps(y))
    print(x)
    x.update(1)
    print("Step performed")
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

