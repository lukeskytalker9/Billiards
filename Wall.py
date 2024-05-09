from Ball import Ball
import numpy as np
"""
This is the class for the wall which describes the wall of the pool table.

When assigning x and y values, the wall is assigned to the bottom righ corner 
of the wall like cartesian coordinates.

By: Jack Biggins
"""
class Wall:

    __slots__ = ['pos1', 'pos2' , 'tangentVector' , 'normalVector']


    def __init__(self, x1, y1 , x2OrAngle , y2OrLength , isPolar = False):

        #If the wall is in polar coordinates then convert to cartesian
        if (isPolar):
            x2 = x1 + y2OrLength * np.cos(x2OrAngle)
            y2 = y1 + y2OrLength * np.sin(x2OrAngle)

        else:
            x2 = x2OrAngle
            y2 = y2OrLength


        self.pos1 = np.array([x1, y1] , dtype=float)
        self.pos2 = np.array([x2, y2] , dtype=float)

        self.tangentVector = np.array([x2 - x1 , y2 - y1] , dtype=float) 
        self.tangentVector = self.tangentVector / np.linalg.norm(self.tangentVector)       

        self.normalVector = np.array([y2 - y1 , x1 - x2] , dtype=float)
        self.normalVector = self.normalVector / np.linalg.norm(self.normalVector)


    def isOverlapping(self, ball: Ball) -> bool:

        #Check if the ball is toughing the corner of pos1
        pos1ToBallVec = ball.pos - self.pos1
        #print(pos1ToBallVec)
        if (np.linalg.norm(pos1ToBallVec) < ball.radius):
            return True
        
        #Check if the ball is touching the corner of pos2
        pos2ToBallVec = ball.pos - self.pos2
        #print(pos2ToBallVec)
        if (np.linalg.norm(pos2ToBallVec) < ball.radius):
            return True


        
        pos1ToBallTangentUnit = np.dot(pos1ToBallVec, self.tangentVector) * self.tangentVector 
        pos1ToBallTangentUnit = pos1ToBallTangentUnit / np.dot(self.tangentVector, self.tangentVector)
        pos1ToBallTangentUnit  = pos1ToBallTangentUnit / np.linalg.norm(pos1ToBallTangentUnit)
        #print(pos1ToBallTangentUnit)

        pos2ToBallTangentUnit = np.dot(pos2ToBallVec, self.tangentVector) * self.tangentVector
        pos2ToBallTangentUnit = pos2ToBallTangentUnit / np.dot(self.tangentVector, self.tangentVector)
        pos2ToBallTangentUnit = pos2ToBallTangentUnit / np.linalg.norm(pos2ToBallTangentUnit)
        #print(pos2ToBallTangentUnit)

        """
        This is statement gives the tangent projection of the ball to each corner then makes them unit vectors.
        It is then true that if subtracting the vectors equals 0 then the ball is within the wall range

        if the ball is within the range of the wall
            then return true if the distance from the wall is less than the radius of the ball
        """
        sum = pos1ToBallTangentUnit + pos2ToBallTangentUnit
        print(sum)
        if (sum[0] == 0. and sum[1] == 0.):
            #print("Now checking if the ball is touching the wall")
            return self.__getDistanceFromWall(ball) < ball.radius

        #If none of the above cases trigger then they are not touching
        return False
    

    def collision(self, ball: Ball) -> None:
        
        # Calculate the normal and tangent components of the ball's velocity.
        normalVel = np.dot(ball.vel, self.normalVector) * self.normalVector
        normalVel = normalVel / np.dot(self.normalVector, self.normalVector) # This is to make sure the normal vector is a unit vector

        tangentVel = np.dot(ball.vel, self.tangentVector) * self.tangentVector
        tangentVel = tangentVel / np.dot(self.tangentVector, self.tangentVector)

        # Reflect the normal component of the ball's velocity.
        # ball.vel used to equal normalVel + tangentVel but we switch normal to show bounce
        ball.vel = tangentVel - normalVel



        # Update position
        distanceFromWall = self.__getDistanceFromWall(ball)
        ball.pos = ball.pos + self.normalVector * (ball.radius - distanceFromWall)

        #If this code runs then the normal vector was facing the wrong way
        if self.isOverlapping(ball):
            ball.pos = ball.pos - 2 * self.normalVector * (ball.radius - distanceFromWall)

        
    def __getDistanceFromWall(self, ball: Ball) -> float:
        distance = np.linalg.norm( np.cross(ball.pos - self.pos1 , self.pos2 - self.pos1) ) / np.linalg.norm(self.pos2 - self.pos1)
        return distance
        



if __name__ == "__!main__":

    print("Beginning the test file for Wall.py")

    print("Testing the isOverlapping method")
    ball = Ball(5,0.5,1,-1,1)
    wall = Wall(0,0,10,0)
    print(wall.isOverlapping(ball))
    print("\n\n")

    print("Testing the collision method")
    ball = Ball(5 , 4.5 , - 1 , 2 , 1)
    wall = Wall(0 , 0 , 10 , 10)
    print(ball)
    wall.collision(ball)
    print(ball)
    print("\n\n")
