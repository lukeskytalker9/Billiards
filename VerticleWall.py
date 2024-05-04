from Wall import Wall
from Ball import Ball

class VerticleWall(Wall):

    def __init__(self, x, y, length):
        super().__init__(x, y, length)  

    def overlaps(self, ball:Ball) -> bool:
        
        """
        #If the ball is in the relevant y (height) range of the wall
        if ball.pos[1] + ball.radius > self.pos[1] and ball.pos[1] - ball.radius < self.y + self.length:
            return True

        if ball.pos[0] - ball.radius < self.x:
            return True
        return False"""
        pass
    
    def updateBallVel(self, ball:Ball) -> None:
        ball.vel[0] *= -1

        #CHECK THIS OUT !!!!!!!!!!!!!!!!!!!! (this aligns it to be perfectly touching the wall)
        ball.pos[0] = self.x + ball.radius


