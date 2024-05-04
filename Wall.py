from Ball import Ball
import numpy as np
"""
This is the class for the wall which describes the wall of the pool table.

When assigning x and y values, the wall is assigned to the bottom righ corner 
of the wall like cartesian coordinates.

By: Jack Biggins
"""
class Wall:

    __slots__ = ['x', 'y' , 'length']

    def __init__(self, x, y , length):
        self.pos = np.array([x, y] , dtype=float)
        self.length = length



    def overlaps(self, ball: Ball) -> bool:
        raise NotImplementedError("This method should be implemented by a subclass")
    
    def updateBallVel(self, ball: Ball) -> None:
        raise NotImplementedError("This method should be implemented by a subclass")
    
