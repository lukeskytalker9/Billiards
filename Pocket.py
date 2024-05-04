import numpy as np
from Ball import Ball

"""
This is the pocket class and is used to store the pocket data as well as checking if the ball has fallen into the pocket
"""
class Pocket:

    __slots__ = ['pos', 'radiusRange']

    def __init__(self, x , y , radiusRange):
        self.pos = np.array([x, y] , dtype=float)
        self.radiusRange = radiusRange

    """
    This method checks if the ball should have fallen into the pocket and declares the ball as in the pocket
    additionaly it returns a boolean True meaining it fell into the pocket.
    """
    def checkIfInPocket(self, ball:Ball) -> bool:
        distance = np.linalg.norm(self.pos - ball.pos)

        if (distance < self.radiusRange):
            #Ball Falls into pocket
            ball.placeInPocket()
            return True
        
        return False
    


